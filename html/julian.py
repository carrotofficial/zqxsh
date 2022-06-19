date: str = input("> ")
def check_validity(s):
  if len(s) == 10 and s[4] == "-" and s[7] == "-":
    return True
  else:
    return False

MONTHS: list = [None, "Ianuarius", "Februarius", "Martius", "Aprilis", "Maius", "Iunius", "Iulius", "Augustus", "September", "October", "November", "December"]

if check_validity(date) == True:
  if int(date[8:]) >= 15:
    print("{} days past the Ides of {}, Year {}"
    .format(
      int(date[8:]) - 15, # day
      MONTHS[int(date[5:7])], # month
      int(date[0:4]) + 753)) # year
  else:
    print("{} days past the Kalends of {}, Year {}"
    .format(
      int(date[8:]) - 1, # day
      MONTHS[int(date[5:7])], # month
      int(date[0:4]) + 753)) # year