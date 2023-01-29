parts = input("Numbers seperated by space :")
my_list = list(map(int,parts.strip().split()))
filepath_write = "inputlist-output.txt"
print("Current list:")
print(my_list)
print("Length of the list: " + str(len(my_list)))
print("The list, sorted below:")
my_ordered_list = my_list.sort()
for i in my_list:
    print(i)
with open(filepath_write, "w") as file_write:
    for i in my_list:
        file_write.write(str(i) + "\n")

print("file written into inputlist-output.txt")





