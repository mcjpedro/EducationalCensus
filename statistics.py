"""
Trabalho de Introdução à Análise de Dados

Estudo do censo estudantil brasileiro de ensino superior do ano de 2014

Autores: Gabriel Jacinto e João Pedro Carvalho Moreira
Data: 02/02/2022
"""
#%% LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

#%% DATA READING
col_list = ["TP_CATEGORIA_ADMINISTRATIVA",
            "TP_TURNO",
            "TP_MODALIDADE_ENSINO",
            "TP_COR_RACA",
            "TP_SEXO",
            "NU_IDADE",
            "CO_UF_NASCIMENTO",
            "IN_DEFICIENCIA",
            "TP_SITUACAO",
            "IN_RESERVA_VAGAS",
            "IN_FINANCIAMENTO_ESTUDANTIL",
            "IN_APOIO_SOCIAL",
            "IN_ATIVIDADE_EXTRACURRICULAR"]                                                                 # Interest columns

census_raw = pd.read_csv("SUP_ALUNO_2014_NEW.csv", usecols = col_list)                                      # Reads the .csv file and save in DataFrame
# census_raw['TP_TURNO'].replace('Afternoon', "Daytime", inplace = True)                                    # Assigns "Daytime" to "Afternoon"
# census_raw['TP_TURNO'].replace('Morning', "Daytime", inplace = True)                                      # Assigns "Daytime" to "Morning"
# census_raw['TP_TURNO'].replace('Full', "Daytime", inplace = True)                                         # Assigns "Daytime" to "Full"

census_raw['REGIAO_NASCIMENTO'] = census_raw['CO_UF_NASCIMENTO']
census_raw['REGIAO_NASCIMENTO'].replace(['RO','AC','AM','RR','PA','AP','TO'], "North", inplace = True)      # Create region north
census_raw['REGIAO_NASCIMENTO'].replace(['MA','PI','CE','RN','PB','PE',
                                        'AL','SE','BA'], "North East", inplace = True)                      # Create region north east
census_raw['REGIAO_NASCIMENTO'].replace(['MT','MS','GO','DF'], "Midwest", inplace = True)                   # Create region midwest
census_raw['REGIAO_NASCIMENTO'].replace(['MG','ES','RJ','SP'], "South East", inplace = True)                # Create region south east
census_raw['REGIAO_NASCIMENTO'].replace(['PR','SC','RS'], "South", inplace = True)                          # Create region south

#%% FUNTION TO CHI SQUARE TEST

# Defining the chi square test
def chi_square(x, y, title) : 
    
    contigency = pd.crosstab(y,x)                                                                           # Create a crosstab
    results = stats.chi2_contingency(contigency)                                                            # Perform the chi square test
    p_value = results[1]                                                                                    # Extract the P-Value of the test
    
    # Verify if the test is significant
    if p_value <= 0.05 :
        
        contigency = pd.crosstab(y,x, normalize='columns')                                                  # Re-criate the crosstable normalizing the columns
        
        plt.figure(figsize=(12,8))
        plt.title(title + '\nP-Value: {:.3f}'.format(p_value))
        sns.heatmap(contigency, annot=True, cmap='YlGnBu')                                                  # Plot a heatmap
        
    else :
        
        print('P-Value > 0,05: There is no relation between the groups!')                                   # Print a message if the test haven't significance
        
#%% STATISTICS: COLOR/RACE VS LOAN IN PRIVATE UNIVERSITIES
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only
df.drop(df[df.TP_CATEGORIA_ADMINISTRATIVA != 'Private'].index, inplace=True)                                # Select students from private institutions
df.drop(df[df.TP_COR_RACA == 'No response'].index, inplace=True)                                            # Remove students that haven't answered their color/race
df.drop(df[df.TP_COR_RACA == 'Not Declare'].index, inplace=True)                                            # Remove students that haven't declared their color/race

title= "Student's loan by color/race\nin Brazilian Private Universities"                                     # Set the graph title
chi_square(df['TP_COR_RACA'], df['IN_FINANCIAMENTO_ESTUDANTIL'], title)                                     # Run the stat test

#%% STATISTICS: COLOR/RACE VS SOCIAL SUPPORT IN PUBLIC UNIVERSITIES
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only
df.drop(df[df.TP_CATEGORIA_ADMINISTRATIVA != 'Public'].index, inplace=True)                                 # Select students from private institutions
df.drop(df[df.TP_COR_RACA == 'No response'].index, inplace=True)                                            # Remove students that haven't answered their color/race
df.drop(df[df.TP_COR_RACA == 'Not Declare'].index, inplace=True)                                            # Remove students that haven't declared their color/race

title= 'Students with social support by color/race\in Brazilian Public Universities'                        # Set the graph title
chi_square(df['TP_COR_RACA'], df['IN_APOIO_SOCIAL'], title)                                                 # Run the stat test
