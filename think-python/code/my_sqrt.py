import math

def mysqrt(a):
    
    epsilon = 0.00001

    if a % 2 == 0:
        x = a / 2
    else:
        x = a / 3

    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon: 
            break
        x = y
    
    return y

def test_square_root():

    print("a    mysqrt(a)   math.sqrt(a)    diff\n"
          "-    ---------   ------------    ----\n")

    a = 1.0
    while a <= 9:
        ms = mysqrt(a)
        mths = math.sqrt(a)
        print(f"{a}   {ms}    {mths}    {abs(ms - mths)}")
        a += 1

test_square_root()