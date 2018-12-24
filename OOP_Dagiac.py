
class Dagiac:
    def __init__(self, socanh):
        self.n = socanh
        self.canh = []
        for i in range(self.n):
            self.canh.append(0)

    def nhapcanh(self):
        for i in range(self.n):
            self.canh[i] = float(input("Ban hay nhap gia tri canh " + str(i + 1) + " : "))

    def hienthicanh(self):
        for i in range(self.n):
            print("Gia tri canh ", i + 1, " la ", self.canh[i])


class Tamgiac(Dagiac):
    def __init__(self):
        Dagiac.__init__(self, 3)

    def dientich(self):
        a, b, c = self.canh
        cv = float((a + b + c) / 2)
        print('Chu vi %f' % cv)
        s = (cv * (cv - a) * (cv - b) * (cv - c)) ** 0.5
        print('Dien tich tam giac co canh ' + str(a) + ', ' + str(b) + ', ' + str(c) + ' la: ' + str(s))


s = Tamgiac()
s.nhapcanh()
s.hienthicanh()
s.dientich()
