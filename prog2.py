# Input a word or sentences
string = input("Please enter your own string: ")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2
print("\nThe original string = ", string)
print("\nThe Reversed string = ", string2)