def left2(str):
  if(len(str) == 2):
    return str
  else:
    temp = str[:2]
    return str[2:] + temp
