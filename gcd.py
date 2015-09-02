""" Greatest common divisor

gcd(a,0) = a  ("This is a definition")
gcd(a,b) = gcd(b,a mod b)
Modulus = the remainder after integer division  """

#  recursive solution
def gcd(a, b):
        if a % b == 0:   # If the remainder 0, it worked, we need b
            return b
        else:
            return gcd(b, a % b)  # Else try again

print(gcd(123456,654321))
