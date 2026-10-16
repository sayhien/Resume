#!/usr/bin/env python3
"""
Fix link annotations in a WeasyPrint-generated PDF.

WeasyPrint writes /Rect arrays with y0 > y1 (inverted), which some PDF
viewers reject, making links unclickable. This normalizes every link
rect to [x_min, y_min, x_max, y_max] and adds explicit border/flag keys.
"""
import sys
import pymupdf


def fix_links(path_in, path_out):
    doc = pymupdf.open(path_in)
    fixed = 0

    for pno in range(len(doc)):
        page = doc[pno]
        annots_key = doc.xref_get_key(page.xref, "Annots")
        if annots_key[0] != "array":
            continue

        # collect annotation xrefs from e.g. "[7 0 R 8 0 R]"
        import re
        xrefs = [int(m) for m in re.findall(r"(\d+)\s+\d+\s+R", annots_key[1])]

        for xr in xrefs:
            obj = doc.xref_object(xr)
            if "/Link" not in obj:
                continue

            rect_key = doc.xref_get_key(xr, "Rect")
            if rect_key[0] != "array":
                continue

            nums = [
                float(t)
                for t in rect_key[1].replace("[", " ").replace("]", " ").split()
            ]
            if len(nums) != 4:
                continue

            x0, y0, x1, y1 = nums
            nx0, nx1 = min(x0, x1), max(x0, x1)
            ny0, ny1 = min(y0, y1), max(y0, y1)

            # pad slightly so the hit area is comfortable to tap
            pad = 1.0
            ny0 -= pad
            ny1 += pad

            doc.xref_set_key(
                xr, "Rect", f"[ {nx0:.4f} {ny0:.4f} {nx1:.4f} {ny1:.4f} ]"
            )
            # no visible border, but ensure annotation prints & is enabled
            doc.xref_set_key(xr, "Border", "[ 0 0 0 ]")
            doc.xref_set_key(xr, "F", "4")
            fixed += 1

    doc.save(path_out, garbage=3, deflate=True)
    doc.close()
    return fixed


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else src
    n = fix_links(src, dst)
    print(f"normalized {n} link annotations -> {dst}")
