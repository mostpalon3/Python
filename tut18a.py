# Take a input of the number and if the number is bigger than hundred print you have succesfully entered a number bigger than hundred

i = 100

while True:
    k = int(input("Try to enter a number greater than 100:\n"))
    if k < 100:
        print("Naah! You have entered a smaller number.TRY AGAIN!\n")
        continue
    elif k == 100:
        print("You have entered the number 100 itself try a number greater than it\n")
        continue
    else:
        print("Kudos!You have sucessfully entered a number greater than 100\n")
        break