def is_even(num):
    """ 
    this function return if a given number is odd or even 
    input - any valid integer
    output - odd/even
    created on - 16th Nov 2022
    """
    if type(num) == int:  
      if num % 2 ==0:
        return 'even'
      else:
        return 'odd'
    else:
     return "please enter integer"     

       #function

for i in range(1,11):
    x = is_even(i)
    print(x)

