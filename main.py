import time
import random


def busca_linear(array, tamanho, alvo):
    posicoes_visitadas = 0
    for j in range(tamanho):
        posicoes_visitadas += 1
        if array[j] == alvo:
            return j, posicoes_visitadas
    return -1, posicoes_visitadas



def busca_binaria(array, alvo, menor, maior):
    posicoes_visitadas = 0
    while menor <= maior:
        meio = menor + (maior - menor) // 2
        posicoes_visitadas += 1
        if array[meio] == alvo:
            return meio, posicoes_visitadas
        elif array[meio] < alvo:
            menor = meio + 1
        else:
            maior = meio - 1
    return -1, posicoes_visitadas


def main():
    tamanho = int(input("diga o tamanho da array: "))
    array = [i for i in range(tamanho)]
    #print(array)
    print(f"sua array vai do numer 0 até {tamanho-1}")

    alvo = input("\nEscolha o número que deseja encontrar ou escreva -1 para que um número aleatório seja escolhido: ")
    if alvo == "-1":
        alvo = random.choice(array)
        print(f"Número aleatório: {alvo}")
    else:
        alvo = int(alvo)

    print("\nBusca Binária")
    start_time = time.perf_counter()
    numero, posicoes_visitados = busca_linear(array,tamanho, alvo)
    end_time = time.perf_counter()
    if numero == -1:
        print("\nnumero nao esta na array")
    else:
        print(f"numero {array[numero]} encontrado na posicao {numero}")
    print(f"{posicoes_visitados} posicoes visitados na array com um tempo de execucaode : {(end_time - start_time) * 1000:.6f} ms")

    print("\nBusca Binária")
    start_time = time.time()
    numero, posicoes_visitadas = busca_binaria(array, alvo, 0, tamanho - 1)
    end_time = time.time()
    if numero == -1:
        print("\nNúmero não está na array")
    else:
        print(f"Número {array[numero]} encontrado na posição {numero}")
    print(f"{posicoes_visitadas} posições visitadas. Tempo de execução: {(end_time - start_time) * 1000:.6f} ms")




main()