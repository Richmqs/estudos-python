# Mini calculadora simples

# Definindo as variáveis de entrada
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

#.lower() sendo utilizado após a variável "operacao" para que comporte qualquer semântica utilizada pelo usuário
operacao = input("Qual operação você deseja realizar? ").lower()

# Definindo condicionais partindo de um pressuposto específico 
if operacao == "soma":
    print (f"A soma dos números digitados é de: {primeiro_numero + segundo_numero} ")
elif operacao == "subtração":
    print (f"A subtração dos números digitados é de: {primeiro_numero - segundo_numero} ")
elif operacao == "divisão":
    #O if abaixo foi inserido para que caso o usuária digite 0 no segundo número o programa não quebre
    if segundo_numero == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        print(f"O valor da divisão entre os números digitados é de: {primeiro_numero / segundo_numero} ")       
elif operacao == "multiplicação":
    print(f"O valor da multiplicação entre os números digitados é de: {primeiro_numero * segundo_numero} ")  
    # Else que encerra o programa caso o usuário não digite uma operação válida 
else:
    print("Erro! Digite uma das quatro operações matemáticas básicas!! ")


