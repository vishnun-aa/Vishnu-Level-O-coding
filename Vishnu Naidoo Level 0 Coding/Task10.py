User_input1=input("Enter first word: ")
User_input2=input("Enter second  word: ")

string0 = set(User_input1)
string1 = set(User_input2)

a=list(string0 & string1)

print("Common letters are :",a)

