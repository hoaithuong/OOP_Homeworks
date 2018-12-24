# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# OOP-Kethua
# Xay dung lop Connguoi chua Ten, tuoi, gioi tinh, ngay sinh
# Lop sinh vien co masv, lop
# Lop giao vien co magv, trinh do


class Person:
    def __init__(self, name, age, birth, sex):
        self.name = name
        self.age = age
        self.birth = birth
        self.sex = sex

    def printInfo(self):
        print(self.name + ': ' + str(self.age) + ', ' + self.sex + ', ' + self.birth)


class Student(Person):
    def __init__(self, name, age, birth, sex, masv, lop):
        Person.__init__(self, name, age, birth, sex)
        self.masv = masv
        self.lop = lop

    def printInfo(self):
        print(self.name + ': ' + str(self.age) + ', ' + self.sex + ', ' + self.birth + ', ' + self.masv + ', ' + self.lop)


class Teacher(Person):
    def __init__(self, name, age, birth, sex, magv, trinhdo):
        Person.__init__(self, name, age, birth, sex)
        self.magv = magv
        self.trinhdo = trinhdo

    def printInfo(self):
        print(self.name + ': ' + str(self.age) + ', ' + self.sex + ', ' + self.birth + ', ' + self.magv + ', ' + self.trinhdo)


# p1 = Person('Hoang thui', '25', '7/9/1993', 'Male')
# p1.printperson()
s1 = Student('Hoang thui', '25', '7/9/1993', 'Male', '1234', '12')
s1.printInfo()
s2 = Teacher('Kaka', '50', '1/1/1974', 'Female', 'GV12', 'Giaosu')
s2.printInfo()
