# Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.

def product_num(m,n):
    if n==1:
        return m
    else:
        return m+ product_num(m,n-1)

    
print("The sum is :"+str(product_num(4,2)))