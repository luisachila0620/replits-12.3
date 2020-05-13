myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:
def increment_by_one (myNumbers): 
    return myNumbers * 3
  
# We double all numbers using map() 
new_list  = () 
result = map(increment_by_one, myNumbers) 
print(list(result)) 

