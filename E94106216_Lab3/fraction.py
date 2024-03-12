from math import gcd

class Fraction(object):
    def __init__(self, Numerator:int, Denominator:int):
        self.num = Numerator
        self.den = Denominator

    def __add__(self, other): # +
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self,other): # -
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self,other): # *
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self,other): # /
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self,other): # ==
        return self.num * other.den == self.den * other.num

    def __ne__(self,other): # !=
        return self.num * other.den != self.den * other.num

    def __repr__(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
        return "Numerator:{0}\nDenominator:{1}".format(self.num, self.den)

    def __str__(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
        return "{0}/{1}".format(self.num, self.den)