""" Question - Count the number of vowels and consonants """

Phrase = input("Enter a phrase: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']

vowel = []
consonant = []

for letter in Phrase:
    if letter in vowels:
        if letter in vowel:
            continue
        else:
            vowel.append(letter)
    elif letter == " ":
        continue
    else:
        if letter in consonant:
            continue
        else:
            consonant.append(letter)

print("Vowels are:",vowel,"Number of vowels:",len(vowel))
print("Consonants are:",consonant,"Number of consonants:",len(consonant))