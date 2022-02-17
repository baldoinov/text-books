
def check_fermat(a, b, c, n):
    if (a**n) + (b**n) == (c**n):
        print(f"{(a**n)} + {(b**n)} = {(c**n)}")
        print("Holy smokes, Fermat was wrong!")
    else:
        print(f"{(a**n)} + {(b**n)} = {(c**n)}")
        print("No, that doesn't work")

def inputs_fermat():

    a = int(input("Insert a value for a: "))
    b = int(input("Insert a value for b: "))
    c = int(input("Insert a value for c: "))
    n = int(input("Insert a value for n: "))

    check_fermat(a, b, c, n)


print("\n\nCheck Fermat's Last Theorem\n")
print("There are no positive integers a,b and c such that \n"
      "(a**n) + (b**n) = (c**n) for any values of n greater than 2.\n")

inputs_fermat()
