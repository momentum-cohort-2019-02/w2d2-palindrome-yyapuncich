# ask user for sentence or name and let them know if it's a palindrome

# ask user for input string
phrase_entered = input("Enter a phrase and let's check if it's a palindrome: ")
#remove all special characters and spaces from phrase
def remove_extra_spaces(phrase_entered):
    """This function removes spaces and special characters from phrase"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += letters.upper()

    phrase_clean = ""
    for char in phrase_entered:
        if char in letters:
            phrase_clean += char
    return phrase_clean

phrase_clean = remove_extra_spaces(phrase_entered)
print(phrase_clean) #checking here
    
# function that reverses original string and returns that reverse
def reverse_phrase(phrase_clean):
    """This function reverses the phrase entered and returns that reversed phrase"""
    return phrase_clean[::-1]

# defines phrase backwards using the reverse_phrase function
phrase_backwards = reverse_phrase(phrase_clean)
# print(phrase_backwards) <----this was testing if it worked

palindrome = True #is this needed or useful?

# compare string to reverse of string, make function to do it?
# print response that confirms palindrome or not "is a palindrome" or "is not a palindrome"
def palindrome(phrase_clean, phrase_backwards):
    """This function let's you know if you've entered a palindrome or not"""
    if phrase_backwards == phrase_clean:
        palindrome = True
        print("This here is a palindrome: ", phrase_clean, phrase_backwards)
    else:
        palindrome = False
        print("This here is not a palindrome: ", phrase_clean, phrase_backwards)

palindrome(phrase_clean, phrase_backwards)

# palindrome = True
# def palindrome():
