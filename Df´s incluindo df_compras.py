import pandas as pd
from tabulate import tabulate


# Criando o DataFrame de Autores

df_autores = pd.DataFrame({
    'id_autor':[1,2,3,4,5,6,7],
    'Nome':['Bernard Cornwell','Conn Iggulden','George R. R. Martin','John Grisham','Dale Carnegie','Napoleon Hill','Gabriel G Márquez'],
    'Nacionalidade':['Britânico','Britânico','Americano','Americano','Americano','Americano','Colombiano'],
    'Idade': [81,54,78,70,66,87,87]
})

# Incluindo J.K. Rowling
novo_autor = {
    'id_autor': 8,
    'Nome': 'J. K. Rowling',
    'Nacionalidade': 'Britânico',
    'Idade': 59
}
df_autores = pd.concat([df_autores, pd.DataFrame([novo_autor])], ignore_index=True)

# Incluindo mais autores
novos_autores2 = pd.DataFrame({
    'id_autor': [9, 10, 11, 12],
    'Nome': ['Agatha Christie', 'Stephen King', 'Olga Tokarczuk', 'Andrzej Sapkowski'],
    'Nacionalidade': ['Britânico', 'Americano', 'Polonesa', 'Polonesa'],
    'Idade': [85, 77, 63, 77]
})
df_autores = pd.concat([df_autores, novos_autores2], ignore_index=True)

# Criando o DataFrame de Obras

df_obras = pd.DataFrame({
    'id_livro': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    'Título': [
        'O Último Reino', 'O Águia de Sharpe',                         
        'Genghis: O Nascimento de um Império', 'O Livro Perigoso para Garotos', 
        'A Guerra dos Tronos', 'A Fúria dos Reis',                     
        'A Firma', 'Tempo de Matar',                                    
        'Como Fazer Amigos e Influenciar Pessoas', 'Como Evitar Preocupações e Começar a Viver',
        'Quem Pensa Enriquece', 'Atitude Mental Positiva: Caminho para o Sucesso', 
        'Cem Anos de Solidão', 'O Amor nos Tempos do Cólera',          
        'Harry Potter e a Pedra Filosofal', 'Harry Potter e a Câmara Secreta' 
    ],
    'id_autor': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],
    'Arrecadado': [
        5000000, 3000000,    
        4000000, 2500000,    
        120000000, 80000000, 
        100000000, 60000000, 
        30000000, 15000000,  
        100000000, 20000000, 
        50000000, 20000000,  
        120000000, 110000000 
    ]
})

# Incluindo novos livros dos outros autores
novos_livros = pd.DataFrame({
    'id_livro': [17, 18, 19, 20, 21, 22, 23, 24],
    'Título': [
        'Assassinato no Expresso do Oriente', 'E Não Sobrou Nenhum', 
        'O Iluminado', 'It: A Coisa',                                
        'Sobre os Ossos dos Mortos', 'Viagens',                      
        'O Último Desejo', 'Espada do Destino'                      
    ],
    'id_autor': [9, 9, 10, 10, 11, 11, 12, 12],
    'Arrecadado': [
        25400000, 19000000, # Agatha Christie
        30000000, 45000000, # Stephen King
        18000000, 21200000, # Olga Tokarczuk
        23600000, 21000000  # Andrzej Sapkowski
    ]
})
df_obras = pd.concat([df_obras, novos_livros], ignore_index=True)


# Fazendo o MERGE (JOIN)

df_merged = pd.merge(
    df_obras,
    df_autores[['id_autor', 'Nome']],
    how='left',
    on='id_autor'
)

df_merged.rename(columns={'Nome': 'Autor'}, inplace=True)
# print(tabulate(df_merged, headers='keys', tablefmt='grid'))


# print(tabulate(df_merged, headers='keys', tablefmt='grid'))

df_clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nome Cliente': ['Patrick Mahomes', 'Stephen Curry', 'Jalen Hurts', 'LeBron James', 'Joe Burrow', 'Luka Doncic', 'Justin Jefferson', 'Jayson Tatum', 'Lamar Jackson', 'Giannis Antetokounmpo'],
    'Cidade': ['Kansas City', 'San Francisco', 'Philadelphia', 'Los Angeles', 'Cincinnati', 'Dallas', 'Minneapolis', 'Boston', 'Baltimore', 'Milwaukee']
})

novos_clientes = pd.DataFrame({
    'id_cliente': [11, 12],
    'Nome Cliente': ['James Harden', 'Chris Paul'],
    'Cidade': ['Houston', 'Los Angeles']
})

df_clientes = pd.concat([df_clientes, novos_clientes], ignore_index=True)


# print(tabulate(df_merged, headers='keys', tablefmt='grid'))

# print(tabulate(df_clientes, headers='keys', tablefmt='grid'))

df_compras = pd.DataFrame ({
    'id_compra': [1,2,3,4,5,6,],
    'id_livro': [5,6,8,9,7,1],
    'id_cliente': [11,9,8,5,2,7],
    'Valor_compra':[20000, 15000,33000,40500,22000,36000]
})

# print(tabulate(df_compras, headers='keys', tablefmt='grid'))

df_hist_compras = pd.merge(
    df_compras,
    df_clientes,
    on='id_cliente',
    how='left'
)

# print(tabulate(df_hist_compras, headers='keys', tablefmt='grid'))

# df_hist_clientes = pd.merge(
#     df_compras,
#     df_obras,
#     on='id_livro',
#     how= 'left'
# )
# print(tabulate(df_hist_clientes, headers='keys', tablefmt='grid'))

df_hist_obras = pd.merge(
    df_compras,
    df_obras[['id_livro', 'Título', 'id_autor']],
    on='id_livro',
    how='left'
)

print(tabulate(df_hist_obras, headers='keys', tablefmt='grid'))
