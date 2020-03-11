def common_end(a, b):
  lastIndexA = len(a) -1
  lastIndexB = len(b) -1
  if a[0] == b[0] or a[lastIndexA] == b[lastIndexB]:
    return True
  else:
    return False
