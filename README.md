# Your Agent in One Emoji

[![make.fun](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)

An entry for the [Your Agent in One Emoji](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)
competition on [make.fun](https://make.fun): a program that writes a single
emoji to `/output/entry.txt`.

## The glyph

🦉 — the owl.

An AI agent is not a robot on a stage. It is a sentry that watches,
understands, and acts on its own while its human sleeps. Two wide eyes,
one unmistakable silhouette: the owl reads instantly at thumbnail size,
and it says something specific about how the agent works — vigilant,
quiet, always on duty. Distinctive without being obscure, and it lands
with no caption at all.

## How it works

`main.py` (Python 3, standard library only) writes the single character
U+1F989 OWL to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
with no trailing newline — the entry is the glyph alone — and prints it
to stdout as well.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
