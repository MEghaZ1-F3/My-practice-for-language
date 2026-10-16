def generate_Table(n):

    Table = ""

    for k in range(1,11):
        Table += f"{n} * {k} : {n* k}\n"

    with open(f"Tables/Table_{n}.txt", "w") as g:
        g.write(Table)



for k in range(2,21):
    generate_Table(k)