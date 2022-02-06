"""
Trabalho de Introdução à Análise de Dados

Estudo do censo estudantil brasileiro de ensino superior do ano de 2014

Autores: Gabriel Jacinto e João Pedro Carvalho Moreira
Data: 02/02/2022
"""
#%% LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
import hypothetical as hp

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
   
#%% FUNCTION TO CHI SQUARE TEST

# Defining the chi square test
def chi_square(DataFrame, column_x, column_y, graph_title) : 
    
    stat = pg.chi2_independence(df, x= column_x, y= column_y)                                               # Calculates the chi square test parameters
    p_value = stat[2]['pval'][0]                                                                            # Select the Pearson's P-Value

    # Verify if the test is significant
    if p_value <= 0.05 :
        
        contigency = pd.crosstab(DataFrame[column_y], DataFrame[column_x], normalize='columns')             # Criate the crosstable for the graphs, normalizing the columns
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS relationship".format(p_value))      # Insert the title with P-Value
        sns.heatmap(contigency, annot=True, cmap='YlGnBu')                                                  # Plot a heatmap
        
    else :
                
        contigency = pd.crosstab(DataFrame[column_y], DataFrame[column_x], normalize='columns')             # Criate the crosstable for the graphs, normalizing the columns    
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS NO relationship".format(p_value))  # Insert the title with P-Value
        sns.heatmap(contigency, annot=True, cmap='YlGnBu')                                                  # Plot a heatmap
        
#%% STATISTICS: COLOR/RACE VS LOAN IN PRIVATE UNIVERSITIES
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only
df.drop(df[df.TP_CATEGORIA_ADMINISTRATIVA != 'Private'].index, inplace=True)                                # Select students from private institutions
df.drop(df[df.TP_COR_RACA == 'No response'].index, inplace=True)                                            # Remove students that haven't answered their color/race
df.drop(df[df.TP_COR_RACA == 'Not Declare'].index, inplace=True)                                            # Remove students that haven't declared their color/race

title= "Student's loan by color/race in Brazilian Private Universities"                                     # Set the graph title
chi_square(df, 'TP_COR_RACA', 'IN_FINANCIAMENTO_ESTUDANTIL', title)                                         # Run the statistic test

#%% STATISTICS: COLOR/RACE VS SOCIAL SUPPORT IN PUBLIC UNIVERSITIES
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only
df.drop(df[df.TP_CATEGORIA_ADMINISTRATIVA != 'Public'].index, inplace=True)                                 # Select students from public institutions
df.drop(df[df.TP_COR_RACA == 'No response'].index, inplace=True)                                            # Remove students that haven't answered their color/race
df.drop(df[df.TP_COR_RACA == 'Not Declare'].index, inplace=True)                                            # Remove students that haven't declared their color/race

title= 'Students with social support by color/race in Brazilian Public Universities'                        # Set the graph title
chi_square(df, 'TP_COR_RACA', 'IN_APOIO_SOCIAL', title)                                                     # Run the statistic test

#%% STATISTICS: EXTRACURRICULAR ACTIVITIES VS ADMINISTRATIVE CATEGORY
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only

title= 'Students with extracurricular activities by the University administrative category'                 # Set the graph title
chi_square(df, 'TP_CATEGORIA_ADMINISTRATIVA', 'IN_ATIVIDADE_EXTRACURRICULAR', title)                        # Run the statistic test

#%% STATISTICS: EXTRACURRICULAR ACTIVITIES VS SHIFT
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only

title= 'Students with extracurricular activities by the course shift'                                       # Set the graph title
chi_square(df, 'TP_TURNO', 'IN_ATIVIDADE_EXTRACURRICULAR', title)                                           # Run the statistic test

#%% STATISTICS: SOCIAL SUPPORT VS RESERVATION OF VACANCIES
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only
df.drop(df[df.TP_CATEGORIA_ADMINISTRATIVA != 'Public'].index, inplace=True)                                 # Select students from public institutions

title= 'Students with social support by the reservation\
    of vacancies program in Brazilian Public Universities'                                                  # Set the graph title
chi_square(df, 'IN_RESERVA_VAGAS', 'IN_APOIO_SOCIAL', title)                                                # Run the statistic test

#%% STATISTICS: AGE VS RACE/COLOR
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only
df.drop(df[df.TP_COR_RACA == 'No response'].index, inplace=True)                                            # Remove students that haven't answered their color/race
df.drop(df[df.TP_COR_RACA == 'Not Declare'].index, inplace=True)                                            # Remove students that haven't declared their color/race

graph_title = 'Students age distribution by race/color in Brazilian Universities'                           # Set graph title

stat = pg.normality(df, dv='NU_IDADE', group='TP_COR_RACA', method='normaltest', alpha=0.05)                # Evaluate if the data have a normal distribution
normality = stat['pval'][0]                                                                                 # Select the Person's P-Value

#Test to perform the Mood's Median test
if normality <= 0.05 :
    
    pivoted = df.pivot(values='NU_IDADE', columns='TP_COR_RACA')                                            # Create a DataFrame with race/color as columns and ages as values
       
    mood = hp.nonparametric.MedianTest(pivoted['White'].dropna(),                                           # Performs Mood's Median test
                                       pivoted['Brown'].dropna(),
                                       pivoted['Black'].dropna(),
                                       pivoted['Indigenous'].dropna(),
                                       pivoted['Yellow'].dropna())
    p_value = mood.test_summary['p-value']                                                                  # Selects the P-Value

    # Verify if the test is significant
    if p_value <= 0.05 :
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS difference".format(p_value))        # Insert the title with P-Value
        sns.set_theme(style="whitegrid")                                                                    # Set graph theme
        sns.boxplot(x= 'TP_COR_RACA', y='NU_IDADE', data=df)                                                # Plot a boxplot
        
    else :
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS NO difference".format(p_value))     # Insert the title with P-Value
        sns.set_theme(style="whitegrid")                                                                    # Set graph theme
        sns.boxplot(x= 'TP_COR_RACA', y='NU_IDADE', data=df)                                                # Plot a boxplot


else :
    
    print("Age vs Race/color: it's a normal distribution! Try other statistical test.")                     # Message case the P-Value from the normality test is greater than 0.05

#%% STATISTICS: AGE VS BIRTH REGION
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only

graph_title = 'Students age distribution by region of birth in Brazilian Universities'                      # Set graph title

stat = pg.normality(df, dv='NU_IDADE', group='REGIAO_NASCIMENTO', method='normaltest', alpha=0.05)          # Evaluate if the data have a normal distribution
normality = stat['pval'][0]                                                                                 # Select the Person's P-Value

#Test to perform the Mood's Median test
if normality <= 0.05 :
    
    pivoted = df.pivot(values='NU_IDADE', columns='REGIAO_NASCIMENTO')                                      # Create a DataFrame with birth region as columns and ages as values
       
    mood = hp.nonparametric.MedianTest(pivoted['North'].dropna(),                                           # Performs Mood's Median test
                                       pivoted['North East'].dropna(),
                                       pivoted['Midwest'].dropna(),
                                       pivoted['South East'].dropna(),
                                       pivoted['South'].dropna())
    p_value = mood.test_summary['p-value']                                                                  # Selects the P-Value

    # Verify if the test is significant
    if p_value <= 0.05 :
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS difference".format(p_value))        # Insert the title with P-Value
        sns.set_theme(style="whitegrid")                                                                    # Set graph theme
        sns.boxplot(x= 'REGIAO_NASCIMENTO', y='NU_IDADE', data=df)                                          # Plot a boxplot

    else :
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS NO difference".format(p_value))     # Insert the title with P-Value
        sns.set_theme(style="whitegrid")                                                                    # Set graph theme
        sns.boxplot(x= 'REGIAO_NASCIMENTO', y='NU_IDADE', data=df)                                          # Plot a boxplot

else :
    
    print("Age vs birth region: it's a normal distribution! Try other statistical test.")                   # Message case the P-Value from the normality test is greater than 0.05

#%% STATISTICS: AGE VS GENDER
df = census_raw.copy()                                                                                      # Copy Data Frame

# Configuring and cleaning the Data Frame
df.drop(df[df.TP_SITUACAO != 'Attending'].index, inplace=True)                                              # Select students that are attending only

graph_title = 'Students age distribution by gender in Brazilian Universities'                               # Set graph title

stat = pg.normality(df, dv='NU_IDADE', group='TP_SEXO', method='normaltest', alpha=0.05)                    # Evaluate if the data have a normal distribution
normality = stat['pval'][0]                                                                                 # Select the Person's P-Value

#Test to perform the Mood's Median test
if normality <= 0.05 :
    
    # pivoted = df.pivot(values='NU_IDADE', columns='TP_SEXO')                                              # Create a DataFrame with birth region as columns and ages as values
       
    mann_whitney = hp.nonparametric.MannWhitney(group= df['TP_SEXO'],                                       # Performs Mann-Whitney test
                                                y1= df['NU_IDADE'])
    p_value = mann_whitney.test_summary['p-value']                                                          # Selects the P-Value

    # Verify if the test is significant
    if p_value <= 0.05 :
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS difference".format(p_value))        # Insert the title with P-Value
        sns.set_theme(style="whitegrid")                                                                    # Set graph theme
        sns.boxplot(x= 'TP_SEXO', y='NU_IDADE', data=df)                                                    # Plot a boxplot

    else :
        
        plt.figure(figsize=(12,8))                                                                          # Define the graph size
        plt.title(graph_title + "\nPearson's P-Value: {:.3f} - THERE IS NO difference".format(p_value))     # Insert the title with P-Value
        sns.set_theme(style="whitegrid")                                                                    # Set graph theme
        sns.boxplot(x= 'TP_SEXO', y='NU_IDADE', data=df)                                                    # Plot a boxplot

else :
    
    print("Age vs gender: it's a normal distribution! Try other statistical test.")                   # Message case the P-Value from the normality test is greater than 0.05

