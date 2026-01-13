import cmath  # Importing cmath to handle complex numbers
def find_roots(a, b, c):
    # Calculating the discriminant
    discriminant = b**2 - 4*a*c

    # Calculating two roots using the quadratic formula
    r1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    r2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return r1, r2

def main():
    print("Quadratic Equation: ax^2 + bx + c = 0")
    
    # Input coefficients a, b, and c
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return
    # Find the roots
    root1, root2 = find_roots(a, b, c)
    print(f"The roots of the equation are: {root1} and {root2}")
main()
