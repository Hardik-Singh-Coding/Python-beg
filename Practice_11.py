""" Given a string, return True if the string is a palindrome, and False otherwise.
A palindrome is a word that reads the same forward and backward.
Ignore casing (upper/lowercase), but do not ignore spaces or punctuation. """

def is_palindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]
        

string1 = "Racecar"
print(is_palindrome(string1))