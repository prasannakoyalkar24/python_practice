# checking whether two words are anagrams or not
word1 = input("Enter a word:")
word2 = input("Enter second word: ")
if sorted(word1.lower().replace(" ","")) == sorted(word2.lower().replace(" ","")):
    print("Anagrams")
else:
    print("not anagrams")