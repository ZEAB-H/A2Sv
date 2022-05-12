a,b,c = map(int, input().split)

if b%c == 0:
    val1 = b//c
else:
    val1 = b//c + 1

if a%c ==0:
    val2 = a //c
else:
    val2 = a//c + 1

print(val1 * val2)