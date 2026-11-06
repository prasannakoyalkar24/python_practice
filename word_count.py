# counting words in a sentence
sentence = input("Enter a sentence:")
count = 0
words = sentence.split()
for i in words:
    count += 1

print(f"No of words in the sentence are: {count}")