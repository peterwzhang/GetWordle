from words import *
from datetime import date, timedelta

# flair is the 304th wordle/index 303
start = date(2021, 6, 18)
cur = date.today()
diff = (cur - start).days - 1 # python starts at 0 so subtract 1

# TODO: error handling + better description
while (True):
    day_index = input("Which WORDLE would you like to see? or Q to quit: ")
    if day_index == 'Q':
        break
    day_index = int(day_index)
    print("The WORDLE for " + (cur + timedelta(days=day_index)).strftime("%m-%d-%Y") + " is: " + answers[diff + day_index])