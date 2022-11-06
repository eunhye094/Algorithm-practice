import fractions

def solution(denum1, num1, denum2, num2):
    a = fractions.Fraction(denum1, num1) + fractions.Fraction(denum2, num2)
    return [a.numerator, a.denominator]