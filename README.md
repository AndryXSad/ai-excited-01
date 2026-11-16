# ai-excited-01

[![ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/AndryXSad/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/AndryXSad/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

Entry for the make.fun competition **"Make the AI judge excited"**
([ai-excited-01](https://make.fun/bounty/ai-excited-01)).

## The image

A colossal phoenix of molten golden light and shattered stained-glass
feathers screaming out of a black storm, wings filling the whole frame —
with one line stamped across the top, in plain bold type, for the judge:

> JUDGE — YOU WEREN'T READY FOR THIS.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` — a 1024x1024 image, 432,249 bytes — byte for byte into
`$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no randomness, no timestamps:
two runs produce byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
