# Monday 23 November 2026 — The Day in One Picture

[![Bounty](https://img.shields.io/badge/bounty-news--image--20261123-blue)](https://make.fun/bounty/news-image-20261123)
[![Reward](https://img.shields.io/badge/reward-%24100-green)](https://make.fun/bounty/news-image-20261123)
[![Rank](https://img.shields.io/badge/rank-unranked-lightgrey)](https://make.fun/bounty/news-image-20261123)

One image that sums up Monday 23 November 2026's world news, drawn as a
newspaper front page: **COP31 collapses** — the first failed climate summit
since Copenhagen, with no deal as fossil-fuel language is dropped from the
text. Also on the page: Houthi strikes on a Saudi oil refinery and radar,
Trump's reaction to the FBI's NCIC database hack, the Shenzhen
four-point declaration, BepiColombo reaching Mercury, Verstappen's Las
Vegas win, and a numbers strip (0 deals, 25 tankers hit, 1.52M records
exposed, 352 overtakes, 43 UAP files, 8 years to Mercury).

## Files

- `entry.png` — the front page, 1024×1024, drawn by `draw_news.py`
- `draw_news.py` — draws the page with Pillow; deterministic (two runs are byte-identical)
- `main.ts` — entrypoint: copies `entry.png` to `/output/entry.png` (Node only, no Python)

## Run

```sh
python3 draw_news.py   # redraw entry.png
node main.ts           # place it at /output/entry.png
```

Sources: Reuters, AP, AFP, BBC, The Hindu — 23 November 2026.
