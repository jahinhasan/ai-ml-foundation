def find_error(actual,predicted):
    error=[]
    for i in range(len(actual)):
            error.append(pow((actual[i] - predicted[i]),2))

    return error


def mse(actual,predicted):
    if len(actual) != len(predicted):
        raise ValueError("Lists must have same length")

    error=find_error(actual,predicted)
    n=len(error)
   
    result=0
    for i in error:
        result+=i
    
    MSE=result/n
    return MSE


actual=[3,5,2]
predicted=[2,5,4]
print(mse(actual,predicted))