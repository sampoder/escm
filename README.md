# 🌈 `escm <your-code>.escm`

Scheme, now written with emojis. Install it on your computer by downloading `escm.py` and editing your shell's configuration path to include:

```bash
escm() {
  if [ -z "$1" ]; then
    echo "Usage: escm [path_to_file].escm"
  else
    if [[ $1 == *.escm ]]; then
      python3 /path/to/escm.py "$1"
      [your_scheme_interpreter] "${1%.escm}.scm"
    else
      echo "Usage: escm [path_to_file].escm"
    fi
  fi
}
```

Docs coming soon.
