from math import gcd

class Fraction(object):
    def __init__(self, Numerator:int, Denominator:int):
        self.num = Numerator
        self.den = Denominator

    def __add__(self, other): # +
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self,other): # -
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self,other): # *
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self,other): # /
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self,other): # ==
        return self.num * other.den == self.den * other.num

    def __ne__(self,other): # !=
        return self.num * other.den != self.den * other.num

    def __repr__(self):
        return "Numerator:{0}\nDenominator:{1}".format(self.num, self.den)

    def __str__(self):
        return "{0}/{1}".format(self.num, self.den)