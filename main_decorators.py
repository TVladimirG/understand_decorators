# В Python - все является объектами. В том числе функция.
# Раз функция это объект, то значит согласно определению:
#  фукнцию можем сохранить в переменную, и передать в функцию в качестве аргументов,
#  вернуть в качестве результата функции, или даже объявить в другом объекте.

# Декоратор - функция принимающая на вход другую функцию
# Декораторы могут быть вложены друг в друга

def my_decorator(show_info=False):
    def decorator(func):     # Вот и сам декоратор, принимает функцию
        def wrapper(*args, **qwargs):
            # можем посмотреть на входящие данные
            arg = args[0]                             # args это кортеж
            qwarg = qwargs.get('type_info')    # qwargs это словарь

            if show_info:  # Аргумент декоратора
                print(f'wrapper: arg = {arg}, qwarg = {qwarg} ')

            value = func(*args, **qwargs)
            return value

        return wrapper
    return decorator


# Мой декоратор с аргументом
# Если аргумент не нужно передавать, тогда my_decorator убрать и просто: @decorator 
@my_decorator(show_info=True)
def my_func(content: str, type_info: str) -> str:
    return f'my_func: content = {content}, type_info = {type_info}'


# Моя функция имеет один позиционный и один именованный аргументы
val: str = my_func('mysite.mail',  type_info='url')
print(val)
