# README — technical reference

New here? Read `START_HERE.md` first. This file is for when you need
detail: adding a job, changing layout, or debugging.

---

## Build

```bash
bash build.sh
```

Renders `resume.html` → fixes links → verifies. Output:
`Loo_Say_Hien_Resume.pdf`.

Manual equivalent:

```bash
pip install weasyprint pymupdf
python3 -c "from weasyprint import HTML; HTML('resume.html').write_pdf('_raw.pdf')"
python3 fix_links.py _raw.pdf resume.pdf
python3 verify.py resume.pdf
```

Run from inside this folder so fonts and the photo resolve.

---

## Files

| File | What it is |
|---|---|
| `START_HERE.md` | Read first. Build command + when to ask Loo. |
| `PREFERENCES.md` | Loo's taste and rejected options. Read before visual changes. |
| `resume.html` | All content + styling. The only file you normally edit. |
| `build.sh` | One-command build. |
| `fix_links.py` | Makes PDF links clickable. Mandatory — see below. |
| `verify.py` | Self-check. |
| `SchibstedGrotesk-*.ttf` | Fonts: 400, 450, 500, 600, 700. |
| `photo.png` | Profile photo. |

---

## Changing the look

`resume.html` has a `:root` block near the top. Change these, not the
individual rules scattered through the CSS:

```css
--accent:      #047857;   /* section labels, link text */
--link-rule:   #6EE7B7;   /* underline beneath links */
--rule:        #9ADEC0;   /* all hairlines */
--rule-weight: 0.7px;     /* thickness of every hairline */
```

---

## Adding a job

Standard entry:

```html
<div class="entry">
    <div class="gutter">
        <div class="yr">Feb 2025 —<br>Apr 2025</div>
        <div class="tagline">Sustainability</div>
    </div>
    <div class="body-col">
        <div class="job-title">UI/UX Designer<span class="contract-tag">Contract</span></div>
        <div class="company">Tomie Technologies Pte Ltd</div>
        <div class="lede">Optional one-line summary.</div>
        <ul class="points">
            <li><b>Term:</b> Bullet text.</li>
        </ul>
    </div>
</div>
```

Drop the `contract-tag` span for permanent roles. `.lede` is optional.

One company, two roles (a promotion) — keep it as **one** entry so it
doesn't read as two employers:

```html
<div class="entry">
    <div class="gutter">
        <div class="yr">Sep 2020 —<br>Apr 2024</div>
        <div class="tagline">Healthcare · Insurance</div>
    </div>
    <div class="body-col">
        <div class="company-head">DocDoc Pte Ltd</div>
        <div class="promo-rail">
            <div class="role-block">
                <div class="role-line">
                    <div class="role-name">Senior UI/UX Designer</div>
                    <div class="role-dates">Apr 2022 – Apr 2024</div>
                </div>
                <ul class="points"><li><b>Term:</b> ...</li></ul>
            </div>
            <!-- earlier role follows, same shape -->
        </div>
    </div>
</div>
```

---

## Troubleshooting

**"It's three pages now."**
Reduce `body { font-size }` by 0.2pt, or `.entry { margin-bottom }` by
2px. Ask Loo first if it needs a real cut — see `START_HERE.md`.

**"An entry jumped to the next page and left a gap."**
WeasyPrint can't split flex containers across pages. Each `.entry` has
`break-inside: avoid` and must fit on one page. Shorten it.

**"The links don't work."**
Check in this order:
1. Run `python3 verify.py <pdf>`. If it passes, the file is fine.
2. Ask how he's viewing it. Chat apps and in-browser previews often
   rasterise PDFs to images, so no link is clickable there. Ask him to
   download it and open in a browser or a real PDF viewer.
3. Only then look for a bug.

This exact sequence has already burned time once. Don't skip to step 3.

**"The bold text looks flat / not bold."**
Synthetic bolding silently renders as regular weight here. Use a real
extracted font instance and register a new `@font-face`. All five
weights are already in this folder.

**"verify.py says wrong number of links."**
If you intentionally added or removed links, update `EXPECTED_LINKS`
at the top of `verify.py`.
