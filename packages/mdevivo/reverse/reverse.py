def reverse(args):
  inputs = args.get("input", "")
  out = "Please provide an input"
  if inputs != "":
    out = inputs[::-1]
  return { "output": out }
