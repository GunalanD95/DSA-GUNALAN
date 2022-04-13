# Python – Remove duplicate values across Different Dictionary Values


test_dic1 = {
    'manoj' : [1],
    'akash' : [1,8,9],
}

test_dic2 = {
    'manoj' : [1, 1, 1], 
    'akash' : [1, 1, 1], 
}

# 1 Using Naive Method

def removeval(dics):
    result = {}

    for key,value in dics.items():
        if value not in result.values():
            result[key] = value
    return result

print("rm",removeval(test_dic1))