def rem(l, word):
    u = []
    for item in l:
        if not(item == word):
            u.append(item.strip(word))
    return u
l = ["amjsd", "megha", "M"]

word = str(input("Enter the word : "))

print(f"{word} is removed and strip : {rem(l,word)}")