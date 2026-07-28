import os

DESCONTO_REMOCAO = 1.00  # Valor descontado ao retirar um ingrediente padrão


def inicializar_dados():
    opcionais = {
        "gerais": {"Bacon": 3.50, "Queijo Extra": 2.50, "Ovo": 2.00, "Cebola Crispy": 2.50},
        "bebidas": {"Gelo Extra": 0.50, "Hortelã": 1.00, "Leite Condensado": 3.00, "Limão Extra": 1.50},
        "doces": {"Calda de Chocolate": 2.50, "Morango": 3.00, "Sorvete Extra": 4.00, "Granola": 2.00}
    }

    cardapio = {
        "Pratos": [
            {"nome": "X-Tudo Burguer", "preco_base": 28.00,
             "ingredientes": ["Pão", "Carne", "Queijo", "Presunto", "Alface", "Tomate", "Milho"],
             "tipo_opcionais": "gerais"},
            {"nome": "Pizza Margherita", "preco_base": 45.00,
             "ingredientes": ["Massa", "Molho de Tomate", "Mussarela", "Manjericão", "Tomate"],
             "tipo_opcionais": "gerais"},
            {"nome": "Macarronada Bolonhesa", "preco_base": 32.00,
             "ingredientes": ["Macarrão", "Molho de Tomate", "Carne Moída", "Queijo Ralado"],
             "tipo_opcionais": "gerais"},
            {"nome": "Strogonoff de Frango", "preco_base": 35.00,
             "ingredientes": ["Arroz", "Batata Palha", "Frango", "Creme de Leite", "Cogumelo"],
             "tipo_opcionais": "gerais"},
            {"nome": "Feijoada Completa", "preco_base": 42.00,
             "ingredientes": ["Arroz", "Feijão Preto", "Carne Seca", "Linguiça", "Farofa", "Couve"],
             "tipo_opcionais": "gerais"},
            {"nome": "Lasanha aos Quatro Queijos", "preco_base": 38.00,
             "ingredientes": ["Massa", "Mussarela", "Provolone", "Parmesão", "Gorgonzola"], "tipo_opcionais": "gerais"},
            {"nome": "Salada Caesar", "preco_base": 25.00,
             "ingredientes": ["Alface", "Frango Grelhado", "Croutons", "Parmesão", "Molho Caesar"],
             "tipo_opcionais": "gerais"},
            {"nome": "Bife a Cavalo", "preco_base": 40.00,
             "ingredientes": ["Bife", "Ovo", "Arroz", "Feijão", "Batata Frita"], "tipo_opcionais": "gerais"},
            {"nome": "Risoto de Funghi", "preco_base": 48.00,
             "ingredientes": ["Arroz Arbóreo", "Funghi", "Parmesão", "Manteiga"], "tipo_opcionais": "gerais"},
            {"nome": "Filé à Parmegiana", "preco_base": 52.00,
             "ingredientes": ["Filé Mignon", "Mussarela", "Molho de Tomate", "Arroz", "Fritas"],
             "tipo_opcionais": "gerais"}
        ],
        "Bebidas": [
            {"nome": "Suco de Laranja", "preco_base": 10.00, "ingredientes": ["Laranja", "Açúcar", "Gelo"],
             "tipo_opcionais": "bebidas"},
            {"nome": "Limonada Suíça", "preco_base": 12.00, "ingredientes": ["Limão", "Açúcar", "Gelo"],
             "tipo_opcionais": "bebidas"},
            {"nome": "Refrigerante Cola", "preco_base": 8.00,
             "ingredientes": ["Refrigerante", "Gelo", "Rodela de Limão"], "tipo_opcionais": "bebidas"},
            {"nome": "Caipirinha Clássica", "preco_base": 18.00, "ingredientes": ["Cachaça", "Limão", "Açúcar", "Gelo"],
             "tipo_opcionais": "bebidas"},
            {"nome": "Mojito", "preco_base": 22.00, "ingredientes": ["Rum", "Hortelã", "Limão", "Água com Gás", "Gelo"],
             "tipo_opcionais": "bebidas"},
            {"nome": "Milkshake de Morango", "preco_base": 16.00,
             "ingredientes": ["Sorvete", "Leite", "Calda", "Chantilly"], "tipo_opcionais": "bebidas"},
            {"nome": "Chá Gelado de Pêssego", "preco_base": 10.00,
             "ingredientes": ["Chá Preto", "Pêssego", "Açúcar", "Gelo"], "tipo_opcionais": "bebidas"},
            {"nome": "Café Expresso", "preco_base": 6.00, "ingredientes": ["Café", "Açúcar"],
             "tipo_opcionais": "bebidas"},
            {"nome": "Cappuccino", "preco_base": 14.00, "ingredientes": ["Café", "Leite", "Chocolate em Pó", "Canela"],
             "tipo_opcionais": "bebidas"},
            {"nome": "Piña Colada", "preco_base": 24.00,
             "ingredientes": ["Rum", "Suco de Abacaxi", "Leite de Coco", "Gelo"], "tipo_opcionais": "bebidas"}
        ],
        "Sobremesas": [
            {"nome": "Sorvete Sundae", "preco_base": 15.00, "ingredientes": ["Sorvete", "Calda", "Castanha", "Cereja"],
             "tipo_opcionais": "doces"},
            {"nome": "Petit Gâteau", "preco_base": 22.00,
             "ingredientes": ["Bolo Quente", "Sorvete", "Calda de Chocolate"], "tipo_opcionais": "doces"},
            {"nome": "Brownie com Nozes", "preco_base": 18.00, "ingredientes": ["Brownie", "Sorvete", "Nozes"],
             "tipo_opcionais": "doces"},
            {"nome": "Pudim de Leite", "preco_base": 12.00, "ingredientes": ["Pudim", "Calda de Caramelo"],
             "tipo_opcionais": "doces"},
            {"nome": "Torta de Limão", "preco_base": 14.00, "ingredientes": ["Massa", "Creme de Limão", "Merengue"],
             "tipo_opcionais": "doces"},
            {"nome": "Cheesecake", "preco_base": 19.00,
             "ingredientes": ["Massa de Biscoito", "Creme de Queijo", "Geleia de Morango"], "tipo_opcionais": "doces"},
            {"nome": "Salada de Frutas", "preco_base": 10.00,
             "ingredientes": ["Banana", "Maçã", "Mamão", "Laranja", "Leite Condensado"], "tipo_opcionais": "doces"},
            {"nome": "Açaí na Tigela", "preco_base": 20.00,
             "ingredientes": ["Açaí", "Banana", "Granola", "Leite em Pó"], "tipo_opcionais": "doces"},
            {"nome": "Mousse de Maracujá", "preco_base": 12.00, "ingredientes": ["Creme", "Sementes de Maracujá"],
             "tipo_opcionais": "doces"},
            {"nome": "Churros", "preco_base": 15.00,
             "ingredientes": ["Massa Frita", "Doce de Leite", "Açúcar", "Canela"], "tipo_opcionais": "doces"}
        ]
    }

    return cardapio, opcionais


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def calcular_preco(item_pedido, tabela_opcionais):
    preco = item_pedido["preco_base"]
    tipo = item_pedido["tipo_opcionais"]

    # Soma os adicionais
    for add in item_pedido["adicionais_escolhidos"]:
        preco += tabela_opcionais[tipo][add]

    # Subtrai as remoções
    preco -= (len(item_pedido["removidos"]) * DESCONTO_REMOCAO)

    return max(0, preco)


def exibir_resumo(item_pedido, tabela_opcionais):
    preco_final = calcular_preco(item_pedido, tabela_opcionais)
    resumo = f"{item_pedido['nome']} - R$ {preco_final:.2f}"

    if item_pedido["adicionais_escolhidos"]:
        resumo += f"\n  [+] Extras: {', '.join(item_pedido['adicionais_escolhidos'])}"
    if item_pedido["removidos"]:
        resumo += f"\n  [-] Sem: {', '.join(item_pedido['removidos'])}"

    return resumo


def personalizar_produto(item_pedido, tabela_opcionais):
    tipo = item_pedido["tipo_opcionais"]
    opcoes_disponiveis = tabela_opcionais[tipo]
    lista_opcionais = list(opcoes_disponiveis.keys())

    while True:
        limpar_tela()
        preco_atual = calcular_preco(item_pedido, tabela_opcionais)

        print(f"=== Personalizando: {item_pedido['nome']} ===")
        print(f"Preço Atual: R$ {preco_atual:.2f}")
        print(
            f"\nIngredientes Atuais: {', '.join(item_pedido['ingredientes']) if item_pedido['ingredientes'] else 'Nenhum'}")

        if item_pedido["adicionais_escolhidos"]:
            print(f"Adicionais Extras (+): {', '.join(item_pedido['adicionais_escolhidos'])}")
        if item_pedido["removidos"]:
            print(f"Removidos (-R$ {DESCONTO_REMOCAO:.2f}/cada): {', '.join(item_pedido['removidos'])}")

        print("\n[ 1 ] Adicionar Ingrediente Extra")
        print("[ 2 ] Retirar Ingrediente Padrão")
        print("[ 3 ] Confirmar e Adicionar ao Carrinho")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            print("\nOpções Adicionais:")
            for i, opt in enumerate(lista_opcionais, 1):
                print(f"{i}. {opt} (+ R$ {opcoes_disponiveis[opt]:.2f})")

            try:
                escolha = int(input("Digite o número do adicional (ou 0 para voltar): "))
                if 1 <= escolha <= len(lista_opcionais):
                    item_pedido["adicionais_escolhidos"].append(lista_opcionais[escolha - 1])
            except ValueError:
                pass

        elif opcao == '2':
            if not item_pedido["ingredientes"]:
                input("\nNão há mais ingredientes para remover! Pressione ENTER...")
                continue

            print("\nIngredientes Atuais (Remover):")
            for i, ing in enumerate(item_pedido["ingredientes"], 1):
                print(f"{i}. {ing}")

            try:
                escolha = int(input("Digite o número do ingrediente a retirar (ou 0 para voltar): "))
                if 1 <= escolha <= len(item_pedido["ingredientes"]):
                    removido = item_pedido["ingredientes"].pop(escolha - 1)
                    item_pedido["removidos"].append(removido)
            except ValueError:
                pass

        elif opcao == '3':
            return item_pedido
        else:
            print("Opção inválida.")


def main():
    cardapio, tabela_opcionais = inicializar_dados()
    carrinho = []

    while True:
        limpar_tela()
        print("====== CARDÁPIO DIGITAL ======")
        print("1. Pratos")
        print("2. Bebidas")
        print("3. Sobremesas")
        print("4. Ver Carrinho e Finalizar")
        print("0. Sair")

        opcao = input("\nEscolha uma categoria: ")

        categoria_atual = None
        if opcao == '1':
            categoria_atual = "Pratos"
        elif opcao == '2':
            categoria_atual = "Bebidas"
        elif opcao == '3':
            categoria_atual = "Sobremesas"

        elif opcao == '4':
            limpar_tela()
            print("=== SEU CARRINHO ===")
            total = 0
            if not carrinho:
                print("Carrinho vazio!")
            else:
                for i, item in enumerate(carrinho, 1):
                    print(f"\n{i}. {exibir_resumo(item, tabela_opcionais)}")
                    total += calcular_preco(item, tabela_opcionais)
                print(f"\nTotal do Pedido: R$ {total:.2f}")
            input("\nPressione ENTER para voltar...")
            continue

        elif opcao == '0':
            print("Saindo... Obrigado pela preferência!")
            break
        else:
            continue

        # Listagem da categoria escolhida
        limpar_tela()
        print(f"=== {categoria_atual.upper()} ===")
        itens_categoria = cardapio[categoria_atual]

        for i, item in enumerate(itens_categoria, 1):
            print(f"[{i}] {item['nome']} - R$ {item['preco_base']:.2f}")
        print("[0] Voltar")

        try:
            escolha_item = int(input("\nDigite o número do item que deseja: "))
            if 1 <= escolha_item <= len(itens_categoria):
                item_original = itens_categoria[escolha_item - 1]

                # Cria um novo dicionário (pedido) copiando os dados base
                novo_pedido = {
                    "nome": item_original["nome"],
                    "preco_base": item_original["preco_base"],
                    "tipo_opcionais": item_original["tipo_opcionais"],
                    "ingredientes": item_original["ingredientes"].copy(),  # Importante para não alterar o original
                    "adicionais_escolhidos": [],
                    "removidos": []
                }

                # Abre a tela de personalização para esse pedido
                novo_pedido = personalizar_produto(novo_pedido, tabela_opcionais)
                carrinho.append(novo_pedido)
                print(f"\n{novo_pedido['nome']} adicionado ao carrinho com sucesso!")
                input("Pressione ENTER para continuar...")
        except ValueError:
            print("Entrada inválida.")


if __name__ == "__main__":
    main()