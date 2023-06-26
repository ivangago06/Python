class Calculadora:
    def sumar(n1, n2):
        return n1 + n2
    
    def restar(n1, n2):
        return n1 - n2
    
    def multiplicar(n1, n2):
        return n1 * n2
    
    def dividir(n1, n2):
        return n1 / n2
    

resultado_suma = Calculadora.sumar(8,9)
resultado_resta = Calculadora.restar(8,9)
resultado_producto = Calculadora.multiplicar(8,9)
resultado_dividir = Calculadora.dividir(8,9)

print(resultado_suma)
print(resultado_resta)
print(resultado_producto)
print(resultado_dividir)