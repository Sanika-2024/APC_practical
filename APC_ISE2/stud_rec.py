


f = open("student.txt", "a")

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    f.write(roll + "," + name + "," + marks + "\n")

f.close()

search = input("Enter roll number to search: ")

f = open("student.txt", "r")
found = False

for line in f:
    data = line.strip().split(",")

    if data[0] == search:
        print("Student Found")
        print("Roll Number:", data[0])
        print("Name:", data[1])
        print("Marks:", data[2])
        found = True
        break

if not found:
    print("Student Not Found")

f.close()
