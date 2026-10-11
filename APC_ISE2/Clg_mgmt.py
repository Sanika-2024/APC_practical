import os


if not os.path.exists("College"):
    os.mkdir("College")


if not os.path.exists("College/records"):
    os.mkdir("College/records")


try:
    f = open("College/records/student.txt", "a")

    n = int(input("Enter number of students: "))

    for i in range(n):
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        branch = input("Enter branch: ")
        marks = input("Enter marks: ")

        f.write(roll + "," + name + "," + branch + "," + marks + "\n")

    f.close()

    
    search = input("Enter roll number to search: ")

    f = open("College/records/student.txt", "r")
    found = False

    for line in f:
        data = line.strip().split(",")

        if data[0] == search:
            print("\nStudent Found")
            print("Roll Number:", data[0])
            print("Name:", data[1])
            print("Branch:", data[2])
            print("Marks:", data[3])
            found = True
            break

    f.close()

    if not found:
        print("Student Not Found")

except ValueError:
    print("Please enter a valid number")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)
