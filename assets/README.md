# Curiosity Den artwork

The profile uses local SVGs: `banner-{dark,light}.svg` for the welcome and
`desk-notes-{dark,light}.svg` for the rotating notebook, and
`card-*-{dark,light}.svg` for the six animated disclosure cards. Both palettes are selected
with GitHub's supported `<picture>` markup.

Cards are capped at 520 px wide in the README (about 81 px tall), and shrink to
fit smaller screens. `cookie-case-{dark,light}.svg` illustrates the optional
cookie mystery inside the final card. The scenario is fictional; it is not a
live shop, counter, or telemetry display.

Edit the colors, text, or animation in `scripts/generate-assets.py`, then run from
the repository root:

```sh
python scripts/generate-assets.py
```

Python 3.10 or newer is sufficient; no packages, tokens, scheduled jobs, or image
services are needed. Commit the generated SVGs along with generator changes.

Animations are CSS inside the SVG files, with a static fallback when reduced
motion is requested or animation is unavailable. The README also includes every
rotating desk note as selectable text. The orbit and robot are illustrations,
not live activity or build indicators.

Click interactions use image cards inside native `<details>` / `<summary>`
elements and ordinary links. Card artwork animates independently; opening a
card reveals short text below it with the browser's normal disclosure behavior.
Cards switch to larger, title-only labels at small image widths for readability.
GitHub does not allow custom slide-in panels, CSS transitions on the README's
disclosures, or JavaScript event handlers. The local preview deliberately keeps
those same interaction limits. See
[GitHub's rendering pipeline](https://github.com/github/markup) and
[collapsed-section documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).
