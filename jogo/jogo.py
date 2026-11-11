import random

# 1. Apresentação do título e inicialização do jogador (Dicionário)
print("=========================================")
print("      SIMULADOR DE BATALHA RPG           ")
print("=========================================")

jogador = {
    "vida": 300,
    "ataque": 20,
    "pocoes": 2,
    "pontos": 0
}

# 2. Tipos de inimigos disponíveis (Lista de dicionários)
tipos_inimigos = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500}
]

# 3. Seleção aleatória de 3 a 5 inimigos (cópia para não alterar o modelo base)
quantidade_inimigos = random.randint(3, 5)
inimigos_batalha = []

for _ in range(quantidade_inimigos):
    modelo = random.choice(tipos_inimigos)
    inimigos_batalha.append(modelo.copy())

total_inimigos = len(inimigos_batalha)
fugiu = False

print(f"\nSurgiram {total_inimigos} inimigos para a batalha!")

# 4. Ciclo principal do jogo
while jogador["vida"] > 0:
    # Filtrar apenas os inimigos que ainda estão vivos
    inimigos_vivos = [inimigo for inimigo in inimigos_batalha if inimigo["vida"] > 0]
    
    # Verificar condição de vitória
    if len(inimigos_vivos) == 0:
        break

    print("\n========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")
    
    opcao = input("Escolha uma opção: ").strip()

    # Opção 1 — Atacar inimigo
    if opcao == "1":
        print("\n--- Inimigos Vivos ---")
        for i, inimigo in enumerate(inimigos_vivos, start=1):
            print(f"{i}. {inimigo['nome']} (Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']})")
        
        try:
            escolha = int(input("Escolha o número do inimigo a atacar: "))
            if 1 <= escolha <= len(inimigos_vivos):
                alvo = inimigos_vivos[escolha - 1]
                
                # Dano do jogador entre 10 e 20
                dano_jogador = random.randint(10, 20)
                alvo["vida"] = max(0, alvo["vida"] - dano_jogador)
                print(f"\nAtacaste o {alvo['nome']} e causaste {dano_jogador} de dano!")
                
                # Verificar se o inimigo foi derrotado ou se contra-ataca
                if alvo["vida"] == 0:
                    jogador["pontos"] += alvo["pontos"]
                    print(f"Derrotaste o {alvo['nome']}! Ganhaste {alvo['pontos']} pontos.")
                else:
                    dano_inimigo = random.randint(5, alvo["ataque"])
                    jogador["vida"] = max(0, jogador["vida"] - dano_inimigo)
                    print(f"O {alvo['nome']} sobreviveu com {alvo['vida']} de vida e contra-atacou!")
                    print(f"Sofreste {dano_inimigo} de dano. Vida atual: {jogador['vida']}")
            else:
                print("Erro: Número de inimigo inválido. Escolha dentro da lista apresentada.")
        except ValueError:
            print("Erro: Por favor, introduza um número válido.")

    # Opção 2 — Consultar estado do jogador
    elif opcao == "2":
        derrotados = total_inimigos - len(inimigos_vivos)
        print("\n--- Estado do Jogador ---")
        print(f"Vida atual: {jogador['vida']}")
        print(f"Pontuação: {jogador['pontos']}")
        print(f"Inimigos derrotados: {derrotados}")
        print(f"Inimigos ainda vivos: {len(inimigos_vivos)}")
        print(f"Poções disponíveis: {jogador['pocoes']}")

    # Opção 3 — Listar inimigos vivos
    elif opcao == "3":
        print("\n--- Inimigos Ativos ---")
        if len(inimigos_vivos) == 0:
            print("Não existem inimigos vivos.")
        else:
            for inimigo in inimigos_vivos:
                print(f"- {inimigo['nome']}: {inimigo['vida']} de vida | {inimigo['ataque']} de ataque")

    # Opção 4 — Usar poção de cura
    elif opcao == "4":
        # Nota: O enunciado especifica o limite máximo de 100 pontos para a cura
        if jogador["pocoes"] <= 0:
            print("\nNão tens poções de cura disponíveis!")
        elif jogador["vida"] >= 100:
            print("\nNão podes usar poção porque já tens 100 ou mais pontos de vida!")
        else:
            jogador["pocoes"] -= 1
            vida_antes = jogador["vida"]
            jogador["vida"] = min(100, jogador["vida"] + 25)
            recuperado = jogador["vida"] - vida_antes
            print(f"\nUsaste uma poção e recuperaste {recuperado} pontos de vida!")
            print(f"Vida atual: {jogador['vida']} | Poções restantes: {jogador['pocoes']}")

    # Opção 5 — Fugir / terminar jogo
    elif opcao == "5":
        fugiu = True
        break

    # Validação de opção inválida no menu
    else:
        print("\nErro: Opção inexistente. Por favor, escolha entre 1 e 5.")

# 5. Condições de fim do jogo e mensagens finais
print("\n=========================================")
if fugiu:
    print("RESULTADO: FUGA")
    print("Partida terminada por fuga. Não obtiveste a vitória.")
elif jogador["vida"] <= 0:
    print("RESULTADO: DERROTA")
    print("Foste derrotado pelos inimigos!")
else:
    print("RESULTADO: VITÓRIA")
    print("Parabéns! Derrotaste todos os inimigos!")

print(f"Pontuação final: {jogador['pontos']} pontos")
print("=========================================")
