#Questão 1
indice = 13
soma = 0
k = 0
def somar(indice,soma,k):
    while k < indice:
        k = k + 1
        soma = soma + k
    return soma

print(somar(indice,soma,k))

# A SOMA É 91



#Questão 2
#num é o número que será testado
def fibonacci(num):
    #num1 e num2 são as duas variáveis auxiliares
    num1 = 0
    num2 = 1
    #caso seja inserido 1 ou 0 será pertencente à sequencia de Fibonacci
    if num == 1 or num == 0:
        print("Pertence a sequência de Fibonacci.")
        return 0
    
    while num > num1:
        soma = num1+num2
        num1 = num2
        num2 = soma
        #Se o novo item da sequência de fibbonaci for o número inserido, ele pertence à sequência!
        if num2 == num:
            print("Pertence a sequência de Fibonacci.")
            return 0
    
    print("Não pertence a sequência de Fibonacci.")
    return 0

fibonacci(1)


#Questão 3

# a) 1,3,5,7,9
# b) 2,4,8,16,32,64,128
# c) 0, 1, 4, 9, 16, 25, 36, 49
# d) 4, 16, 36, 64, 100
# e) e) 1, 1, 2, 3, 5, 8, 13
# f) 2,10, 12, 16, 17, 18, 19, 200


#Questão 4
"""Supondo que tenham 3 interruptores : A, B e C. Ligaria o interruptor A e deixaria ligado por um bom tempo. 
Depois desligaria o interruptor A e  ligaria o interuptor B. Logo após ligar o interruptor B, iria na primeira sala, se estiver apagada e fria, sei que se trata 
do interruptor C. Se estiver desligada e quente, sei que se trata do interruptor A.Caso esteja ligada, será o interruptor B. Agora basta repetir o processo para a segunda sala e consequentemente a 
opção que sobrar será a última sala. """



#Questão 5
#frase é a string a ser passada para a função
def inverterString(frase):
    #fraseInvertida é a variável tipo STR que receberá os caracteres
    fraseInvertida = ''
    #irei percorrer de trás para frente a string
    for i in range(len(frase)-1,-1,-1):

        #adicionarei cada caracter na fraseInvertida
        fraseInvertida =  fraseInvertida + frase[i]
    
    print(fraseInvertida)
    return 0

inverterString("Meu nome é Yuri Mello")



#Finalizado, Obrigado :)