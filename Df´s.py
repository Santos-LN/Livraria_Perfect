import pandas as pd
from tabulate import tabulate

df_autores = pd.DataFrame({
    'id_autor':[1,2,3,4,5,6,7],
    'Nome':['Bernard Cornwell','Conn Iggulden','George R. R. Martin','John Grisham','Dale Carnegie','Napoleon Hill','Gabriel G Márquez'],
    'Nacionalidade':['Britânico','Britânico','Americano ','Americano','Americano','Americano ','Colombiano '],
    'Idade': [81,54,78,70,66,87,87]
})

novo_autor = {
    'id_autor': 9,
    'Nome': 'J. K. Rowling',
    'Nacionalidade': 'Britânico',
    'Idade': 59
}

df_autores = pd.concat([df_autores,pd.DataFrame([novo_autor])],ignore_index=True)

df_obras = pd.DataFrame({
    'id_livro': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'Título': [
        'O Último Reino', 'O Águia de Sharpe',
        'Genghis: O Nascimento de um Império', 'O Livro Perigoso para Garotos',
        'A Guerra dos Tronos', 'A Fúria dos Reis',
        'O Poderoso Chefão', 'O Siciliano',
        'A Firma', 'Tempo de Matar',
        'Como Fazer Amigos e Influenciar Pessoas', 'Como Evitar Preocupações e Começar a Viver',
        'Quem Pensa Enriquece', 'Atitude Mental Positiva: Caminho para o Sucesso',
        'Cem Anos de Solidão', 'O Amor nos Tempos do Cólera'
    ],
    'id_autor': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],
    'Arrecadado': [
        5000000, 3000000,    # Bernard Cornwell
        4000000, 2500000,    # Conn Iggulden
        120000000, 80000000, # George R. R. Martin
        150000000, 30000000, # Mario Puzo 
        100000000, 60000000, # John Grisham
        30000000, 15000000,  # Dale Carnegie 
        100000000, 20000000, # Napoleon Hill
        50000000, 20000000   
    ]
})



novo_autores2 = {
    'id_autor': [10, 11, 12, 13],
    'Nome': ['Agatha Christie', 'Stephen King', 'Olga Tokarczuk', 'Andezej Sapkowski'],
    'Nacionalidade': ['Britânico', 'Americano', 'Polonesa', 'Polonesa'],
    'Idade': [85, 77, 63, 77]
}

df_autores = pd.concat([df_autores, pd.DataFrame(novo_autores2)], ignore_index=True)


# print(tabulate(df_obras, headers= 'keys', tablefmt= 'grid'))


novos_livros = ({
    'id_livro': [17,18,19,20,21,22,23,24],
    'Título':['Assassinato no Expresso do Oriente','E Não Sobrou Nenhum','O Iluminado','It: A Coisa','Sobre os Ossos dos Mortos','Viagens','O Último Desejo', ' Espada do Destino'],
    'id_autor': [9,9,10,10,11,11,12,12],
    'Arrecadado': [25400000, 19000000, 30000000,450000000,18000000,21200000, 23600000,21000000]
})
df_obras = pd.concat([df_obras, pd.DataFrame(novos_livros)], ignore_index=True)

print(tabulate(df_obras, headers= 'keys', tablefmt= 'grid'))