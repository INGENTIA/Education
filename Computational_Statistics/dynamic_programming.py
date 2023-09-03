
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)



if __name__ == '__main__':

    n = int(input('choice a number: '))
    resultado = fibonacci_recursivo(n)
    print(n)
