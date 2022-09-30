def add(v1, v2):
    """adds two vectors v₁ and v₂ component-wise as defined in (ℤ/2ℤ)⁴
    NOTE: the addition in ℤ mod 2 is equivalent to Binary XOR"""
    
    # ^ is the Bitwise XOR Operator in Python
    return tuple(v1[i] ^ v2[i] for i in range(4))


def multiply(c, v):
    """multiplies a scalar c with vector v component-wise as defined in (ℤ/2ℤ)⁴
    NOTE: the multiplication in ℤ mod 2 is equivalent to Binary AND"""
    
    # & is the Bitwise AND Operator in Python
    return tuple(c & v[i] for i in range(4))


def addition(set_of_tuples):
    """returns True if the given set of tuples is closed under Vector Addition, False otherwise"""
    
    for v1 in set_of_tuples:
        for v2 in set_of_tuples:
            if add(v1, v2) not in set_of_tuples:
                return False
    return True


def multiplication(set_of_tuples):
    """returns True if the given set of tuples is closed under Scalar Multiplication, False otherwise"""
    
    for c in {0, 1}:
        for v in set_of_tuples:
            if multiply(c, v) not in set_of_tuples:
                return False
    return True


def main():
    """__main__ function"""
    
    n = int(input("Enter number of vectors you want in the set: "))
    W = set()
    for _ in range(n):
        # an example of valid input may be 1, 0, 0, 1 OR 1,0,0,1
        # an example of invalid input may be 1 0 0 1
        v = input("Enter comma separated 4-tuple v₁, v₂, v₃, v₄: ").split(",")
        v = tuple(int(vi) for vi in v)
        
        if len(v) != 4 or set(v) not in ({0}, {1}, {0, 1}):
            print("Invalid Input!")
            break
        else:
            W.add(v)

    else:
        # W is a Vector Space iff it is closed under both Vector Addition and Scalar Multiplication
        print(addition(W) and multiplication(W))
    

if __name__ == "__main__":
    main()