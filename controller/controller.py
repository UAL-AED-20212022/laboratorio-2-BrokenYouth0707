from model.LinkedList import LinkedList

def criar_linked_list():
    return LinkedList()

def registar_país_no_inicio(lista, nome_de_país):
    lista.insert_at_start(nome_de_país)

def registar_país_no_fim(lista, nome_de_país):
    lista.insert_at_end(nome_de_país)

def registar_país_depois_de_outro(lista, novo_país, position):
    lista.insert_after_item(position, novo_país)

def registar_país_antes_de_outro(lista, novo_país, position):
    lista.insert_before_item(position, novo_país)

def registar_país_numa_posicao(lista, nome_de_país, index: int):
    lista.insert_at_index(index, nome_de_país)

def numero_de_países_na_lista(lista):
    return lista.get_count()

def verificar_se_o_país_existe_na_lista(lista, nome_de_país):
    return lista.search_item(nome_de_país)

def eliminar_primeiro_país_da_lista(lista): 
    nome_do_país = lista.start_node.item    #Devolve o primeiro elemento da lista de paises
    lista.delete_at_start()
    return nome_do_país

def eliminar_ultimo_país_da_lista(lista):
    nome_do_país = lista.get_last_node()    #Devolve o ultimo elemento da lista de paises
    lista.delete_at_end()
    return nome_do_país

def eliminar_país(lista, nome_de_país):
    existe = lista.search_item(nome_de_país)    #Verifica se o país indicado está na lista
    if existe: 
        lista.delete_element_by_value(nome_de_país)
    return existe