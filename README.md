# Installation

```
virtualenv -p python3 venv
. venv/bin/activate
pip install .
```

# Running at startup

Put this in your `~/.xprofile`:

```
(. ~/path/to/veganpizza/venv/bin/activate && python ~/path/to/veganpizza/run.py &)
```
