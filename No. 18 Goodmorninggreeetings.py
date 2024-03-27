#Good Morning
import time
name=input("Enter Your Name: ")
hour = int(time.strftime('%H'))
print(hour)
if hour>0 and hour<12 :
    print("Good Morning", name)
elif hour<12 and hour>5:
    print("Good Evening", name)
else:
    print("Good Night", name)
