#
# a = 10
# b = 10
#
# assert a==b, "a and b are not same same"
# print("a and b same")


def devide(a,b):
    assert b>0,"b is zero not allowed"
    return a/b

result = devide(10,0)
print(result)