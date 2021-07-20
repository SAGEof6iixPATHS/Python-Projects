known_users = ["Alice","Bob","Clair","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My name is Travis.")
    print("What is your name?")
    name = input("-->").strip().capitalize()
    print("Thank you {}!".format(name))

    if name in known_users:
        print("Hello {}!".format(name))
        print("Would you like to be removed from our system (y/n)?")
        remove = input("-->").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Okay!")
        else:
            print("I beg your pardon!")
    else:
        print("Hello {}! I don't think that I have met you before.".format(name))
        print("Would you like to be added in our system (y/n)?")
        add = input("-->").strip().lower()

        if add == "y":
            known_users.append(name)
        elif add == "n":
            print("Okay!")
        else:
            print("I beg your pardon!")
