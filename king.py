class abu:
    
    def __init__(self, name: str, marks: int, phone: int):
        self.name = name
        self.marks = marks
        self.phone =phone
        

    # 2. Method: Handles the string formatting and returns the sentence
    def get_details(self) -> str:
        return "The name of the student is {}, his marks are {} and phone number is {}".format(
            self.name, self.marks, self.phone
        )

name_input = input("Enter name: ")
marks_input = int(input("Enter marks: "))
phone_input = int(input("Enter phone number: "))


student = abu(name_input, marks_input, phone_input)


print(student.get_details())