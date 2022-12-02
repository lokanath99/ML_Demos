# def disp_name(name = 'john doe', corse = 'AI'): # default args
def disp_name(name, corse, **kwargs):
    print('name :', name)
    print('course :', corse)
    for i, j in kwargs.items():
        print(i, " : ", j)
    # print(kwargs.items())


# def add(a, b, *c):#varianble length args
def add(a, b):
    print(type(a))
    return a+b#+sum(c)

def count_E_O(lst):
    even,odd = 0,0
    for e in lst:
        if e % 2 == 0:
            even+=1
        else:
            odd+=1

    return even, odd

# print(add(2,6))#position
# print(add(b=6, a=2))#keyword argument
# disp_name('talkalot', 'ML')
# disp_name(corse='ML')
# print(add(1, 3, 3, 5))
# disp_name(name='talkalot', corse='ML' , age= 90, college='JIT', classroom='iT2')# key word length arguments


# even, odd = count_E_O([26,69,8,56,3,21,6,51])
# print("number even numbers: ", even)
# print("number odd numbers: ", even)

# #scope of variables
# a = 10#global
# b = 20
#
# def change_var():
#     globals()['a'] = 15
#     # global a
#     a = 20#local
#     print("inside change",a)
#
# change_var()
# print(a)

# #anonymous functions(lamda)

# def square(a):
#     return a*a
def add(a,b):
    return a+b

f = lambda a,b : a+b

print(f(5,5))
