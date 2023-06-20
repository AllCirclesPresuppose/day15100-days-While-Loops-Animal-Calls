print("While Loops! Animal Calls!")
print()
print()
exit = ""
while exit != "yes":
    animal = input("What animal do you want to hear? ")
    if animal == "cow":
        print("a cow goes moo!")
    elif animal == "monkey":
        print("a monkey goes ooh ooh aah aah!")
    elif animal == "cat":
        print("A cat says meow!")
    elif animal == "dog":
        print("A dog says woof!")
    elif animal == "horse":
        print("A horse says neigh!")
    else:
        print(
            "the " + animal +
            " says... I dunno, man, something, i'm sure. bzzrt awooga? sure. "
            + animal + " says bzzrt awooga.")
    exit = input("exit game? (yes/no)")
