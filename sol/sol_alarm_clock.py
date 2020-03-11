def alarm_clock(day, vacation):
  if vacation:
    if day > 0 and day < 6:
      return "10:00"
    elif day == 6 or day == 0:
      return "off"
  else:
    if day > 0 and day < 6:
      return "7:00"
    elif day == 6 or day == 0:
      return "10:00"

