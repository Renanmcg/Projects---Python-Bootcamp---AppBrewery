with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(number) for number in list1 if number in list2]

print(result)


