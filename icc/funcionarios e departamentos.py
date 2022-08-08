def meusFunc(nomeDepto, depto, func, funcXdepto):
    # lista q vai receber o nome dos funcionarios
    lista = []

    # pegamos o index da lista onde possui o numero do departamento
    codDepartamento = depto.index(str(nomeDepto))

    # compara o codigo do departamento com o codigo do departamento q os funcionarios pertencem
    for i in range(len(funcXdepto)):
        # se o codigo do deprtamento do funcionario for igual ao do deprtamento chamado salva o nome do cliente
        if funcXdepto[i] == codDepartamento:
            lista.append(func[i])

    return lista

def meuDepto(nomeFunc, depto, func, funcXdepto):
    #  pegamos o codigo do funcionario
    codFuncionario = func.index(nomeFunc)
    #  pegamos o codigo do deprtamento que o funcionario pertence
    codDepartamento = funcXdepto[codFuncionario]

    # retorna o nome do deprtamento
    return depto[codDepartamento]

# Programa principal
depto = ['Vendas', 'Compras', 'RH', 'TI', 'Marketing']    
func = ['João', 'Paulo', 'Clara', 'Eduardo', 'Ana', 'Jorge', 'Augusto', 'Pedro', 'Roberto', 'Manoel',
        'Luís', 'Inácio', 'Dino', 'Flávio', 'Ciro', 'Fernando', 'Leonel']
funcXdepto = [1, 1, 4, 3, 0, 0, 1, 1, 1, 2, 0, 3, 4, 3, 2, 3, 2]

nomeDepto = input() # Lê o nome do departamento a pesquisar os funcionários
nome = input() # Lê o nome do funcionário a pesquisar o departamento

# .strip tira o espaço em branco depois do nome (tem um erro no do professor)
print(meusFunc(nomeDepto.strip(), depto, func, funcXdepto))
print(meuDepto(nome, depto, func, funcXdepto))