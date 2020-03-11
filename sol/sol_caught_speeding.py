def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      result = 0
    elif speed >=61 and speed <= 80:
      result =1
    elif speed >= 81:
      result =2
  elif is_birthday:
    if speed <= 65:
      result = 0
    elif speed >=66 and speed <= 85:
      result =1
    elif speed >= 86:
      result =2
  return result

