#%%
def find_message(text: str) -> str:
    """Find a secret message"""
    
    up = [i for i in text if i.isupper() == True ]
    up_to_string = "".join(up)

    #find_message = lambda text: ''.join(filter(str.isupper, text))


    return up_to_string

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# %%
# Your optional code here
# You can import some modules or create additional functions


def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    # replace this for solution
    if number % 3 ==False and number % 5 == False:
        return 'Fizz Buzz'
    elif number % 3 ==False :
        return "Fizz"
    elif number % 5 ==False:
        return "Buzz"
    else:
        return str(number)
    #return 'Fizz'*(not n%3)+' '*(not n%15)+'Buzz'*(not n%5) or str(n)

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#%%
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if array ==[]:
        return 0
    n = 0
    a = 0
    for i in array:
        while n < len(array):
            a += array[n]
            n+=2
    result = a*array[-1]
    return result
    '''
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

    checkio=lambda x: sum(x[::2])*x[-1] if x else 0

    '''


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#%%
def best_stock(a):
    x = {key : value for key, value in sorted(a.items(), key = lambda a : a[1], reverse = True)}

    return list(x.keys())[0]
'''
return max(data, key=data.__getitem__)
return max(data, key=lambda x: data[x])

'''

if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")

#%%
a = dict({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2})
b = 0
for key, value in a.items():
    if b < value:
        b = value
        c = key
print(key)

# %%
a = dict({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2})
b= 0 
for i ,(key, value) in enumerate(a.items()):
    if i == 0:
        b = value
    else:
        if b < value:
            b = value
            c = key
print(key)
    
