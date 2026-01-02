def find_list(maximum,number):
    new_list=[]
    
    for i in number:
        element=i/maximum
        new_list.append(element)
    return new_list



def find_max(number):
    maximum=number[0]
    length=len(number)
    for i in range(1,length):
        if number[i]>maximum :
            maximum=number[i]
    print(find_list(maximum,number))


number = [2,4,6,8]
find_max(number)
