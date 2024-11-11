class Loja:
    def __init__(self, local):
        self.local = local
        self.funcionarios = []
        self.estoque = []
        self.loja_proxima = None

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)
        funcionario.loja = self

    def demitir(self, funcionario):
        self.funcionarios.remove(funcionario)
        funcionario.loja = None

    def adicionar_estoque(self, instrumento):
        self.estoque.append(instrumento)

    def remover_estoque(self):
        self.estoque.pop

    def consultar_instrumentos(self):
        estoque = {"GUITARRA": 0, "BAIXO": 0, "VIOLÃO": 0}
        for instrumento in self.estoque:
            if isinstance(instrumento, Guitarra):
                estoque["GUITARRA"]+= 1
            elif isinstance(instrumento, Baixo):
                estoque["BAIXO"]+= 1  
            elif isinstance(instrumento, Violão):
                estoque["VIOLÃO"]+= 1  
        print(estoque)
        return


    
    def consultar_funcionarios(self):
        cargos = {}
        funcionarios = self.funcionarios
        for func in funcionarios:
            cargos[f"{func.cargo}"] = 0
        
        for func in funcionarios:
            cargos[f"{func.cargo}"] += 1 
        
        print(cargos)
        
    
    def definir_loja_proxima(self , loja):
        self.loja_proxima = loja
    

class Funcionario:
    def __init__(self, nome, documento, salario, cargo, loja):
        self.nome = nome
        self.documento = documento 
        self.salario = salario 
        self.cargo = cargo
        self.loja = loja

    def mudar_loja(self, nova_loja):
        self.loja = nova_loja

    

    
class Instrumento:
    def __init__(self, marca, modelo, preco, num_cordas, loja):
        self._marca = marca
        self._modelo = modelo
        self.preco = preco
        self._num_cordas = num_cordas
        self._loja = loja
    
    @property
    def loja(self):
        return self._loja
    
    @loja.setter
    def loja(self, loja):
        self._loja = loja

    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def num_cordas(self):
        return self._num_cordas
    
    @num_cordas.setter
    def num_cordas(self, num_cordas):
        self._num_cordas = num_cordas

    

class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, captador, amplificador):
        super().__init__(self, marca, preco, modelo, num_cordas)
    
        self.captador = captador
        self.amplificador = amplificador


class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, escala):
        super().__init__(self, marca, modelo, preco, num_cordas)
    
        self.escala = escala

class Violão(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, tipo_madeira):
        super().__init__(self, marca, modelo, preco, num_cordas)
    
        self.tipo_madeira = tipo_madeira
