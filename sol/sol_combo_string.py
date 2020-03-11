def combo_string(a, b):
  len_a = len(a)
  len_b = len(b)
  short = ""
  long = ""
  if len_a < len_b:
    short = a
    long = b
  else:
    short = b
    long = a
    
  return short+long+short
