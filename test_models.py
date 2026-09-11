from models import Student, HonoursStudent

student1 = Student("Lisa", "S1", 72)
student2 = HonoursStudent("John", "S2", 85, "Artificial Intelligence")

print(student1)
print(student2)

print("School:", Student.school_name)
print("Total Students:", Student.total_students)

print(student1.has_passed())
print(student2.has_passed())