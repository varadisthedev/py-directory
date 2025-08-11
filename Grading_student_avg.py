# 5. Student Grade Processing
# You are given a list of students and their marks in three subjects.
# python
# CopyEdit
# students = [
# {"name": "Alice", "marks": [85, 78, 92]},
# {"name": "Bob", "marks": [70, 60, 75]},
# {"name": "Charlie", "marks": [90, 88, 95]}
# ]
# (a) Write a function to calculate the average marks of each student.
# (b) Based on average, assign grades: A (≥90), B (80–89), C (70–79), D (<70).
# (c) Return a new list with each student's name, average, and grade.

students = [
{"name": "Alice", "marks": [85, 78, 92]},
{"name": "Bob", "marks": [70, 60, 75]},
{"name": "Charlie", "marks": [90, 88, 95]}
]

def assign(x):  
# use of match and case
    match x:
        case _ if x>=90:
            return "A"
        case _ if 80<=x<=89:
            return "B"
        case _ if  70<=x<=79:
            return "C"
        case _ if x<=70:
            return "D"
def marks():
    for y in students:
        print(f" avg marks of student {y['name']} is: {assign(sum(y['marks'])/3)}")   

def final(data): 
    result = []
    for student in data:
        grade = assign(sum(student['marks'])/3)
        avg = sum(student['marks'])/3
        result.append({
            "name": student["name"],
            "average": avg,
            "grade": grade
        })
    return result


marks()
print(final(students))

