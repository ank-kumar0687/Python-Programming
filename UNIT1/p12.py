a = 10   

def outer_function():
    b = 20   

    def inner_function():
        nonlocal b      
        global a        

        b = b + 5       
        a = a + 5       

        c = 30          
        print("Local variable c:", c)

    inner_function()
    print("Nonlocal variable b:", b)

outer_function()
print("Global variable a:", a)