def swap(string):
     
    # storing the first character
    start = string[-1]
     
    # storing the last character
    end = string[0]
    #middle=string[1:-1]
    swapped_string = start + string[1:-1] + end
    print(swapped_string)
     

a=input("Enter the string")
swap(a)
