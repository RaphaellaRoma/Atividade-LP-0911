from franquia_de_lojas import *


impostor = Loja("Tijuca")

funcionario_a = Funcionario("Bianca", "000.000.000.00", "200,00","vendedor", None)

impostor.contratar(funcionario_a)

violao_a = Violão("Kotsuba", "S3O", "39,90","200", "betula")

impostor.adicionar_estoque(violao_a)

print(impostor.consultar_funcionarios())
print(impostor.consultar_instrumentos())


