
def reverse(str):
    n = len(str) - 1
    rev(str, n)

def rev(str, n):
    if n < 0:
        return
    print(str[n])
    rev(str, n-1)

print(reverse("adewale"))