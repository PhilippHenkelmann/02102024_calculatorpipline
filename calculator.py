def add (x,y):
    return y+x

def subtract (x,y):
    return y-x

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y


if __name__=="__main__":
    print("Calculator is running")