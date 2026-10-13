import sys

def simInt(principal, rate, time):
    return (principal * rate * time) / 100

p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

print("simple interest:", simInt(p, r, t))