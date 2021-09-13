def show(func):
    def new_func(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        
    return new_func