import os

# =========================
# DEFINIÇÃO DAS CLASSES
# =========================


# Classe que representa um pedido
class Pedido:
    def __init__(self, codigo_pedido, valor_pedido):
        self.codigo_pedido = codigo_pedido       # Código único do pedido
        self.valor_pedido = valor_pedido         # Valor monetário do pedido
        self.status_pedido = "PENDENTE"         # Status inicial do pedido

    # Método para alterar o status do pedido
    def alterar_status(self, novo_status):
        self.status_pedido = novo_status

# Classe que representa um cliente
class Cliente:
    def __init__(self, nome_cliente, cpf_cliente):
        self.nome_cliente = nome_cliente         # Nome do cliente
        self.cpf_cliente = cpf_cliente           # CPF do cliente (somente números)
        self.lista_pedidos = []                  # Lista de pedidos do cliente

    # Método para adicionar um pedido à lista do cliente
    def adicionar_pedido(self, pedido):
        self.lista_pedidos.append(pedido)

    # Método para buscar um pedido pelo código
    def buscar_pedido(self, codigo_pedido):
        for pedido in self.lista_pedidos:
            if pedido.codigo_pedido == codigo_pedido:
                return pedido
        return None

# =========================
# "BANCO DE DADOS" EM MEMÓRIA
# =========================
lista_clientes = []  # Lista que armazenará os clientes cadastrados

# =========================
# FUNÇÕES DE APOIO
# =========================

# Limpar a tela do terminal (Windows ou Linux/Mac)
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Pausar a execução até o usuário pressionar ENTER
def pausar():
    input("\nPressione ENTER para continuar...")

# Validar CPF: deve ter apenas números e 11 dígitos
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Buscar cliente na lista pelo CPF
def buscar_cliente_por_cpf(cpf):
    for cliente in lista_clientes:
        if cliente.cpf_cliente == cpf:
            return cliente
    return None

# =========================
# FUNÇÕES PRINCIPAIS
# =========================

# Cadastro de um novo cliente
def cadastrar_cliente():
    limpar_tela()
    print("=== CADASTRO DE CLIENTE ===\n")

    nome_cliente = input("Digite o nome do cliente: ")
    cpf_cliente = input("Digite o CPF (somente números): ")

    # Validação do CPF
    if not validar_cpf(cpf_cliente):
        print("\nCPF inválido!")
        pausar()
        return

    # Verifica se o cliente já está cadastrado
    if buscar_cliente_por_cpf(cpf_cliente):
        print("\nCliente já cadastrado!")
        pausar()
        return

    # Cria e adiciona o cliente à lista
    novo_cliente = Cliente(nome_cliente, cpf_cliente)
    lista_clientes.append(novo_cliente)

    print("\nCliente cadastrado com sucesso!")
    pausar()

# Listar todos os clientes cadastrados
def listar_clientes():
    limpar_tela()
    print("=== LISTA DE CLIENTES ===\n")

    if not lista_clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for indice, cliente in enumerate(lista_clientes, start=1):
            print(f"{indice}. Nome: {cliente.nome_cliente} | CPF: {cliente.cpf_cliente} | Total de pedidos: {len(cliente.lista_pedidos)}")

    pausar()

# Criar um novo pedido para um cliente existente
def criar_pedido():
    limpar_tela()
    print("=== CRIAÇÃO DE PEDIDO ===\n")

    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf_cliente)

    if not cliente:
        print("\nCliente não encontrado!")
        pausar()
        return

    codigo_pedido = input("Digite o código do pedido: ")

    try:
        valor_pedido = float(input("Digite o valor do pedido: R$ "))
    except ValueError:
        print("\nValor inválido!")
        pausar()
        return

    # Cria o pedido e adiciona ao cliente
    novo_pedido = Pedido(codigo_pedido, valor_pedido)
    cliente.adicionar_pedido(novo_pedido)

    print("\nPedido criado com sucesso!")
    pausar()

# Listar todos os pedidos de um cliente específico
def listar_pedidos_cliente():
    limpar_tela()
    print("=== PEDIDOS DO CLIENTE ===\n")

    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf_cliente)

    if not cliente:
        print("\nCliente não encontrado!")
        pausar()
        return

    print(f"\nCliente: {cliente.nome_cliente}\n")

    if not cliente.lista_pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for pedido in cliente.lista_pedidos:
            print(f"Código: {pedido.codigo_pedido} | Valor: R$ {pedido.valor_pedido:.2f} | Status: {pedido.status_pedido}")

    pausar()

# Alterar o status de um pedido específico
def alterar_status_pedido():
    limpar_tela()
    print("=== ALTERAÇÃO DE STATUS ===\n")

    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf_cliente)

    if not cliente:
        print("\nCliente não encontrado!")
        pausar()
        return

    codigo_pedido = input("Digite o código do pedido: ")
    pedido = cliente.buscar_pedido(codigo_pedido)

    if not pedido:
        print("\nPedido não encontrado!")
        pausar()
        return

    # Menu de status
    print("\nEscolha o novo status:")
    print("1 - PENDENTE")
    print("2 - PAGO")
    print("3 - ENVIADO")
    print("4 - ENTREGUE")

    opcao_status = input("Opção: ")
    mapa_status = {"1": "PENDENTE", "2": "PAGO", "3": "ENVIADO", "4": "ENTREGUE"}

    if opcao_status in mapa_status:
        pedido.alterar_status(mapa_status[opcao_status])
        print("\nStatus atualizado com sucesso!")
    else:
        print("\nOpção inválida!")

    pausar()

# =========================
# MENU PRINCIPAL
# =========================
def menu_principal():
    while True:
        limpar_tela()
        print("====================================")
        print("   SISTEMA DE CLIENTES E PEDIDOS")
        print("====================================")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Criar pedido")
        print("4 - Listar pedidos do cliente")
        print("5 - Alterar status do pedido")
        print("0 - Sair")
        print("====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            criar_pedido()
        elif opcao == "4":
            listar_pedidos_cliente()
        elif opcao == "5":
            alterar_status_pedido()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida!")
            pausar()

# =========================
# EXECUÇÃO DO SISTEMA
# =========================
if __name__ == "__main__":
    menu_principal()