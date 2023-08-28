q = 0
for n in range(5, 101):
    if n%7==0 and n%5!=0:
        print(n)
        q += 1
print(f'A quantidade é {q}')