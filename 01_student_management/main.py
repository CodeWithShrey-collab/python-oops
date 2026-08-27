import json

class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display(self):
        print("---------------------")
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)
        print("Grade",self.get_grade())

    def get_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B"
        elif self.marks>=60:
            return "C"
        else:
            return "D"

    def update_marks(self,marks):
        self.marks=marks

    def to_dict(self):
        return {
            "name":self.name,
            "roll":self.roll,
            "marks":self.marks
        }

def save_students(students):
    data=[]
    for student in students:
        data.append(student.to_dict())
    with open("students.json","w")as file:
        json.dump(data,file,indent=4)

def load_students():

    students=[]

    try:
        with open("students.json","r") as file:
            data=json.load(file)

        for item in data:
            student=Student(
                item["name"],
                item["roll"],
                item["marks"]
            )

            students.append(student)

    except FileNotFoundError:
        pass

    return students

students=load_students()

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Update Marks")
    print("5. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:

        name=input("Enter name:")
        roll=int(input("Enter roll number:"))
        marks=float(input("Enter marks:"))

        student=Student(name,roll,marks)
        students.append(student)
        save_students(students)
        print("Student added successfully")

    elif choice==2:
        if len(students)==0:
            print("No students found")
        else:
            for student in students:
                student.display()

    elif choice==3:

        roll=int(input("Enter roll number:"))
        found=False

        for student in students:
            if student.roll==roll:
                student.display()
                found=True
                break

        if not found:
            print("Student not found")

    elif choice==4:

        roll=int(input("Enter roll number:"))
        found=False

        for student in students:
            if student.roll==roll:
                marks=float(input("Enter new marks:"))
                student.update_marks(marks)
                save_students(students)
                print("Marks Updated")
                found=True
                break
        if not found:
            print("Student not found")

    elif choice==5:
        break

    else:
        print("Invalid choice")