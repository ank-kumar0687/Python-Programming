t = (20, 30, 40)

print("tuple:", t)


try:
    t[1] = 50
except TypeError:
    print("Tuple is immutable, cannot be modified")