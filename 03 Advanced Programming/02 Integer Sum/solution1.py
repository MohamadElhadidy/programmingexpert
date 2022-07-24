def flatten_lists(func):
    def wrapper(*args):
        lst = []
        for arg in args:
            if isinstance(arg, list):
                lst.extend(arg)
            else:
                lst.append(arg)
            
        result = func(*lst)
        return result

    return wrapper

def convert_strings_to_ints(func):
    def wrapper(*args):
        lst = []
        for arg in args:
            if isinstance(arg, str ) and arg.isdigit():
                lst.append(int(arg))
            else:
                lst.append(arg)
            
        result = func(*lst)
        return result
    
    return wrapper

def filter_integers(func):
    def wrapper(*args):
        lst = []
        for arg in args:
            if isinstance(arg,int) :
                lst.append(arg)
            
        result = func(*lst)
        return result
    
    return wrapper

@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)