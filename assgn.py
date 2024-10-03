class Student:
    def __init__(self, name, registration_number, age, course):
        self.name = name
        self.registration_number = registration_number
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Registration Number: {self.registration_number}")
        print(f"Age: {self.age}")
        print(f"Course : {self.course}")
        
student1 = Student("Laker Jessy", "S23B13/029", 20, "Information Technology")
student2 = Student("Oliver Mugisa", "S23B13/889", 22, "Computer Science")
student3 = Student("Peter Oppong", "S23B13/082", 21, "Electrical Engineering")
student4 = Student("Nancy Eze", "S23B13/009", 20, "Data Science")


student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()