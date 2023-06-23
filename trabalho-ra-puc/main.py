import json

refeicoes = []  # Lista para armazenar as refeições
usuarios = {}  # Dicionário para armazenar os usuários e senhas

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    usuarios[nome_usuario] = senha
    
    print("Usuário cadastrado com sucesso!")

# Função para fazer login
def fazer_login():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Verifica se o nome de usuário e senha estão corretos
    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

# Função para adicionar uma refeição
def adicionar_refeicao():
    nome_refeicao = input("Digite o nome da refeição: ")
    
    alimentos = []  # Lista para armazenar os alimentos da refeição
    
    # Loop para adicionar alimentos à refeição
    while True:
        nome_alimento = input("Digite o nome do alimento (ou 'sair' para finalizar a refeição): ")
        if nome_alimento.lower() == 'sair':
            break
        
        calorias = float(input("Digite a quantidade de calorias do alimento: "))
        proteinas = float(input("Digite a quantidade de proteínas do alimento: "))
        carboidratos = float(input("Digite a quantidade de carboidratos do alimento: "))
        gorduras = float(input("Digite a quantidade de gorduras do alimento: "))
        
        alimento = {
            'nome': nome_alimento,
            'calorias': calorias,
            'proteinas': proteinas,
            'carboidratos': carboidratos,
            'gorduras': gorduras
        }
        
        alimentos.append(alimento)
    
    refeicao = {
        'nome': nome_refeicao,
        'alimentos': alimentos
    }
    
    refeicoes.append(refeicao)
    print("Refeição adicionada com sucesso!")

# Função para remover uma refeição
def remover_refeicao():
    nome_refeicao = input("Digite o nome da refeição a ser removida: ")
    
    # Percorre a lista de refeições e remove a refeição com o nome especificado
    for refeicao in refeicoes:
        if refeicao['nome'] == nome_refeicao:
            refeicoes.remove(refeicao)
            print("Refeição removida com sucesso!")
            return
    
    print("Refeição não encontrada!")

# Função para exibir as refeições
def exibir_refeicoes():
    if not refeicoes:
        print("Nenhuma refeição adicionada.")
    else:
        print("Refeições adicionadas:")
        for refeicao in refeicoes:
            print(f"\nNome: {refeicao['nome']}")
            print("Alimentos:")
            for alimento in refeicao['alimentos']:
                print(f"- {alimento['nome']}:")
                print(f"  Calorias: {alimento['calorias']}")
                print(f"  Proteínas: {alimento['proteinas']}")
                print(f"  Carboidratos: {alimento['carboidratos']}")
                print(f"  Gorduras: {alimento['gorduras']}")
            
            # Calcula as calorias e proteínas totais da refeição
            calorias_total = sum(alimento['calorias'] for alimento in refeicao['alimentos'])
            proteinas_total = sum(alimento['proteinas'] for alimento in refeicao['alimentos'])
            carboidratos_total = sum(alimento['carboidratos'] for alimento in refeicao['alimentos'])
            gorduras_total = sum(alimento['gorduras'] for alimento in refeicao['alimentos'])
            
            # Exibe as calorias e proteínas totais da refeição
            print(f"Calorias totais: {calorias_total}")
            print(f"Proteínas totais: {proteinas_total}")
            print(f"Carboidratos totais: {carboidratos_total}")
            print(f"Gorduras totais: {gorduras_total}")

# Função para calcular as calorias e proteínas totais do dia
def calcular_total_dia():
    calorias_total_dia = 0
    proteinas_total_dia = 0
    carboidratos_total_dia = 0
    gorduras_total_dia = 0
    
    # Percorre a lista de refeições e soma as calorias e proteínas de cada alimento
    for refeicao in refeicoes:
        calorias_total = sum(alimento['calorias'] for alimento in refeicao['alimentos'])
        proteinas_total = sum(alimento['proteinas'] for alimento in refeicao['alimentos'])
        carboidratos_total = sum(alimento['carboidratos'] for alimento in refeicao['alimentos'])
        gorduras_total = sum(alimento['gorduras'] for alimento in refeicao['alimentos'])
        
        calorias_total_dia += calorias_total
        proteinas_total_dia += proteinas_total
        carboidratos_total_dia += carboidratos_total
        gorduras_total_dia += gorduras_total
    
    # Exibe as calorias e proteínas totais do dia
    print("Total do dia:")
    print(f"Calorias totais do dia: {calorias_total_dia}")
    print(f"Proteínas totais do dia: {proteinas_total_dia}")
    print(f"Carboidratos totais do dia: {carboidratos_total_dia}")
    print(f"Gorduras totais do dia: {gorduras_total_dia}")

# Função para salvar as refeições em um arquivo JSON
def salvar_refeicoes():
    with open('refeicoes.json', 'w') as arquivo:
        json.dump(refeicoes, arquivo)

# Função para carregar as refeições de um arquivo JSON
def carregar_refeicoes():
    global refeicoes
    try:
        with open('refeicoes.json', 'r') as arquivo:
            refeicoes = json.load(arquivo)
        print("Refeições carregadas com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de refeições encontrado.")

# Menu principal do programa
def menu_principal():
    print("----- Bem-vindo ao Sistema de Refeições -----")
    while True:
        print("\nOpções:")
        print("1 - Cadastrar novo usuário")
        print("2 - Fazer login")
        print("0 - Sair")
        
        opcao_principal = input("Digite a opção desejada: ")
        
        if opcao_principal == '1':
            cadastrar_usuario()
        elif opcao_principal == '2':
            if fazer_login():
                menu_usuario()
        elif opcao_principal == '0':
            break
        else:
            print("Opção inválida!")

# Menu do usuário após o login
def menu_usuario():
    while True:
        print("\nOpções:")
        print("1 - Adicionar refeição")
        print("2 - Remover refeição")
        print("3 - Exibir refeições")
        print("4 - Calcular total do dia")
        print("5 - Salvar refeições")
        print("6 - Carregar refeições")
        print("0 - Sair")
        
        opcao_usuario = input("Digite a opção desejada: ")
        
        if opcao_usuario == '1':
            adicionar_refeicao()
        elif opcao_usuario == '2':
            remover_refeicao()
        elif opcao_usuario == '3':
            exibir_refeicoes()
        elif opcao_usuario == '4':
            calcular_total_dia()
        elif opcao_usuario == '5':
            salvar_refeicoes()
        elif opcao_usuario == '6':
            carregar_refeicoes()
        elif opcao_usuario == '0':
            break
        else:
            print("Opção inválida!")

# Inicia o programa chamando o menu principal
menu_principal()
