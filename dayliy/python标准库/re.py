import re
pattern = "this"
text = 'Does this text match the pattern'
match = re.search(pattern,text)
s = match.start()
e = match.end()
print(f"Found \"{match.re.pattern}\" in \"{match.string}\" from \"{s}\" to \"{e}\" ({text[s:e]})")