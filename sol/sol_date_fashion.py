def date_fashion(you, date):
  result =0
  if you >= 8 or date >= 8:
    result = 2
  
  if you <= 2 or date <= 2:
    result = 0
    
  if you > 2 and you < 8 and date >2 and date <8:
    result = 1
  return result
