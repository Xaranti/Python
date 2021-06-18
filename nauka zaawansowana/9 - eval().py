var_x = 10
password = 'secret password'
source = 'password'

globals = globals().copy()
del globals['password']
result =eval(source, globals)
print (result)

print (globals())