# we have to form a list with some random strings and number and then first detect the number and then print the number which is greater than 6

i = ["tree", 5, "Icon", "potter", "blade runner", 2049, 8, 6, 3, 0.2, 4, 99, str, int]

for item in i:
    if str(item).isnumeric() and item >= 6:
        print(item)
        