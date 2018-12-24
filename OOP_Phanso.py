# OOP-Phanso

class Phanso:
    def __init__(self, tuso=0, mauso=1):
        self.tu = tuso
        self.mau = mauso

    def nhapphanso(self):
        self.tu = int(input('Nhap tu so: '))
        self.mau = int(input('Nhap mau so: '))

    def printphanso(self):
        if self.mau != 0:
            print("Phan so:" + str(self.tu) + "/" + str(self.mau))
        else:
            print("Phan so khong hop le!")

    def rutgon(self):
        max = 1
        if self.tu < self.mau:
            fmin = self.tu
        else:
            fmin = self.mau
        for i in range(1, fmin + 1):
            if self.tu % i == 0 and self.mau % i == 0:
                max = i
        self.tu = self.tu // max
        self.mau = self.mau // max

    def cong(self, a):
        tu = self.tu * a.mau + a.tu * self.mau
        mau = self.mau * a.mau
        return Phanso(tu, mau)

    def tru(self, a):
        self.tu = self.tu * a.mau - a.tu * self.mau
        self.mau = self.mau * a.mau


p1 = Phanso(6)
p1.printphanso()
p1.nhapphanso()
p1.rutgon()
p1.printphanso()
p2 = Phanso(5, 4)
p2.rutgon()

p3 = p1.cong(p2)
p3.rutgon()
p3.printphanso()

p1.tru(p2)
p1.rutgon()
p1.printphanso()
