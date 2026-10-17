word = "Donkey"

with open("Donke.txt","r") as g:
    content = g.read()


contents = content.replace(word,"####")

with open("Donke.txt", "w") as g:
    g.write(contents)