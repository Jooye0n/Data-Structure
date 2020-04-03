def gcd(m, n):
    while n:
        m, n = n, m%n
    return m


class Fraction:
    """Fractional numbers and their relevant operations"""
    def __init__(self, num, denom):
        self._num = num
        self._denom = denom
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self._num)+"/"+str(self._denom)
    
    def __add__(self, other):
        new_num = self._num * other._denom + self._denom * other._num
        new_denom = self._denom * other._denom
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
    
    # Add more arithmetic operators here such as -, *, /.
    def __sub__(self, other):
        new_num = (self._num * other._denom) - (other._num * self._denom)
        new_denom = self._denom * other._denom
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
    
    def __mul__(self, other):
        new_num = self._num * other._num
        new_denom = self._denom * other._denom
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
    
    def __truediv__(self, other):
        new_num = self._num * other._denom
        new_denom = self._denom * other._num
        common = gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
    
    def __eq__(self, other):
        return (self._num * other._denom) == (other._num * self._denom)
    
    # Add more comparison operators here such as !=, <, <=, >, >=.
    
    def __ne__(self, other):
        return (self._num * other._denom) != (other._num * self._denom)
    
    def __gt__(self, other):
        return (self._num * self._denom) > (other._num * other._denom)
    
    def __ge__(self, other):
        return (self._num * self._denom) >= (other._num * other._denom)
    
    def __lt__(self, other):
        return (self._num * self._denom) < (other._num * other._denom)
    
    def __le__(self, other):
        return (self._num * self._denom) <= (other._num * other._denom)



if __name__ == "__main__":
    # You can test your implementation here as followings
    
    my_fraction = Fraction(3,5)
    print(f"Fraction(3,5) will be represented as {my_fraction}.")
    print(f"I ate {my_fraction} of the pizza.")
    
    f1 = Fraction(3,4)
    f2 = Fraction(1,2)
    print(f"{f1} + {f2} = {f1+f2}")
    print(f"{f1} - {f2} = {f1-f2}")
    print(f"{f1} * {f2} = {f1*f2}")
    print(f"{f1} / {f2} = {f1/f2}")
    
    print(f">{f1>f2}")
    print(f">={f1>=f2}")
    print(f"<{f1<f2}")
    print(f"<={f1<=f2}")
    
    f1 = Fraction(1,2)
    f2 = f1
    print(f"Is f1 identical to f2? {f1 is f2}")
    print(f"Is f1 equal to f2? {f1 == f2}")
    
    f2 = Fraction(1,2)
    print(f"Is f1 identical to f2? {f1 is f2}")
    print(f"Is f1 equal to f2? {f1 == f2}")

# Test codes for various operators of fraction numbers

