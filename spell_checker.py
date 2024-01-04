from spellchecker import SpellChecker

corrector = SpellChecker()  # Note the correct capitalization
word = input("Enter a word: ")

if word in corrector:
    print("CORRECT")
else:
    correct_word = corrector.correction(word)
    print("Correct spelling is:", correct_word)
