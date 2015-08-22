# time complexity 

# 1.1 dominant operation
def logarithmic(n): 
    result = 0
    while n > 1: 
        n //= 2
        result += 1 
    return result

# 1.2 constant time
def constant(n):
    result = n * n
    return result

# 1.3 linear time
def quadratic(n):
    result = 0
    for x in xrange(n):
        for y in xrange(x, n):
            result += 1
    return result

def linear(n, m):
    result = 0 
    for i in xrange(n):
        result += i
    for j in xrange(m):
        result += j 
    return result

n = 2
m = 2

print "logarithmic:",logarithmic(n)
print "constant:",constant(n)
print "quadratic:",quadratic(n)
print "linear:",linear(n,m) 

