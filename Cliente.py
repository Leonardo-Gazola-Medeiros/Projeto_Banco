class Cliente:
    def __init__(self, nome, saldo_inicial = 0, saques_diarios = 0):
        self.nome = nome;
        self.saldo = saldo_inicial;

    def deposito(self, valor):
        self.saldo += valor;
        print(f"{self.nome}, foi adicionado R${valor} à sua conta.");
    
    def saque(self, valor):
        if(saques_diarios >= 3):
            print(f"{self.nome}, você já ultrapassou os limites de 3 saques diários. Espere até o próximo dia para poder realizar novos saques");
        elif(self.valor > 500):
            print(f"{self.nome}, o valor de saque pedido é maior do que o limite máximo por operação (R$500,00).");
        else:
            saques_diarios += 1;
            self.saldo -= valor;
            print(f"{self.nome}, foram sacados R${valor} de sua conta.");



    def extrato(self):
        print(f"{self.nome}, você possui R${valor} em sua conta.");