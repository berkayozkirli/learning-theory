from __future__ import annotations
import math

class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        self.re = real
        self.im = imaginary

    @property
    def magnitude(self):
        return math.hypot(self.re, self.im)

    @property
    def angle(self):
        return math.atan2(self.im, self.re)

    def to_polar(self) -> tuple[float, float]:
        return (self.magnitude, self.angle)

    @staticmethod
    def from_polar(magnitude: float, angle: float) -> ComplexNumber:
        return ComplexNumber(magnitude * math.cos(angle),
                            magnitude * math.sin(angle))

    def conjugate(self):
        return ComplexNumber(self.re, -self.im)

    def __repr__(self):
        return f"ComplexNumber({self.re}, {self.im})"

    def __str__(self):
        sign = '+' if self.im >= 0 else '-'
        return f"{self.re} {sign} {abs(self.im)}i"


    def __add__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        if isinstance(other, (int, float)):
            return ComplexNumber(self.re + other, self.im)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re + other.re, self.im + other.im)
        return NotImplemented
    def __radd__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        return self.__add__(other)
    
    def __sub__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        if isinstance(other, (int, float)):
            return ComplexNumber(self.re - other, self.im)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re - other.re, self.im - other.im)
        return NotImplemented
    def __rsub__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        if isinstance(other, (int, float)):
            return ComplexNumber(other - self.re, -self.im)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(other.re - self.re, other.im - self.im)
        return NotImplemented

    def __mul__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        if isinstance(other, (int, float)):
            return ComplexNumber(self.re * other, self.im * other)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re * other.re - self.im * other.im,
                                 self.re * other.im + self.im * other.re)
        return NotImplemented
    def __rmul__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        return self.__mul__(other)
    
    def __truediv__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return ComplexNumber(self.re / other, self.im / other)
        if isinstance(other, ComplexNumber):
            denom = other.re ** 2 + other.im ** 2
            if denom == 0:
                raise ZeroDivisionError("division by zero")
            return ComplexNumber((self.re * other.re + self.im * other.im) / denom,
                                (self.im * other.re - self.re * other.im) / denom)
        return NotImplemented
    def __rtruediv__(self, other: int | float | ComplexNumber) -> ComplexNumber:
        if isinstance(other, (int, float)):
            denom = self.re ** 2 + self.im ** 2
            if denom == 0:
                raise ZeroDivisionError("division by zero")
            return ComplexNumber((other * self.re) / denom, (-other * self.im) / denom)
        if isinstance(other, ComplexNumber):
            denom = self.re ** 2 + self.im ** 2
            if denom == 0:
                raise ZeroDivisionError("division by zero")
            return ComplexNumber((other.re * self.re + other.im * self.im) / denom,
                                (other.im * self.re - other.re * self.im) / denom)
        return NotImplemented

    def __abs__(self):
        return self.magnitude
    def __neg__(self):
        return ComplexNumber(-self.re, -self.im)
    def __eq__(self, other: ComplexNumber) -> bool:
        if not isinstance(other, ComplexNumber):
            return False
        return self.re == other.re and self.im == other.im
    def __ne__(self, other: ComplexNumber) -> bool:
        if not isinstance(other, ComplexNumber):
            return False
        return not self.__eq__(other)