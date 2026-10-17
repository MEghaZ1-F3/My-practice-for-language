words = ["Donke","bad","dad"]


with open("Donke.txt","r") as t:
    con = t.read()

for word in words:
    con = con.replace(word, "#" *len(word))

with open("Donke.txt","w") as t:
    t.write(con)