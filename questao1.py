class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


inicio = None
cont_v = 1
cont_a = 201


def inserirSemPrioridade(novo):
    global inicio
    if inicio is None:
        inicio = novo
    else:
        atual = inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo


def inserirComPrioridade(novo):
    global inicio
    if inicio is None or inicio.cor == 'V':
        novo.proximo = inicio
        inicio = novo
    else:
        atual = inicio
        while atual.proximo is not None and atual.proximo.cor == 'A':
            atual = atual.proximo
        novo.proximo = atual.proximo
        atual.proximo = novo


def inserir():
    global cont_v, cont_a
    cor = input("Informe a cor do cartão (A/V): ").upper()

    if cor == 'V':
        numero = cont_v
        cont_v += 1
        print(f"Informe o número do cartão: {numero}")
        novo = Nodo(numero, cor)
        inserirSemPrioridade(novo)

    elif cor == 'A':
        numero = cont_a
        cont_a += 1
        print(f"Informe o número do cartão: {numero}")
        novo = Nodo(numero, cor)
        inserirComPrioridade(novo)
    else:
        print("Cor inválida.")


def imprimirListaEspera():
    atual = inicio
    texto = "Lista -> "
    while atual is not None:
        texto += f"[{atual.cor},{atual.numero}] "
        atual = atual.proximo
    print(texto)


def atenderPaciente():
    global inicio
    if inicio is not None:
        print(f"Atendendo o paciente cartão cor {inicio.cor} e número {inicio.numero}")
        inicio = inicio.proximo
    else:
        print("Nenhum paciente na fila.")


# Menu principal
while True:
    print("1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - sair")

    op = input(">>")

    if op == '1':
        inserir()
    elif op == '2':
        imprimirListaEspera()
    elif op == '3':
        atenderPaciente()
    elif op == '4':
        break