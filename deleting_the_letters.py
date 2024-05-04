# Someone forbade the letters
word = input() + " forbade the letter"   # Creating a phrase that will be checking
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]   # Input the alphabet list (it would be created with an ACSII chars of list comprehence)
for i in abc:   # Starting a loop to compare the phrase and the alphabet letters
    if i in word:   # If some letters are found in phrase, 
        print(word, i)   # Output the phrase and each letter on a new string,
        word = word.replace(i, '').replace('  ', ' ').strip()   # And the letter is overwriting to empty string, and deleting extra spaces in string and starting new iteration