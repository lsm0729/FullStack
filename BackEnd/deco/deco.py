def outer_func():
    print(f'call outer_func function')

    def inner_func():
        return f'call inner_func functions'
    print(inner_func())

outer_func()