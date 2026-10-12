a="yes"
while a=="yes":
    day = 0
    print("Is your birthday in set1?")
    print(" 1  3  5  7\n 9 11 13 15\n17 19 21 23\n25 27 29 31")
    answer = int(input("Enter 0 for no and 1 for yes:"))
    if answer == 1 :
        day +=1
    print("\nIs your birthday in Set2?")
    print(" 2  3  6  7\n10 11 14 15\n18 19 22 23\n26 27 30 31")
    answer = int(input("Enter 0 for no and 1 for yes:"))
    if answer == 1 :
        day +=2
    print("\nIs your birthday in Set3?")
    print(" 4  5  6  7\n12 13 14 15\n20 21 22 23\n28 29 30 31")
    answer = int(input("Enter 0 for no and 1 for yes:"))
    if answer == 1 :
        day +=4
    print("\nIs your birthday in Set4?")
    print(" 8  9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31")
    answer = int(input("Enter 0 for No and 1 for Yes:"))
    if answer == 1:
        day += 8
    print("\nIs your birthday in Set5?")
    print("16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31")
    answer = int(input("Enter 0 for No and 1 for Yes: "))
    if answer == 1:
        day += 16
    print("your birthday is:" , day)
    a= input("Do you wanna try again?(yes/no): ")

    
