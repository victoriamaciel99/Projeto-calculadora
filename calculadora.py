nome_usuario = input("Por favor, insira seu nome:")
print(f"Olá, {nome_usuario}!")
idade_usuario = int(input("Por favor, insira sua idade:"))
if idade_usuario >=18:
  print("Você é maior de idade.")
else:
  print("Você é menor de idade.")
renda_usuario = float(input("Por favor, insira sua renda (exemplo: 1800.15): ").replace('.', '').replace(',','.'))
print(renda_usuario-50000)
print(renda_usuario/300)
print(renda_usuario%3)
print(renda_usuario*3)

Por favor, insira seu nome:Victoria
Olá, Victoria!
Por favor, insira sua idade:27
Você é maior de idade.
Por favor, insira sua renda (exemplo: 1800.15): 2135.56
163556.0
711.8533333333334
1.0
640668.0
