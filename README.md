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

Usage is fairly simple, write Scheme as you usually would but use emojis for actions / command words instead of words.

Here's the list of currently available aliases:

| Emoji | Function | Emoji | Function |
|-------|----------|-------|----------|
| ▶️   | begin    | 🟰   | define   |
| 🤷   | if       | 📏   | length   |
| 📞   | apply    | 🖨️   | display  |
| 📝   | displayln | ⚠️   | error    |
| 🔍   | eval     | 🚪   | exit     |
| 📂   | load     | ↩️   | newline  |
| 🖨️‍   | print    | 📃?  | atom?    |
| 🔢?  | integer? | 📦?  | list?    |
| 👥?  | pair?    | 💡?  | procedure? |
| 🔮?  | promise? | 🔤?  | string?  |
| 🔣?  | symbol?  | 🗑️?  | null?    |
| 📄➕  | append   | 🥕   | car      |
| 📤   | cdr      | ✌️➕  | cons     |
| 📓   | list     | 🗺️   | map      |
| 🕵️   | filter   | 🔀   | reduce   |
| 1️⃣! | set-car! | 2️⃣! | set-cdr! |
| ➕   | +        | ➖   | -        |
| ✖️   | *        | ➗   | /        |
| 😏   | abs      | ⬆️   | expt     |
| 🔗   | modulo   | 😃   | quotient |
| ⏫   | remainder | 🌒   | acos     |
| 🌓   | acosh    | 🌗   | asin     |
| 🌘   | asinh    | 🌛   | atan     |
| 🌜   | atan2    | 🌙   | atanh    |
| 🌆   | ceil     | 🌅   | copysign |
| 🌄   | cos      | 🌃   | cosh     |
| 🌄   | degrees  | 🌇   | floor    |
| 🌈   | log      | 🌈🔟  | log10    |
| 🌊   | log1p    | 🌊2️⃣ | log2     |
| 🌌   | radians  | 🌟   | sin      |
| 🌠   | sinh     | 🌋   | sqrt     |
| 🌚   | tan      | 🌞   | tanh     |
| 🌡️   | trunc    | 🟰?  | eq?      |
| 🤝?  | equal?   | ❌   | not      |
| 🔵?  | even?    | 🔴?  | odd?     |
| 0️⃣?  | zero?    | 🔁   | cond     |
| 🤝   | and      | 🙏   | or       |
| 🏷️   | let      | 🏁   | begin    |
| 📑   | lambda   | 📜   | quote    |
| 🟰-🤏 | define-macro | 🔎   | expect   |
| 🔁-✂️ | unquote-splicing | 🕒   | delay    |
| 🌊-🌊 | cons-stream | 🔒!  | set!     |


###### 🐻 Shoutout to any future 61A-ers learning Scheme! That was the inspiration for this project... wahoo :)
