"""
Trabalho de Introdução à Análise de Dados

Estudo do censo estudantil brasileiro de ensino superior do ano de 2014

Autores: Gabriel Jacinto e João Pedro Carvalho Moreira
Data: 02/02/2022
"""
#%% LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt

#%% DATA READING
plot_color = ['chocolate', 'darkred', 'saddlebrown', 'lightcoral', 'seagreen', 'lightseagreen', 'teal']     # Colors for the plots in the code
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

census_raw = pd.read_csv("SUP_ALUNO_2014.csv", sep = "|", usecols = col_list)                               # Reads the .csv file with separator "|" and save in DataFrame

#%% ADMINISTRATIVE CATEGORY
'''
ADMINISTRATIVE CATEGORY
Type of Administrative Category of the IES
1. Pública Federal
2. Pública Estadual
3. Pública Municipal
4. Privada com fins lucrativos
5. Privada sem fins lucrativos
6. Privada - Particular em sentido estrito
7. Especial
8. Privada comunitária
9. Privada confessional
'''
adm_category = census_raw['TP_CATEGORIA_ADMINISTRATIVA']                                        # Selects only Administrative Category column
adm_category = adm_category.replace([1,2,3], "Public")                                          # Assigns "Public" to numbers 1, 2 and 3
adm_category = adm_category.replace([4,5,6,7,8,9], "Private")                                   # Assigns "Private" to numbers 4, 5, 6, 7, 8 and 9
count_adm_category = dict(adm_category.value_counts())                                          # Counts how many public and private studants, and saves in dictionary 

plt.figure(1)                                                                                   # Creates the Figure 1
plt.suptitle('Administrative Category of Students\n Universities in Brazil')                    # Sets the title                                                                               
plt.subplot(1,2,1)                                                                              # Creates a subplot
plt.xticks(range(len(count_adm_category)), count_adm_category.keys(), rotation='horizontal')    # Sets the x label sticks
plt.bar(range(len(count_adm_category)), count_adm_category.values(),
        color = plot_color[2:4])                                                                # Makes a bar plot
plt.xlabel('Administrative Category')                                                           # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_adm_category.values(), labels = count_adm_category.keys(),
        autopct = "%1.1f%%", startangle = 90, colors = plot_color[2:4])                         # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout

#%% COURSE SHIFT
'''
COURSE SHIFT
Type of course shift to which the student is linked
1. Morning
2. Afternoon
3. Night
4. Full
(.) Not applicable (Ead)
'''
course_shift = census_raw['TP_TURNO']                                                           # Selects only Course Shift column
course_shift = course_shift.replace(1, "Morning")                                               # Assigns "Morning" to number 1
course_shift = course_shift.replace(2, "Afternoon")                                             # Assigns "Afternoon" to number 2
course_shift = course_shift.replace(3, "Night")                                                 # Assigns "Night" to number 3
course_shift = course_shift.replace(4, "Full")                                                  # Assigns "Full" to number 4
count_course_shift = dict(course_shift.value_counts())                                          # Counts the shift of courses, and saves in dictionary 

plt.figure(2)                                                                                   # Creates the Figure 2    
plt.title('Courses Shift of the Students\n in Brazil Universities')                             # Sets the title                                                                                                                                                            # Creates a subplot
plt.xticks(range(len(count_course_shift)), count_course_shift.keys(), rotation='horizontal')    # Sets the x label sticks
plt.bar(range(len(count_course_shift)), count_course_shift.values(),
        color = plot_color[0:4])                                                                # Makes a bar plot
plt.xlabel('Shift')                                                                             # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.axes([.6, .5, .4, .4], facecolor='y')                                                       # Sets the axes of the next plot
plt.pie(count_course_shift.values(), startangle = 90, colors = plot_color[0:4])                 # Makes apie plot
plt.tight_layout()                                                                              # Adjusts the layout

#%% EDUCATION MODALITY
'''
EDUCATION MODALITY
Type of course teaching modality
1. In person
2. In Distance
'''
education_modality = census_raw['TP_MODALIDADE_ENSINO']                                         # Selects only Education Modality column
education_modality = education_modality.replace(1, "In Person")                                 # Assigns "In Person" to number 1
education_modality = education_modality.replace(2, "In Distance")                               # Assigns "In Distance" to number 2
count_education_modality = dict(education_modality.value_counts())                              # Counts how many in person and in distance studants, and saves in dictionary 

plt.figure(3)                                                                                   # Creates the Figure 3
plt.suptitle('Education Modality of the Students\n in Brazil Universities')                     # Sets the title
plt.subplot(1,2,1)                                                                              # Creates a subplot                                                                                                                                                           # Creates subplot
plt.xticks(range(len(count_education_modality)), count_education_modality.keys(), 
           rotation='horizontal')                                                               # Sets the x label sticks
plt.bar(range(len(count_education_modality)), count_education_modality.values(),
        color = plot_color[3:5])                                                                # Makes a bar plot
plt.xlabel('Shift')                                                                             # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label      
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_education_modality.values(), labels = count_education_modality.keys(),
        autopct = "%1.1f%%", startangle = 90, colors = plot_color[3:5])                         # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout

#%% COLOR/RACE
'''
COLOR/RACE
Student's color/race type
0. Student did not want to declare color/race
1. White
2. Black
3. Brown
4. Yellow
5. Indigenous
9. Does not have the information (No response)
'''
color_race = census_raw['TP_COR_RACA']                                                          # Selects only Color/Race column
color_race = color_race.replace(0, "Not Declare")                                               # Assigns "Not Declare" to number 0
color_race = color_race.replace(1, "White")                                                     # Assigns "White" to number 1
color_race = color_race.replace(2, "Black")                                                     # Assigns "Black" to number 2
color_race = color_race.replace(3, "Brown")                                                     # Assigns "Brown" to number 3
color_race = color_race.replace(4, "Yellow")                                                    # Assigns "Yellow" to number 4
color_race = color_race.replace(5, "Indigenous")                                                # Assigns "Indigenous" to number 5
color_race = color_race.replace(9, "No response")                                               # Assigns "No response" to number 9
count_color_race = dict(color_race.value_counts())                                              # Counts the color/race of the students, and saves in dictionary 

plt.figure(4)                                                                                   # Creates the Figure 4
plt.title("Students's Color/Race in Brazil Universities")                                       # Sets the title
plt.xticks(range(len(count_color_race)), count_color_race.keys(), 
           rotation = 20)                                                                       # Sets the x label sticks
plt.bar(range(len(count_color_race)), count_color_race.values(),
        color = plot_color[0:7])                                                                # Makes a bar plot
plt.xlabel('Color/Race')                                                                        # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label      
plt.axes([.6, .5, .4, .4], facecolor='y')                                                       # Sets the axes of next plot
plt.pie(count_color_race.values(), startangle = 90, colors = plot_color[0:7])                   # Makes a pie plot inside the plot
plt.tight_layout()                                                                              # Adjusts the layout

#%% SEX
'''
SEX
Informs the student's gender
1. Famale
2. Male 
'''
male_female = census_raw['TP_SEXO']                                                             # Selects only Sex column
male_female = male_female.replace(1, "Female")                                                  # Assigns "Female" to number 1
male_female = male_female.replace(2, "Male")                                                    # Assigns "Male" to number 2
count_male_female = dict(male_female.value_counts())                                            # Counts how many males and females students, and saves in dictionary 

plt.figure(5)                                                                                   # Creates the Figure 5
plt.suptitle("Students's Sex in Brazil Universities")                                           # Sets the title
plt.subplot(1,2,1)                                                                              # Creates a subplot
plt.xticks(range(len(count_male_female)), count_male_female.keys(), 
           rotation = 20)                                                                       # Sets the x label sticks
plt.bar(range(len(count_male_female)), count_male_female.values(),
        color = plot_color[1:3])                                                                # Makes a bar plot
plt.xlabel('Sex')                                                                               # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label      
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_male_female.values(), labels = count_male_female.keys(),
        autopct = "%1.1f%%", startangle = 90, colors = plot_color[1:3])                         # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout

#%% AGE
'''
AGE
Age completed by the student in the Census reference year
'''
age_in_year = census_raw['NU_IDADE']                                                            # Selects only Sex column
count_age_in_year = age_in_year.to_list()                                                       # Counts how many males and females students, and saves in a list 

plt.figure(6)                                                                                   # Creates the Figure 6
plt.title("Students's Age in Brazil Universities")                                              # Sets the title                                                              # Sets the x label sticks
plt.hist(count_age_in_year, bins=50)                                                            # Makes a bar plot
plt.xlabel('Age')                                                                               # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label      
plt.xlim((0, 70))                                                                               # Limits in x label

