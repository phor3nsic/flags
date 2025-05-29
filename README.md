# flags

Parse stdin to emogi flags...

### Usage:

```sh
echo "[CVE-2023-5561] [http] [medium] https://example/?rest_route=/wp/v2/users&search=@ [route="?rest_route=/wp/v2/users&"]" | flags | notify -silent
```

You recive message like:

```
🟠 MEDIUM: [CVE-2023-5561] [http] [medium] https://example/?rest_route=/wp/v2/users&search=@ [route=?rest_route=/wp/vx/users]
```

### Install

- via pipx:

```sh
pipx install git+https://github.com/phor3nsic/flags
```
- via pip:

```sh
pip install git+https://github.com/phor3nsic/flags
```
