p1 = "Make a lot of mmoney"
p2 = "buy this"
p3 = "suscribe this"
p4 = "click this"

message = input("Enter your message: ")
if ( p1 in message or p2 in message or p3 in message or p4 in message):
    print("Spam message")
else:
    print("Not spam")