#Good Morning
import time
hour = int(time.strftime('%H'))
print(hour)
if hour>0 and hour<12 :
    print("Good Morning Sarnendu")
elif hour<12 and hour>5:
    print("Good Evening Sarnendu")
else:
    print("Good Night Sarnendu")
