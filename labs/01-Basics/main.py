# Python program to illustrate 
# function with main
def getInteger():
    result = 3
    return result
  
def main():
    print("Started")
  
    # calling the getInteger function and 
    # storing its returned value in the output variable
    output = getInteger()     
    print(output)
  
# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    main()