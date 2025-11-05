import os  

builds_registradas = []

MENU_ART = """
⢸⢿⠀⠀⠀⠀⢸⢯⡿⡹⠟⠆⠀⠀⠀⣻⣿⢷⠀⠀⠀⣠⣴⣾⡟⣿⣳⣦⡀⠀⣟⡇⠀⠀⠀⣿⣻⠀⣿⣻⡽⠏⠟⠀⠀⠀⠀⠀⠀⠀
⢸⣻⠀⠀⠀⠀⢸⢯⣇⣀⣀⡀⠀⠀⣰⢿⠟⣟⣧⠀⢰⡿⡝⠁⠀⠀⠈⠓⠉⠀⣿⡅⠀⠀⠀⡷⣯⠀⡷⣇⣀⣀⡀ ⢀⣴⠶⢦⡀⣶⠲
⢸⣹⠀⠀⠀⠀⢸⡿⡾⠿⠿⠀⠀⢀⣿⡏⠀⢸⡿⡆⢸⣿⡀⠀⣰⣿⣿⣿⢿⠇⣿⡶⠀⠀⠀⣿⣹⠰⣿⣹⠿⠿⠇⢸⣇⠀⢸⡇⣿⠷
⢸⣽⣀⣀⣀⣀⢸⣻⣇⣀⣀⡀⠀⣼⣷⠿⠿⠿⢿⣳⡘⢷⡷⣄⡀⢀⣠⣯⡿⠀⢿⣽⣄⠀⣠⣟⡟⢘⡷⣇⣀⣀⣀⠙⠛⠋⠀⠛⠀
⠜⠾⠝⠯⠟⠃⠸⠷⠫⠟⠽⠃⠼⠻⠃⠀⠀⠀⠈⠿⠳⠈⠙⠳⠿⠯⠗⠋⠀⠀⠈⠛⠾⠿⠽⠚⠁⠈⠿⠹⠏⠟⠿⠀⠀⠀⠀⠀⠀⠀
⢠⣤⠀⠀⠀⠀⢠⣤⡤⣤⢤⡄⠀⠀⣠⣤⣤⣤⣄⡀⠀⢠⣤⣤⢤⡤⣴⢢⡤⣤⠀⠀⠀⢰⣤⡄⢠⣤⡤⣤⣤⣀⠀⠀⠀⣠⣤⣤⣤⡀
⢸⣳⠀⠀⠀⠀⢸⡷⡏⠉⠉⠁⣠⡿⡿⠋⠉⠙⢺⠿⠆⢸⣯⡏⠉⠉⠉⢸⡽⣯⣷⡄⠀⢸⣟⡇⢸⡷⡏⠉⠓⢟⣷⡄⣾⢿⡋⠉⠻⠛
⢸⣹⠀⠀⠀⠀⢸⡿⣷⣶⣶⠇⣿⣹⠀⠀⢀⣀⣆⣀⣰⢸⣷⣷⣶⣶⡇⢸⣹⡇⢿⣹⡆⢸⣏⡇⢸⡿⡇⠀⠀⠈⣿⣷⠹⣏⡿⣶⣆⡀
⢸⣽⠀⠀⠀⠀⢸⡽⡏⠉⠉⠀⢿⡽⡄⠀⠛⠛⢛⡿⡿⢸⡷⡏⠉⠉⠀⢸⡷⡇⠀⠻⣽⢾⣯⡇⢸⡿⡅⠀⠀⣰⣿⡏⠀⠈⠉⠓⢿⣻
⢸⣞⡶⣖⡶⡖⢸⣻⣗⣶⣲⡆⠈⠻⣽⣳⣶⣶⣻⠝⠁⢸⣟⣷⣲⢶⣶⢸⣟⡇⠀⠀⠘⢿⣞⡇⢸⣽⢳⣖⣿⠽⠊⠀⠺⣿⣶⡴⣞⠗
"""
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
   
    limpar_tela()
    print(MENU_ART)
    print("╔═══════════════════════════════════╗")
    print("║      REGISTRADOR DE BUILDS v1.0   ║")
    print("╚═══════════════════════════════════╝")
    print("1. Registrar Nova Build")
    print("2. Ver Builds Registradas")
    print("3. Sair")
    print("===================================")
    return input("Escolha uma opção: ")

def registrar_build():
    limpar_tela()
    print("--- Novo Registro de Build ---")
    
    boneco = input("Digite o nome do Boneco (Campeão): ")
    runas = input("Digite as Runas (ex: Conquistador + Inspiração): ")
    
    itens = []
    print("Digite os 6 itens (deixe em branco para parar):")
    for i in range(6):
        item = input(f"  Item {i+1}: ")
        if not item:  
            break
        itens.append(item)
    
    nova_build = {
        "boneco": boneco,
        "runas": runas,
        "itens": itens
    }
    
    builds_registradas.append(nova_build)
    
    print("\n*** Build registrada com sucesso! ***")

def ver_builds():
    limpar_tela()
    print("--- Builds Registradas ---")

    print("# ----------------------------------------")
    print("# TODO: LÓGICA DO BANCO DE DADOS (SELECT)")
    print("# Aqui, em vez de ler da lista 'builds_registradas',")
    print("# fazer um SELECT no banco para carregar os dados.")
    print("# Ex: 'SELECT * FROM tabela_build JOIN (gastão que ensinou)...'")
    print("# ----------------------------------------\n")
    
    if not builds_registradas:
        print("Nenhuma build registrada ainda.")
    else:
        for i, build in enumerate(builds_registradas):
            print(f"\n--- Build #{i+1} ---")
            print(f"  Boneco: {build['boneco']}")
            print(f"  Runas:  {build['runas']}")
            
            itens_formatados = ', '.join(build['itens']) if build['itens'] else 'Nenhum'
            print(f"  Itens:  {itens_formatados}")
            print("-----------------")
            
    input("\nPressione Enter para voltar ao menu...")

def main():
    while True:
        opcao = mostrar_menu()
        
        if opcao == '1':
            registrar_build()
        elif opcao == '2':
            ver_builds()
        elif opcao == '3':
            limpar_tela()
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()