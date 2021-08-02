import datetime
import functools

def CreateFuncWrapper(func):
    def func_with_wrapper(*args,**kwargs):
        print('Function started at {}'.format(datetime.datetime.now().isoformat()))
        print('Following arguments were used')
        print(args,kwargs)
        result = func(*args,**kwargs)
        print('+'*10)
        return result
    return func_with_wrapper
@CreateFuncWrapper
def changesalary(employeename,newsalary,isbonus=False):
    print('changing salary for {} to {} as bonus = {}'.format(employeename,newsalary,isbonus))
    return newsalary

#changesalary = CreateFuncWrapper(changesalary)

print(changesalary('John',2000,True))
