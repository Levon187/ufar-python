from Student import Student


student1 = Student(first_name='Armen', last_name='Poghosyan', gpa=75, faculty='Law', course=2)
student2 = Student(first_name='Anna', last_name='Mamikonyan', gpa=80, faculty='IT', course=1)

student1.gpa = 90
print(student1.gpa)
print(student2.first_name.__sizeof__())


my_list = [5, 6, 12.13121]
print(my_list.__sizeof__())

