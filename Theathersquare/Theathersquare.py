a,b,c = map(int, input().split)

if a%c == 0:
    val1 = a//c
else:
    val1 = a//c + 1

if b%c ==0:
    val2 = b //c
else:
    val2 = b//c + 1

print(val1 * val2)