with open("old.txt","r") as g:
    con = g.read()

with open("renamed_by_python.txt","w") as g:
    g.write(con)