courses = [
    "History I",
    "Physics I",
    "Calculus I",
    "Biology I",
    "Introduction to Programming",
    "Chemistry I",
    "Psychology I",
    "Microeconomics",
    "Linear Algebra",
    "English Composition I",
    "Introduction to Philosophy",
    "Macroeconomics",
    "Calculus II",
    "Discrete Mathematics",
    "Data Structures and Algorithms"
]
print(courses)
print(sorted(courses))
print(sorted(courses, reverse=True))
courses.reverse()
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
courses_tuple = [
(1, "Introduction to programming"),
(2, "Calculus I"),
(3, "Data Structures and Algorithms"),
(4, "Linear Algebra"),
(5, "Physics I"),
(6, "Chemisrty I"),
(7, "Biology I"),
(8, "Microeconomics"),
(9, "Macroeconomics"),
(10, "Psychology I"),
(11, "History I"),
(12, "English Composition I"),
(13, "Introduction to Philosophy"),
(14, "Calculus II"),
(15, "Discrete Mathematics")
]
new_list = []
for course in courses_tuple:
    course_name = course[1]
    new_list.append(course_name)
print(new_list)
departments = [
    (1, "Computer Science"),
    (2, "Mathematics"),
    (3, "Computer science"),
    (4, "Mathematics"),
    (5, "Physics"),
    (6, "Chemistry"),
    (7, "Biology"),
    (8, "Economics"),
    (9, "Economics"),
    (10, "Psychology"),
    (11, "History"),
    (12, "English"),
    (13, "Philosophy"),
    (14, "Mathematics"),
    (15, "Computer Science")
]
while True: 
    user_input = input("Enter course ID (1-15)  or quit or 0: ")
    if user_input == "quit":
        print("The value quit has been used to exit.")
        break
    if user_input =="0":
        print("Course ID is out of range (1-15), try again.")
        continue
    course_id =int(user_input)
    found = False
    for course in departments:
         if course[0] == course_id:
                print(
                    "Course ID",
                    course_id,
                    "is in the",
                    course[1],
                    "department."
                )
                found = True
                break
    if not found:
                print("Course ID not found.")
                