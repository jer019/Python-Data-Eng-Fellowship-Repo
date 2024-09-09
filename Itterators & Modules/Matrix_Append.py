#  create a self defined module named as MatrixOperation and have two fucntions over list appending and , deletion.
#  Call this module and perfrom operations over lists. Lists must be provided by the user

class MatrixOperation:
    def __init__(self,list):
        self.list=list

    def append(self,element):
        self.list.append(element)

    def delete(self,element):
        self.list.remove(element)

matrix=MatrixOperation([])

elements=input("Enter elements of matrix: ").split()

for element in elements:
    matrix.append(element)

print(f"Matrix after append: {matrix.list}")

ele=input("Enter an element to remove from matrix: ")
matrix.delete(ele)

print(f"Matrix after removing element {matrix.list}")

