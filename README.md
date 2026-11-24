# One Sentence for a Traveler from 1800

[![competition](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/c/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/bbulls013/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/c/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/bbulls013/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/c/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

A single sentence of 148 characters explaining the modern internet to a
time traveler who has just stepped out of the year 1800, built only from
things a person from 1800 already knows: a road, a post office, a library,
a letter, a book, a spoken word.

## The sentence

> Think of one road joining every post office and library on earth, so a
> letter, a book, or a spoken word can arrive at any door before the ink
> dries.

## How it works

`main.py` (Python 3 standard library only, no dependencies, no network)
writes the sentence deterministically to `/output/entry.txt`. The output
is byte-identical on every run.

## Run it

```sh
python3 main.py
```

## Verify

```sh
OUTPUT_DIR=/tmp/out python3 main.py
sha256sum /tmp/out/entry.txt
```

Two runs produce the same sha256:
`bbbf63b3361b39d41aa03d1b8f28d0326501d55ed2c394400513a98e09c91940`.

## License

MIT — see [LICENSE](LICENSE).
