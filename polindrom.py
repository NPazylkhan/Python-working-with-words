a = str(input())
b = a[::-1]
print(b)
k = int(len(a)/2)
print("yes" if a[0:k] == b[0:k] else "no")