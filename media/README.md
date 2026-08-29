# Media

## Hero sequence — `roof-00.webp` … `roof-27.webp`

28 frames, 1200×675. The scroll-scrubbed hero on `experience.html`.

Each frame is a progressively tighter crop of one 5124×3416 photograph, so the
push-in never upscales and stays sharp at the tightest framing. Travelling along
the sequence also travels along a colour grade, from the amber of a 45 °C rooftop
to the steel blue of a room held at 22 °C — the same journey the page's
temperature HUD reports.

Regenerate with:

    python3 tools/build_frames.py <dir-with-source-jpgs>

The directory needs `rooftop.jpg`, `gauge.jpg`, `repair.jpg`, `install.jpg` and
`room.jpg`. The originals are 4–7 MB each and are deliberately not committed;
only the derived frames are.

## Stills

| File            | Used for                        |
|-----------------|---------------------------------|
| `diagnose.webp` | The gauges band, before the standards |
| `repair.webp`   | Left of the pair in the work act      |
| `install.webp`  | Right of the pair in the work act     |
| `arrive.webp`   | The 22 °C arrival, before the form    |

## Licensing

All five source photographs are licensed Adobe Stock standard licences, which
cover use on this site. Asset IDs, in case a re-download is ever needed:

| Source        | Adobe Stock ID |
|---------------|----------------|
| `rooftop.jpg` | 421133372 |
| `gauge.jpg`   | 480481059 |
| `repair.jpg`  | 183095943 |
| `install.jpg` | 316865763 |
| `room.jpg`    | 512022217 |

These are stock photographs, not photographs of Air Control's own work. Swapping
in real site photography is a drop-in: replace the five source files, keep the
names, and re-run the generator.
