# ask user for sentence or name and let them know if it's a palindrome

# ask user for input string
phrase_entered = input("Enter a phrase and let's check if it's a palindrome: ")
#remove all special characters and spaces from phrase

# function that reverses original string and returns that reverse
def reverse_phrase(phrase_entered):
    return phrase_entered[::-1]

# defines phrase backwards using the reverse_phrase function
phrase_backwards = reverse_phrase(phrase_entered)
# print(phrase_backwards) <----this was testing if it worked

palindrome = True
# compare string to reverse of string, make function to do it?
def palindrome(phrase_entered, phrase_backwards):
    if phrase_backwards == phrase_entered:
        palindrome = True
        print("This here is a palindrome: ", phrase_entered, phrase_backwards)
    else:
        palindrome = False
        print("This here is not a palindrome: ", phrase_entered, phrase_backwards)

palindrome(phrase_entered, phrase_backwards)

# palindrome = True
# def palindrome():

# def palindrome_check(phrase_entered):

# return value of True or False

# print response that confirms palindrome or not "is a palindrome" or "is not a palindrome"
