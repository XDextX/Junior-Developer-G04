# Created by German Montero at 16/8/2021
def factorial(numero: int):
    if numero == 0 or numero == 1:
        return numero
    else:
        return numero * factorial(numero - 1)


if __name__ == '__main__':
    print(factorial(5))
