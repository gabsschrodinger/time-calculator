def add_time(start, duration, day = ""):
  new_time = ""
  days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  if day != "":
    current_day = days.index(day.lower())

  days_later = 0
  day_period = start.split()[1]
  init_hours = start.split()[0].split(":")[0]
  init_minutes = start.split()[0].split(":")[1]

  add_hours = duration.split(":")[0]
  add_minutes = duration.split(":")[1]

  while int(add_minutes) > 0:
    if(60 - int(init_minutes) > int(add_minutes)):
      init_minutes = str(int(init_minutes) + int(add_minutes))
      if len(init_minutes) == 1: init_minutes = "0" + init_minutes
      add_minutes = 0
    else:
      add_minutes = str(int(add_minutes) - 60 + int(init_minutes))
      init_minutes = "00"
      init_hours = str(int(init_hours) + 1)
      if int(init_hours) == 12:
        if day_period == "AM": day_period = "PM"
        else: day_period = "AM"
        if day_period == "AM": days_later += 1
      elif int(init_hours) == 13:
        init_hours = "1"

  for hour in range(int(add_hours)):
    init_hours = str(int(init_hours) + 1)
    if int(init_hours) == 12:
        if day_period == "AM": day_period = "PM"
        else: day_period = "AM"
        if day_period == "AM": days_later += 1
    elif int(init_hours) == 13:
      init_hours = "1"

  new_time = init_hours + ":" + init_minutes + " " + day_period

  if day != "":
    for j in range(days_later):
      current_day += 1
      if current_day == len(days): current_day = 0
    
    new_time += ", " + days[current_day].capitalize()

  if days_later == 1: new_time += " (next day)"
  elif days_later > 1: new_time += " (" + str(days_later) + " days later)"

  return new_time


print(add_time("11:43 PM", "24:20", "tueSday"))