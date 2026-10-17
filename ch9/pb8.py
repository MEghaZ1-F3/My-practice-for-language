with open("this.txt") as j:
    ui = j.read()

with open("this_copy.txt","w") as u:
          u.write(ui)