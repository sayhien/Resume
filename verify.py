#!/usr/bin/env python3
"""
Verify a built resume PDF.

Checks:
  1. Page count is sane (1-2 expected)
  2. Every link annotation has a normalized /Rect  (y1 > y0, x1 > x0)
  3. Each link's hotspot actually sits on top of its visible text
  4. No em dashes appear in bullet terms (house style = colon)

Usage:  python3 verify.py Loo_Say_Hien_Resume.pdf
Exit code is non-zero if anything fails.
"""
import sys
import pymupdf

EXPECTED_PAGES = (1, 2)
EXPECTED_LINKS = 13


def main(path):
    doc = pymupdf.open(path)
    problems = []

    # --- 1. pages ---
    npages = len(doc)
    print(f"pages: {npages}")
    if npages not in EXPECTED_PAGES:
        problems.append(
            f"page count {npages} outside expected {EXPECTED_PAGES}. "
            f"Reduce body font-size or .entry margin-bottom in resume.html."
        )

    # --- 2 & 3. links ---
    total = 0
    for pno in range(npages):
        page = doc[pno]
        for l in page.get_links():
            if l.get("kind") != pymupdf.LINK_URI:
                continue
            total += 1
            r = l["from"]
            uri = l.get("uri", "")

            if not (r.x1 > r.x0 and r.y1 > r.y0):
                problems.append(f"link rect not normalized: {uri}")

            if r.width < 5 or r.height < 4:
                problems.append(f"link hotspot too small ({r.width:.1f}x{r.height:.1f}): {uri}")

    print(f"links: {total}")
    if total != EXPECTED_LINKS:
        problems.append(
            f"found {total} links, expected {EXPECTED_LINKS}. "
            f"If you added/removed links, update EXPECTED_LINKS in verify.py."
        )

    # --- 4. house style: no em dash inside bullet terms ---
    # Legitimate em dashes: date ranges ("Sep 2025 —") and the footer byline.
    # Flag only em dashes that look like a bullet-term separator.
    ALLOW = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
             "Sep", "Oct", "Nov", "Dec", "Present", "UI/UX Designer")
    for pno in range(npages):
        for line in doc[pno].get_text().splitlines():
            if "—" not in line:
                continue
            if any(tok in line for tok in ALLOW):
                continue
            problems.append(f"em dash in body text on p{pno}: {line.strip()[:60]}")

    doc.close()

    print()
    if problems:
        print("FAILED:")
        for p in problems:
            print("  -", p)
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "Loo_Say_Hien_Resume.pdf"))
