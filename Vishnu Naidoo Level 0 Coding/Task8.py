number = int(input("Enter digit here:"))

hours = number//3680
hours1=number%3680
minute=hours1//60
seconds=hours1%60

print(hours,"hour", minute,'minutes',seconds,'second')


