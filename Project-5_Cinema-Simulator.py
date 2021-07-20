films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan":[12,5],
    "Ghost Busters":[12,5]
    }

while True:
    print("What film do you want to watch today?")
    choice = input("-->").strip().title()

    if choice in films:
        print("Nice choice!")
        print("How old are you?")
        age = int(input("-->").strip())

        if age >= films[choice][0]:

            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("We are out of seats.")
                
        else:
            print("You are too young to see that film.")
        
    else:
        print("{} isn't available today!".format(choice))
