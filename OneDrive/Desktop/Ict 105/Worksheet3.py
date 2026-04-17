# Worksheet 3 - ICT 105
# Session 5 and 6 
print("SESSION 5 - WORKING WITH DICTIONARIES")
print()

course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"],
    1006: ["BIO102", "ENGL101"],
    1007: ["ECON101", "PSY101"],
    1008: ["ECON102", "SOC101"],
    1009: ["PSY102", "SOC102"],
    1010: ["CS101", "MATH101"]
}

print("Student Course Enrollments:")
for student_id, courses in course_enrollments.items():
    print("Student ID:", student_id, "Enrolled Courses:", courses)

print()
departments = {
    "Computer Science": [
        ("Computer Science", "CS101", "Introduction to Computer Science"),
        ("Computer Science", "CS202", "Data Structures and Algorithms")
    ],
    "Mathematics": [
        ("Mathematics", "MATH101", "Calculus I"),
        ("Mathematics", "MATH102", "Calculus II")
    ],
    "Physics": [
        ("Physics", "PHY101", "General Physics I"),
        ("Physics", "PHY102", "General Physics II")
    ],
    "Chemistry": [
        ("Chemistry", "CHEM101", "General Chemistry I"),
        ("Chemistry", "CHEM102", "General Chemistry II")
    ],
    "Biology": [
        ("Biology", "BIO101", "Biology I"),
        ("Biology", "BIO102", "Biology II")
    ]
}

print("Courses by Department:")
for department, courses in departments.items():
    print("Department:", department)
    for course in courses:
        print(course)

print()
lecturer_assignments = {
    "Dr. Emily Brown": ["CS101", "MATH102"],
    "Mr. Michael Johnson": ["CS202", "PHY102"],
    "Prof. David Lee": ["PHY101"],
    "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"],
    "Miss. Sophia Carter": ["CHEM102", "BIO101"],
    "Dr. Lucas Sanchez": ["PSY101", "PSY102"]
}

print("Lecturer Assignments:")
for lecturer, courses in lecturer_assignments.items():
    print("Lecturer:", lecturer, "Courses:", courses)

print()
print("SESSION 6 - USER INPUTS AND WHILE LOOPS")
print()

students = []
active = True

while active:
    student_name = input("Enter student name (or type quit to stop): ")

    if student_name.lower() == "quit":
        active = False
    else:
        students.append(student_name)
        print(student_name, "has been added to the class.")

print("Students entered:", students)
print()
locations = [
    (101, 15, "Ground Floor", "Building A"),
    (102, 15, "Ground Floor", "Building A"),
    (103, 20, "Ground Floor", "Building A"),
    (104, 20, "Ground Floor", "Building A"),
    (105, 25, "Ground Floor", "Building A"),
    (106, 25, "Ground Floor", "Building A"),
    (107, 30, "Ground Floor", "Building A"),
    (108, 30, "Ground Floor", "Building A"),
    (109, 30, "Ground Floor", "Building A"),
    (110, 10, "Ground Floor", "Building A"),
    (201, 10, "1st Floor", "Building A"),
    (202, 10, "1st Floor", "Building A"),
    (203, 25, "1st Floor", "Building A"),
    (204, 25, "1st Floor", "Building A"),
    (205, 30, "1st Floor", "Building A"),
    (206, 40, "1st Floor", "Building A"),
    (207, 40, "1st Floor", "Building A"),
    (208, 40, "1st Floor", "Building A")
]

required_seats = int(input("Enter minimum number of seats needed: "))

for room in locations:
    if room[1] >= required_seats:
        print("Room", room[0], "can support", required_seats, "students.")
        print("Capacity:", room[1], "Floor:", room[2], "Location:", room[3])
        break

print()
students2 = []
active = True
max_cap = 3

while active:
    name = input("Enter a student name (quit / exit / 0 to stop): ")

    if name.lower() in ["quit", "exit", "0"]:
        print("Exit parameter used:", name)
        active = False
    else:
        students2.append(name)
        print(name, "has been added.")

        if len(students2) == max_cap:
            print("Maximum class capacity reached.")
            break

print("Student list:", students2)
print("Total students entered:", len(students2))
print("max_cap value:", max_cap)
print()
line_count = 0

try:
    while True:
        text = input("Type something (CTRL+C to stop): ")
        print(text)
        line_count += 1
except KeyboardInterrupt:
    print()
    print("Infinite loop stopped.")
    print("Total number of lines:", line_count)