

file = open("sample.txt", "r")

content = file.read()


print("File Content:\n")
print(content)


words = content.split()
word_count = len(words)

print("\nNumber of words in file:", word_count)


file.close()