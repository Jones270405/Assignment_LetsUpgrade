# Print highest score in descending order
def top_students(n):
    sorted_list = sorted(students, key=lambda x: x[1], reverse=True)
    return sorted_list[:n]

# Print the average score of all students      
def average_score(students):
    total=0
    for i in students:
        total+=i[1]
    return total/len(students)

# List of students with name and score
students = [
    ("Riya", 85),
    ("Aman", 72),
    ("Neha", 48),
    ("Vikram", 95),
    ("Sara", 67),
    ("Karan", 43),
    ("Pooja", 88),
    ("Ramesh", 59),
    ("Tina", 49),
    ("Ali", 78)
]

# Calling function top_students(students)
print(top_students(3))
# Calling function average_score(stduents)
print(average_score(students))

# Created a file - remedial.txt and wrote names of students with score below 50
with open("remedial.txt", "w") as f:
    for i in students:
        if i[1]<50:
            f.write(i[0]+"\n")



