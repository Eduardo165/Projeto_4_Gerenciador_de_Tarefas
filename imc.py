
print('|-----------------------------------------------------|')
print('|                 CUIDE DA SUA SAÚDE!                 |')
print('|-----------------------------------------------------|')
print('| Faixa de IMC       | Classificação                  |')
print('|--------------------|--------------------------------|')
print('| < 18.5             | Abaixo do peso                 |')
print('| 18.5  24.9         | Peso normal                    |')
print('| 25.0  29.9         | Sobrepeso                      |')
print('| 30.0  34.9         | Obesidade Grau I               |')
print('| 35.0  39.9         | Obesidade Grau II              |')
print('| ≥ 40.0             | Obesidade Grau III (mórbida)   |')
print('|-----------------------------------------------------|')

nome =input('Qual é o seu nome:  ')
int(input('Qual a sua idade: '))
peso = float(input('Qual é seu peso: '))
altura = float(input('Qual é sua altura: '))


imc = peso/(altura**2)


if imc <=18.5:
    print(f' {nome}Você está abaixo do peso. É importante cuida da sua sáude! :) ')
elif imc<=24.9:
    print(f' {nome} Vocé está dentro do normal. continue assim :)')
elif imc<=29.9:
    print(f' {nome} Vocé está sobrepeso. vai fazer uma dieta :(   )')
elif imc <=34.9:
    print(f' {nome} Vocé esta no grau  I de obesidade . cuide disso antes que seja tarde.    ')
elif imc<=39.9:
    print(f' {nome} Seu resultado indica que vocé esta no grau II. Melhor procurar ajuda. :(   )')
else:
    print(f' {nome} Seu resultado fala que vocé esta no grau III. Proucure um medico urgente!!')





