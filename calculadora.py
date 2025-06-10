# Calculadora em Python
# Criador: Douglas Magalhães de Vasconcelos

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.\n")
        return None

def calculadora():
    while True:
        try:
            print("--- Calculadora ---")
            print("1. - Somar")
            print("2. - Subtração")
            print("3. - Multiplicação")
            print("4. - Divisão")
            print("5. - Sair")
            
            escolha = input("Escolha uma operação matemática: ")

            if escolha == "5":
                print("Programa encerrado com sucesso!")
                break
            
            if escolha in ['1','2', '3', '4']:
                number1 = float(input("Digite um número: "))
                number2 = float(input("Digite um número: "))
            else:
                raise ValueError("Opção inválida! Escolha 1, 2, 3, 4 ou 'sair'.")
            
            if escolha == '1':
                resultado = somar(number1, number2)
                print(f"Resultado da soma de {number1} + {number2} = {resultado}")
            elif escolha == '2':
                resultado = subtrair(number1, number2)
                print(f"Resultado da subtração de {number1} - {number2} = {resultado}")
            elif escolha == '3':
                resultado = multiplicar(number1, number2)
                print(f"Resultado da multiplicação de {number1} * {number2} = {resultado}")
            elif escolha == '4':
                resultado = dividir(number1, number2)
                if resultado is not None:
                    print(f"Resultado da divisão de {number1} / {number2} = {resultado:0.2f}")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    calculadora()

# Lema do Douglas:
# Programação exige determinação constante.
