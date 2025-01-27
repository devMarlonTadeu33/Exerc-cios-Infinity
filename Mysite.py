'''
Ex01. Faça um site com o streamlit de curriculo! O seu site deve conter os tópicos:

- Apresentação (Uma imagem sua e um texto de apresentação)
- Habilidades (Uma lista não ordenada)
- Experiências Profissionais (Uma lista ordenada)

'''



import streamlit as st

st.title('Meu currículo!')

st.write()
url_infinity = 'https://infinityschool.com.br/'
url_link_markdown = 'https://github.com/devMarlonTadeu33'

url_imagem = 'https://i.pinimg.com/736x/52/c5/6a/52c56a66bb6d790fe6bb4afd5d55d112.jpg'
st.image(url_imagem, caption= 'Minha imagem de perfil', width= 250)

f'''

##  Sobre mim
Meu nome é Marlon Tadeu, tenho 21 anos de idade e atualmente resido em Santa Luzia - MG.
Atualmente estou cursando desenvolvimento fullstack na [Infinity School]({url_infinity})

> Clique [aqui]({url_link_markdown}) para visitar meu perfil do github!



## Habilidades:

- Python iniciante
- 
-


'''