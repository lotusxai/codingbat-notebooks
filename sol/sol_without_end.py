def without_end(str):
  if len(str) == 2:
    return ''
  else:
    str = str[1:]
    l = len(str) -1
    str = str[:l]
    return str

