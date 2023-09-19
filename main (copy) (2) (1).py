 #1.2 leap yeark

def isleapyear (year):
  if (year % 4 == 0 and year % 100 !=0)      or year % 400 == 0:
    return True
  else:
    return False
year = int(input("enter a year :"))
           
if isleapyear (year):
  print('{}  is a leap ye