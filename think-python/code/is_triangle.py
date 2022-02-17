def is_triangle(a, b, c):
    if (a <= b + c) and (b <= a + c) and (c <= b + a):
        print("\nYes")
    else:
        print("\nNo")


def inputs_triangle():

    a = int(input("Insert a value for a: "))
    b = int(input("Insert a value for b: "))
    c = int(input("Insert a value for c: "))
    is_triangle(a, b, c)

print("\n\nCheck if three lenghts can form a triangle\n")

print("If any of the three lengths is greater than the sum \n" 
      "of the other two, then you cannot form a triangle. \n"
      "Otherwise, you can. (If the sum of two lengths equals \n"
      "the third, they form what is called a “degenerate” triangle.)\n\n")

inputs_triangle()
