"""
1)Student #
Создайте класс Student, конструктор которого имеет параметры name, lastname,
department, year_of_entrance. Добавьте метод get_student_info, который
возвращает имя, фамилию, год поступления и факультет в
отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
Программирование.”
"""

class Student():
    """ Класс Студент """
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
    
    def get_student_info(self):
        print(f"{self.name.title()} {self.lastname.title()} поступил в {self.year_of_entrance} г. на факультет: {self.department.title()}")


student_1 = Student('николай', 'шматов', 'информационные технологии', 2006)
student_1.get_student_info()       
