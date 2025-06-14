#Coletar dados de um produto

print("---Coleta de dados---")
nome = input("Nome do produto: ")
cargo = input("Qual o seu cargo? ")
empresa = input("Em que empresa você trabalha? ")
Salário = int(input("Informe o seu salário (Utilize apenas números): R$"))
tempo = input("Há quanto tempo você trabalha na empresa? (Utilize apenas números) ")

print("---Suas informações---")
print(f"Nome: {nome}")
print(f"Cargo: {cargo}")
print(f"Empresa: {empresa}")
print(f"Salário: R${Salário}")
print(f"Tempo de trabalho: {tempo} anos")