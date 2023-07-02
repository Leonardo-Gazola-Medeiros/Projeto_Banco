import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDEPOSITO
    [s]\tSACAR
    [e]\tEXTRATO
    [nc]\tNOVA CONTA
    [lc]\tLISTAR CONTAS
    [nu]\tNOVO USUARIO
    [q]\tSAIR
    => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
        if valor > 0:
             saldo += valor
             extrato += f"Depósito:\tR$ {valor:.2f}\n"
             print("\n=== Depósito Realizado Com Sucesso! ===")
        else:
             print("\n--- Operação Falhou ---")
        return saldo,extrato;
    
def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques >= limite_saques

     if excedeu_saldo:
          print("--- Voce não tem saldo suficiente. ---")
     elif excedeu_limite:
          print("--- A quantia excedeu o limite de R${limite}. ---")
     elif excedeu_saques:
          print("--- Voce excedeu o limite de saques diários. ---")
     elif valor > 0:
          saldo -= valor
          extrato += f"Saque:\t\tR${valor:.2f}\n"
          numero_saques += 1
          print("\n=== Saque Realizado Com Sucesso! ===")
     else:
          print("\n--- Operação Falhou, O valor informado é inválido! ---")
     
     return saldo, extrato;

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================");

def criar_usuario(usuarios):
        cpf = input("Informe o CPF (Somente Numeros!)")
        usuario = filtrar_usuario(cpf,usuarios)

        if usuario:
              print("Já existe um usuário cadastrado com essas informações")
              return
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf":cpf,"endereço":endereco})

        print("Usuário Cadastrado com Sucesso!");

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def filtrar_usuario(cpf, usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario[cpf] == cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None;

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agência:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha));

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
             valor = float(input("Informe o valor do Depósito: "))

             saldo, extrato = deposito(saldo,valor,extrato)

        elif opcao == "s":
             valor = float(input("Informe o valor do Saque: "))

             saldo,extrato = saque(
                  saldo = saldo,
                  valor = valor,
                  extrato = extrato,
                  limite = limite,
                  numero_saques = numero_saques,
                  limite_saques = LIMITE_SAQUE)
             
              
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
              
        elif opcao == "nu":
             criar_usuario(usuarios)
             
              
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
             listar_contas(contas)

        elif opcao == "q":
             break
        
main()
              

        