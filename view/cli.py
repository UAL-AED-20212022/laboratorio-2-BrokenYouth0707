from controller import controller as controller

def cli():
    
    lista = controller.criar_linked_list()

    while True:
        
        try:
        
            menu = input().split()
            menu[0] = menu[0].upper()
            país = menu[1:]
            l = len(menu)

            if menu[0] == "RPI" and l == 2:
                registar_I(lista, país)
            
            elif menu[0] == "RPF" and l == 2:
                registar_F(lista, país)

            elif menu[0] == "RPDE" and l == 3:
                registar_D(lista, país)
            
            elif menu[0] == "RPAE" and l == 3: 
                registar_A(lista, país)

            elif menu[0] == "RPII" and l == 3:
                regisar_I(lista, país)
             
            elif menu[0] == "VNE" and l == 1:
                tamanho_da_lista(lista, país)
            
            elif menu[0] == "VP" and l == 2:
                verificar_país(lista, país)
            
            elif menu[0] == "EPE" and l == 1:
                eliminar_primeiro(lista)
            
            elif menu[0] == "EUE" and l == 1: 
                eliminar_ultimo(lista)
            
            elif menu[0] == "EP" and l == 2:
                eliminar(lista, país)
            else:
                print("Faltam argumentos")
        
        except EOFError: 
            break

def registar_I(lista, país):
    controller.registar_país_no_inicio(lista, nome_de_país = país[0])
    lista.traverse_list()

def registar_F(lista, país):
    controller.registar_país_no_fim(lista, nome_de_país = país[0])
    lista.traverse_list()

def registar_D(lista, país):
    controller.registar_país_depois_de_outro(lista, novo_país = país[0], position = país[1])
    lista.traverse_list()

def registar_A(lista, país):
    controller.registar_país_antes_de_outro(lista, novo_país = país[0], position = país[1])
    lista.traverse_list()

def regisar_I(lista, país):
    controller.registar_país_numa_posicao(lista, nome_de_país = país[0], index = int(país[1]))
    lista.traverse_list()

def tamanho_da_lista(lista, país):
    tamanho = controller.numero_de_países_na_lista(lista)
    print(f"O número de elementos são {tamanho}.")

def verificar_país(lista, país):
    nome_de_país = país[0]
    nome = controller.verificar_se_o_país_existe_na_lista(lista, nome_de_país)
    if nome == True: 
        print(f"O país {nome_de_país} encontra-se na lista.")
    else: 
        print(f"O país {nome_de_país} não se encontra na lista.")

def eliminar_primeiro(lista):
    nome_de_país = controller.eliminar_primeiro_país_da_lista(lista)
    if nome_de_país: 
        print(f"O país {nome_de_país} foi eliminado da lista.")

def eliminar_ultimo(lista):
    nome_de_país = controller.eliminar_ultimo_país_da_lista(lista)
    if nome_de_país: 
        print(f"O país {nome_de_país} foi eliminado da lista.")

def eliminar(lista, país):
    nome_de_país = país[0]
    nome = controller.eliminar_país(lista, nome_de_país)
    if nome: 
        print(f"O país {nome_de_país} foi eliminado da lista.")
    else: 
        print(f"O país {nome_de_país} não se encontra na lista.")