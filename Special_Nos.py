def magic_no(n):
    # Magic no.
    num = n
    sum1 = 0
    c = 0
    sum2 = 0
    while num > 0:
        num = num // 10
        c += 1
    for a in range(c):
        x = n % 10
        n = n // 10
        sum1 += x
    while sum1 > 0:
        y = sum1 % 10
        sum1 = sum1 // 10
        sum2 += y
    if sum2 == 1:
        print("It is a mgaic no.")
    else:
        print("Not a magic no.")


def perfect_no(n):
    l = []
    um = 0
    for a in range(1, n):
        if n % a == 0:
            l.append(a)
    for i in range(len(l)):
        um += l[i]

    if um == n:
        print("It is is a perfect no.")
    else:
        print("Its not a perfect no.")


def armstrong_no(n):
    num = n
    c = 0
    cube = 0
    num2 = n
    while num > 0:
        num = num // 10
        c += 1
    for a in range(c):
        x = num2 % 10
        num2 = num2 // 10
        cube += (x ** 3)
    if cube == n:
        print("It is an armstrong no.")
    else:
        print("It is not an armstrong no.")


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def strong_no(n):
    num=n
    num2=n
    c=0
    s=0
    while num > 0:
        num = num // 10
        c += 1
    for a in range(c):
        x = num2 % 10
        num2 = num2 // 10
        s+= fact(x)
    if s==n:
        print("It is a Strong No.")
    else:
        print("It is not a strong no.")


'''def prime_no(n):
    for a in range(2,n):
        if n%a==0:
            c+=1'''
def main2():
    n=int(input("n:"))
    magic_no(n)
    perfect_no(n)
    armstrong_no(n)
    strong_no(n)
main2()
