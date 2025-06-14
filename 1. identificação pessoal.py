#Coletar e exibir informações básicas sobre uma pessoa

print("---Coleta de dados---")
nome = input("Nome completo: ")
idade = int(input("Idade: "))
cidade = input("Em que cidade você mora? ")
profissão = input("Qual a sua profissão? ")
hobby = input("Descreva um hobby ou atividade que você gosta de fazer: ")

print("---Suas informações---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissão}")
print(f"Hobby: {hobby}")