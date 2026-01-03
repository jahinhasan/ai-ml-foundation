def gradient(actual,predicted):
    if len(actual) != len(predicted):
        return "length of two list is not same"
    length=len(actual)
    gred=[]
    for i in range(length):
        result=predicted[i]-actual[i]
        gred.append((2*result)/length)
    return gred


actual= [3,5]
predicted=[2,6]
print(gradient(actual,predicted))