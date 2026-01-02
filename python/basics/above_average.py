def avarage(number):
    total=0
    for i in number:
        total=total+i
    length=len(number)
    avg=total/length
    count=0
    for i in number:
        if avg<i:
            count=count+1
    return count


number=[2,4,6,8]
print(avarage(number))
