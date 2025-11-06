import streamlit as st

#--------------------------------------------------------SIDEBAR
st.sidebar.image('logo.png')
st.sidebar.title('SAÚDE EM PRIMEIRO LUGAR!')


nome = st.sidebar.text_input('Digite seu nome: ')
idade = st.sidebar.text_input('Digite sua idade: ')
peso = st.sidebar.text_input('Digite seu peso: ')
altura = st.sidebar.text_input('Digite sua altuta: ')

#-------------------------------------------------------PRINCIPAL
st.title('CUIDE DA SUA SAUDE')

('f | Faixa de IMC        | Classificação                  |')
('|---------------------|-------------------------------|')
('| < 18.5              | Abaixo do peso                 |')
('| 18.5 – 24.9         | Peso normal                    |')
('| 25.0 – 29.9         | Sobrepeso                      |')
('| 30.0 – 34.9         | Obesidade Grau I               |')
('| 35.0 – 39.9         | Obesidade Grau II              |')
('| ≥ 40.0              | Obesidade Grau III (mórbida)   |')

if st.sidebar.button ('Calcular'):


    peso= float(peso)
    altura= float(altura)

    imc = peso / (altura**2)
    st.metric('IMC', imc )


    if imc <=18.5:
        print(f' {nome}Você está abaixo do peso. É importante cuida da sua sáude! :) ')
    elif imc<=24.9:
        st.write (f' {nome} Vocé está dentro do normal. continue assim :)')
    elif imc<=29.9:
        st.write (f' {nome} Vocé está sobrepeso. vai fazer uma dieta :(   )')
    elif imc <=34.9:
        st.write (f' {nome} Vocé esta no grau  I de obesidade . cuide disso antes que seja tarde.    ')
    elif imc<=39.9:
        st.write(f' {nome} Seu resultado indica que vocé esta no grau II. Melhor procurar ajuda. :(   )')
    else:
        st.write(f' {nome} Seu resultado fala que vocé esta no grau III. Proucure um medico urgente!!')
