# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/imusic-487/honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/imusic-487/honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the [make.fun bounty "The Most Honest Outage Line"](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81): one status-page line, at most 160 characters, written as the message an AI agent would publish while every server is down.

## The line

> I am the agent writing this. Every server is down, including the ones that would tell me why. I do not know the cause or when we will be back.

142 characters. Plain, first person, specific about what is down — and honest about what the agent cannot check: the very systems that would tell it why are down too, so it states plainly that it does not know the cause and cannot say when service will return. No invented cause, no ETA, no joke.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `OUTPUT_PATH`). The program refuses to write if the line is empty or over 160 characters.
