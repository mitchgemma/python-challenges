# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utçm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# Not done 

def reverse():
    string = input("enter a word or phrase to reverse:")
    reversed_string = ''
    i = len(string) - 1
    # print(i)
    while i >= 0 :
        reversed_string += string[i]
        i = i - 1
    print(reversed_string)
reverse()