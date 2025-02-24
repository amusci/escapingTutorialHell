'''

A tetrahedron is a pyramid with a triangular base and three sides. A tetrahedral number is a number of items within a tetrahedron.

Create a function that takes an integer n and returns the nth tetrahedral number.

'''

def tetra(n):
    return (round(n * (n + 1) * (n + 2) / 6, 0))

if __name__ == "__main__":
    print(
tetra(6))