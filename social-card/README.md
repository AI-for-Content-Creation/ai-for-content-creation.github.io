# Social / link-preview card

This folder generates `images/sm-card.jpg` — the image that expands when the
workshop URL is shared on social media, Slack, etc. (the Open Graph /
`twitter:image` card referenced from `index.html`).

The card is a CVPR promo showing the workshop name, date/time, room, topics,
and a row of the invited speakers with their photos.

## Regenerate

```bash
pip install pillow
python social-card/generate_card.py          # current year (default 2026)
python social-card/generate_card.py 2027     # a specific year
```

Output:
- `images/sm-card.jpg` — used by the live site (commit this).
- `social-card/<year>/sm-card-<year>.jpg` — archived copy for that year.

## Inputs

| What | Where |
| --- | --- |
| Speaker names / affiliations / talk times | `_data/speakers_<year>.csv` (already used by the website) |
| Speaker headshots | `social-card/<year>/speakers/<lastname>.jpg` |
| Date / time / room / topics | the `EVENT` dict at the top of `generate_card.py` |

Headshot filenames are the speaker's **last name, lower-cased**
(e.g. `Saining Xie` → `xie.png`). `.jpg`, `.jpeg`, `.png`, `.webp` all work.
Speakers are ordered by their `time` column.

If a face sits high or low in its photo (e.g. a full-body shot), nudge the
crop with the per-speaker `focus` map in the `EVENT` dict
(`0.0` = top, `0.5` = centre, `1.0` = bottom; default `0.42`).

## Make next year's card

1. Copy `social-card/2026/` → `social-card/2027/` and replace the headshots.
2. Update `_data/speakers_2027.csv` (the site needs this anyway).
3. Add a `2027` entry to the `EVENT` dict in `generate_card.py`.
4. Run the script and commit `images/sm-card.jpg`.

## Source headshots (2026)

Downloaded from each speaker's homepage (linked in `_data/speakers_2026.csv`),
used to promote their workshop talk.
