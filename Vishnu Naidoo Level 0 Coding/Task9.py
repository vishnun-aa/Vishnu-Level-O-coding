word = input("enter the specific word:")

string0 = word.lower()
print(string0)

countvowel = 0 
list1 = ('a','e','i,','o','u')
for char in string0:
    if char in list1:
        countvowel=countvowel+1

print('number of vowles in given words is:',countvowel)


