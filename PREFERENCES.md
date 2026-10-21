# Loo's preferences

Decisions already made. Respect these unless he says otherwise.
If he contradicts something here, he wins — but note it in one line so
he knows the record is changing.

---

## Already rejected — don't re-suggest

| Thing | Verdict |
|---|---|
| Em dash (—) as a bullet term separator | **Rejected.** Reads as AI-written. Use a colon. |
| Bullet dots (•) | **Rejected.** Replaced with vertical hairline rails. |
| Bold weight 600 / 700 for headings | **Too heavy.** Settled on 450. |
| 1px+ hairlines | **Too prominent.** Settled on 0.7px. |
| 0.5px hairlines | **Too faint.** 0.7px is the answer. |
| Thick coloured rail grouping the DocDoc roles | **Rejected.** Roles sit flush left instead. |
| Solid lines that looked dotted-but-dense | He wants dots clearly separated if dotted at all. Currently solid. |
| Separate vertical rails per bullet | **Rejected.** One continuous rail per group. |
| Grey horizontals + coloured verticals (mismatched) | **Rejected.** All rules share one colour and weight. |
| Heavy rule under the name / under the contact strip | **Removed.** |
| Rule above the page-2 footer | **Removed.** |

---

## Settled design decisions

- **Two pages.** Not one, not three, unless he says so.
- **Reverse chronological** everywhere — experience and education.
- **Hairlines:** 0.7px, `#9ADEC0`, identical for horizontal rules and
  vertical rails.
- **Accent:** `#047857`. Used for section labels and link text only.
- **Link underlines:** visible, `#6EE7B7`, with offset from the text.
  He specifically complained when these were too subtle.
- **Every bullet** leads with a bold 1–2 word Title Case term + colon.
- **Gutter tags are domains** (Healthcare, Fintech, Property), never
  employment type. Contract status goes in the tag beside the job title.
- **Font:** Schibsted Grotesk. Weights are real extracted instances —
  never synthetic bold (it renders as regular weight in this pipeline).

---

## Content facts — verified, don't "correct" these

These were checked against his MOM employment records. They differ from
older copies of his resume that may be floating around.

- **Plus65 Interactive:** Jun 2017 – Jun 2019 (not May 2017)
- **Immensinc:** Mar 2014 – May 2015 (single engagement)
- **DocDoc:** one employer, two roles —
  UI/UX Designer Sep 2020 – Mar 2022, promoted to
  Senior UI/UX Designer Apr 2022 – Apr 2024
- **Doctor World:** May 2020 – Jul 2020, contract
- **Tomie Technologies:** Feb 2025 – Apr 2025, contract
- A "Freelance UX Designer (Aug 2019 – Sep 2020)" entry appears on
  older versions. It was **deliberately removed.** Don't restore it.

---

## Working style

- He wants to **see proposed text before it goes into the PDF.**
- He gives feedback in batches of several points at once. Address
  every point, and say which ones you did.
- He notices when something is claimed as fixed but isn't. Verify
  before saying it's done — `verify.py` exists for this.
- If he reports a problem you can't reproduce, **say so and ask**,
  rather than changing something at random.
