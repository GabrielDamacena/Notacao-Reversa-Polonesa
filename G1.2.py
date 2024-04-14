class Notacao_Reversa_Polonesa:
    def __init__(self,Lista):
        self.numeros = []
        self.operadores = []
        self.Lista = Lista
        self.dic_Numeros ={}
        self.dic_Operadores = {}
        self.equacao_remontada = []
        self.resul_equacao = []
    def Desmontar(self):
        cont = 0
        lixo=[]
        for n in self.Lista:
            cont+=1
            self.dic_Numeros[cont]=n.split()
            for i in n:
                    if i == '+' or i == '-' or i == '*' or i == '/' or i == '^' or i == '(' or i == ')':
                        self.operadores.append(i)
                    elif i == " ":
                        lixo.append(i)
                    else:
                        self.numeros.append(i)

        return  self.numeros, self.operadores

    def  Montar_Equacao(self):
        for n in self.dic_Numeros:
            nova = "".join(self.dic_Numeros[n])
            self.equacao_remontada.append(nova)

        return self.equacao_remontada

    def Calcular_Equacao(self):
        conte = 0
        while len(self.dic_Numeros) != 0:
            conte+=1
            num=[]
            op=[]
            count=0
            for i in self.dic_Numeros:
                for n in self.dic_Numeros[i]:
                    count += 1
                    if count >= 6:
                        break
                    elif n.isdigit():
                        num.append(n)
                    elif n == '+' or n == '-' or n == '*' or n == '/' or n == '^':
                        op.append(n)
            if len(num) >=3:
                n1 = float(num.pop())
                n2 = float(num.pop())
                n3 = float(num.pop())
            elif len(num) <3:
                n1 = float(num.pop())
                n2 = float(num.pop())
            else:
                break

            for i in op:
                if i == "^":
                    final1 = n1 ** n2
                    self.resul_equacao.append(final1)
                elif i == "*" or i== "/":
                    if i == "*":
                        r = n1 * n2
                    elif i == "/":
                        final2 = r / n3
                        self.resul_equacao.append(final2)
                elif i == "+" or i == "-":
                    if i == "-":
                        r = n1 - n2
                    elif i == "+":
                        final3 = r + n3
                        self.resul_equacao.append(final3)
            self.dic_Numeros.pop(conte)

        return self.resul_equacao
def Start():
    if __name__ == "__main__":
        lista = ["10 - 5 + 2","8 * 6 / 2"," 2 + 3  * 4 ", "2 ^ 3"]
        notacao = Notacao_Reversa_Polonesa(lista)
        print(notacao.Desmontar())
        print(notacao.Montar_Equacao())
        print(notacao.Calcular_Equacao())

Start()




