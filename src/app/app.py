from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b

    def division(a,b):
        return a/b

    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(lista):
        """
        Verifica si hay al menos un número primo en la lista.
        Retorna True si hay un número primo, de lo contrario, False. Hola
        """
        def es_primo(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        return any(es_primo(num) for num in lista)
        pass

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(inicio, fin):
        """
        Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
        Retorna la cantidad de números pares.
        """
        return len([num for num in range(inicio, fin + 1) if num % 2 == 0])
        pass

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(lista, multiplo):
        """
        Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
        Si no hay múltiplos, retorna None.
        """
        multiplos = [num for num in lista if num % multiplo == 0]
        return max(multiplos) if multiplos else None
        pass

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        palabra = palabra.lower()
        return palabra == palabra[::-1]
        pass

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(n):
        """
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
        return sum([i for i in range(1, 2 * n, 2)])
        pass

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        return len(lista) == len(set(lista))
        pass

    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial
        pass

    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        vocales = 'aeiouAEIOU'
        return sum(1 for char in cadena if char in vocales)
        pass

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        unique_sorted = sorted(set(lista), reverse=True)
        return unique_sorted[1] if len(unique_sorted) > 1 else None
        pass

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib
        pass
