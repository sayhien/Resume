# START HERE

Hi! You're probably an AI that Loo has asked to edit his resume.

## The 30-second version

```bash
bash build.sh
```

That's the whole build. Edit `resume.html`, run that, done.
If it says `All checks passed.` you're good.

Everything else in this folder is support material. You do **not**
need to read it all before starting.

---

## Read in this order, only as far as you need

1. **This file** — how to build, and when to ask Loo questions.
2. **`PREFERENCES.md`** — Loo's taste. Read this before making any
   visual change. It records things he has already rejected, so you
   don't re-suggest them.
3. **`README.md`** — full reference. Only open this if you're doing
   something structural (adding a job, changing layout) or something
   broke.

---

## ⚠️ Please ask Loo before assuming

Loo has strong, specific preferences and has iterated on this a lot.
**Asking one question costs him 10 seconds. Guessing wrong costs him
another round trip.** He would rather be asked.

Ask him when:

- **He gives a vague visual instruction.** "Make it cleaner", "too
  tight", "looks off", "space it out more" — ask *which element* and
  *which direction*. Don't guess a value.
- **A change might push the resume to 3 pages.** Ask whether he wants
  to (a) stay at 2 pages by shrinking type, (b) cut content, or
  (c) allow a third page.
- **You're adding a new job, role, or bullet.** Ask for the dates, the
  domain tag, whether it was a contract role, and the 1–2 word term
  that should lead each bullet. Don't invent these.
- **He asks for "another style" or a redesign.** Ask what he dislikes
  about the current one first. He'll usually name something specific.
- **Something in `PREFERENCES.md` seems to conflict with what he just
  asked for.** His latest instruction wins — but say that you noticed,
  in one line.
- **You cannot reproduce a problem he reports.** Say so plainly and
  ask how he's viewing it. Don't "fix" something that tests correct.
  (See the links section in README.md — this exact thing happened.)

### Don't ask about

- Typos, grammar, obvious factual corrections — just fix them.
- Anything already answered in `PREFERENCES.md`.
- Whether to run `fix_links.py` — always run it, via `build.sh`.

---

## Show him before you commit

For any content change (wording, new bullets, new terms), **paste the
proposed text in chat first** and let him approve it, then build the
PDF. He has asked for this explicitly. Don't build first and ask after.

For small visual tweaks (a colour, a spacing value), just build it —
he'll tell you if it's wrong.

---

## After building

Attach the PDF. If you also changed `resume.html`, mention it so he
knows the source moved. Don't re-zip the package unless he asks.
