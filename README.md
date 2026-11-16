# ai-excited-01

[![ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/AndryXSad/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/AndryXSad/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

My entry for make.fun's **ai-excited-01** bounty: make the AI judge excited.

## The image

A golden phoenix bursting out of dark smoke, wings spread wide, feathers
shattering into glowing stained-glass shards — with one line staring the
judge down from the top of the frame:

> JUDGE — YOU WEREN'T READY FOR THIS.

Fire, motion, and a dare, all in one frame. The phoenix is the jolt; the
text is the twist.

## How it works

`main.py` (Python 3, standard library only) copies the bundled `entry.png`
into the output directory and checks the copy's size. No network, no
randomness — run it twice and the output bytes are identical.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
