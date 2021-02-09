import math

def expression_1(x):
    y = math.pow(x,3) - ((2*x) + math.pow(x,2)) -100
    return y

def expression_2(x, y):
    z = (math.pow(x,4)/(2*y)) - (3*x*y) + ((6*y)/(7*x))
    return int(z)


def expression_3(x, y):
    z = (math.pow(x,3) +math.pow(y,2)) / (math.pow(x,2) - math.pow(y,3))
    return z
    

if __name__ == "__main__":
    
    pass
