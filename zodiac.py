a="yes"
while a=="yes":
    y=int(input("Enter your birth year:"))
    if y > 2026 or y < 1900:
        print("It is not correct!!!Please write right year you have born in!")
        continue
    z=y%12
    if z == 0:
        print("Your Chinese Zodiac sign is:Monkey" )
    elif z == 1:
        print("Your Chinese Zodiac sign is:Rooster")
    elif z == 2:
        print("Your Chinese Zodiac sign is:Dog")
    elif z == 3:
        print("Your Chinese Zodiac sign is:Pig")
    elif z == 4:
        print("Your Chinese Zodiac sign is:Rat")
    elif z == 5:
        print("Your Chinese Zodiac sign is:Ox")
    elif z == 6:
        print("Your Chinese Zodiac sign is:Tiger")
    elif z == 7:
        print("Your Chinese Zodiac sign is:Rabbit")
    elif z == 8:
        print("Your Chinese Zodiac sign is:Dragon")
    elif z == 9:
        print("Your Chinese Zodiac sign is:Snake")
    elif z == 10:
        print("Your Chinese Zodiac sign is:Horse")
    else:
        print("Your Chinese Zodiac sign is:Sheep")
    a= input("Do you wanna try again?(yes/no): ")

