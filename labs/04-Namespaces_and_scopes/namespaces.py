# var1 is in the global namespace
var1 = 5
# some_func() is in the global namespace
def some_func():
 
    # var2 is in the local namespace
    var2 = 6
    # some_inner_func() is in the local namespace
    def some_inner_func():
        # var3 is in the nested local
        # namespace
        var3 = 7
        # print function is in the built-in namespace
        print(var1 + var2 + var3)
    some_inner_func()
some_func()