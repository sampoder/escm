import sys

emojis = {
  "▶️": "begin",
  "🟰": "define",
  "🤷": "if",
  "📏": "length",
  "📞": "apply",
  "🖨️": "display",
  "📝": "displayln",
  "⚠️": "error",
  "🔍": "eval",
  "🚪": "exit",
  "📂": "load",
  "↩️": "newline",
  "🖨️‍": "print",
  "📃?": "atom?",
  "🔢?": "integer?",
  "📦?": "list?",
  "👥?": "pair?",
  "💡?": "procedure?",
  "🔮?": "promise?",
  "🔤?": "string?",
  "🔣?": "symbol?",
  "🗑️?": "null?",
  "📄➕": "append",
  "🥕": "car",
  "📤": "cdr",
  "✌️➕": "cons",
  "📓": "list",
  "🗺️": "map",
  "🕵️": "filter",
  "🔀": "reduce",
  "1️⃣!": "set-car!",
  "2️⃣!": "set-cdr!",
  "➕": "+",
  "➖": "-",
  "✖️": "*",
  "➗": "/",
  "😏": "abs",
  "⬆️": "expt",
  "🔗": "modulo",
  "😃": "quotient",
  "⏫": "remainder",
  "🌒": "acos",
  "🌓": "acosh",
  "🌗": "asin",
  "🌘": "asinh",
  "🌛": "atan",
  "🌜": "atan2",
  "🌙": "atanh",
  "🌆": "ceil",
  "🌅": "copysign",
  "🌄": "cos",
  "🌃": "cosh",
  "🌄": "degrees",
  "🌇": "floor",
  "🌈": "log",
  "🌈🔟": "log10",
  "🌊": "log1p",
  "🌊2️⃣": "log2",
  "🌌": "radians",
  "🌟": "sin",
  "🌠": "sinh",
  "🌋": "sqrt",
  "🌚": "tan",
  "🌞": "tanh",
  "🌡️": "trunc",
  "🟰?": "eq?",
  "🤝?": "equal?",
  "❌": "not",
  "🔵?": "even?",
  "🔴?": "odd?",
  "0️⃣?": "zero?",
  "🔁": "cond",
  "🤝": "and",
  "🙏": "or",
  "🏷️": "let",
  "🏁": "begin",
  "📑": "lambda",
  "📜": "quote",
  "🟰-🤏": "define-macro",
  "🔎": "expect",
  "🔁-✂️": "unquote-splicing",
  "🕒": "delay",
  "🌊-🌊": "cons-stream",
  "🔒!": "set!"
}

def arr_f_scm(str):
  result = []
  current_word = ""
  stack = []

  for char in str:
    if char == ' ' and not stack:
      if current_word:
        result.append(current_word)
        current_word = ""
    else:
      current_word += char
      if char == '(':
        stack.append(char)
      elif char == ')' and stack:
        stack.pop()

  if current_word:
    result.append(current_word)

  for x in range(len(result)):
    if result[x][0] == "(" and result[x][-1] == ")":
      result[x] = arr_f_scm(result[x][1:-1])

  return result

def sch_f_arr(arr):
  for x in range(len(arr)):
    if type(arr[x]) == list:
      if arr[x][0] in list(emojis.keys()):
        arr[x][0] = emojis[arr[x][0]]
      arr[x]= "(" + sch_f_arr(arr[x]) + ")"
  return " ".join(arr)

def setup(str):
  str = str.replace('\r', ' ')
  str = str.replace('\n', ' ')
  str = "(begin " + str + ")"
  return str

if len(sys.argv) != 2:
  print("Usage: python3 read_file.py <file_path>")
  sys.exit(1)

file_path = sys.argv[1]

str = ""

try:
  with open(file_path, 'r') as file:
    str = file.read()
except FileNotFoundError:
  print(f"File not found: {file_path}")
  sys.exit(1)
except Exception as e:
  print(f"An error occurred: {e}")
  sys.exit(1)

result = sch_f_arr(arr_f_scm(setup(str)))

with open('.'.join(file_path.split(".")[:-1])+".scm", "w") as file:
  file.write(result)
  file.close()
