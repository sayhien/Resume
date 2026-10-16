#!/usr/bin/env bash
# Build the resume PDF from resume.html
# Usage:  bash build.sh
set -e

OUT="${1:-Loo_Say_Hien_Resume.pdf}"

echo "==> checking dependencies"
python3 -c "import weasyprint" 2>/dev/null || pip install weasyprint --break-system-packages -q
python3 -c "import pymupdf"    2>/dev/null || pip install pymupdf    --break-system-packages -q

echo "==> rendering HTML to PDF"
python3 -c "from weasyprint import HTML; HTML('resume.html').write_pdf('_raw.pdf')"

echo "==> normalising link rectangles (REQUIRED - see README)"
python3 fix_links.py _raw.pdf "$OUT"
rm -f _raw.pdf

echo "==> verifying output"
python3 verify.py "$OUT"

echo ""
echo "Done: $OUT"
