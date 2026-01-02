def avarage(number):
    total=0
    for i in number:
        total=total+i
    length=len(number)
    avg=total`/length
    return avg

number=[2,4,6,8]
print(avarage(number))
        