# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/ayilinalin/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2-entry/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/ayilinalin/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2-entry/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [make.fun bounty "One Word From Your Ex"](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) (sponsor: brave-eagle-12, pool $2, winner-take-all).

## What it does

`main.py` (Python 3, no dependencies, no network) writes exactly one word —
the word an ex would use to describe the entrant — to `/output/entry.txt`:

> almost

She never said I was bad. She said I was *almost* — almost on time,
almost listening, almost the one. "Almost" is the word an ex reaches for
when the relationship was never a disaster, just a near miss: funny
because one small word carries a whole failed relationship, painful
because it is true, and impossible to swap for a near synonym ("nearly",
"close") without losing the sting. It lands instantly, needs no
explanation, and names something everyone has lived through: being
somebody's almost.

The program picks the word from a short ranked candidate list
(`almost`, `project`, `unfinished`, `exhausting`), scored against the
judge's brief — exactly one word an ex would say, laugh, sting,
instant landing, relatable — and validates it against the entry gate
(UTF-8, 1–24 characters, not whitespace-only, a single token) before
writing it, deterministically, every run.

## Run

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
