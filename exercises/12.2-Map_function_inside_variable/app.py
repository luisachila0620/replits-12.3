names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name

#Your code go here:
names_list = ()
result = map(prepender, names)
print(list(result))