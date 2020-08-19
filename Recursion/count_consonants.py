# Given a string, count the number of consonants
# Note a consonant is a letter that is not vowel
# i.e a letter that is not a, e, i, o, or u.

input_str_1 = "abc de"
input_str_2 = "LucIdPrOgRAmmiNg"

vowels = "aeiou"

def iterative_count_consonants(input_str):
    counter = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            counter += 1
    
    return counter

def recursive_count_consonants(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    
    return recursive_count_consonants(input_str[1:])

print(recursive_count_consonants(input_str_2))


