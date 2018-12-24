# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

class Tugiac:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def printInfo(self):
        print(
            'Hinh tu giac, cac canh la: ' + str(self.a) + ', ' + str(self.b) + ', ' + str(self.c) + ', ' + str(self.d))


class Hinhvuong(Tugiac):
    def __init__(self, a):
        Tugiac.__init__(self, a, a, a, a)

    def dientich(self):
        return self.a * self.a


class Chunhat(Tugiac):
    def __init__(self, a, b):
        Tugiac.__init__(self, a, b, a, b)

    def dientich(self):
        s = self.a * self.b
        return s


da = Tugiac(1, 2, 3, 4)
da.printInfo()
hv = Hinhvuong(5)
print('Dien tich hinh vuong: ', hv.dientich())
hcn = Chunhat(2, 3)
print('Dien tich hinh chu nhat ', hcn.dientich())
