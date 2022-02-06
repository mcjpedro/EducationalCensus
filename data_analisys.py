"""
Trabalho de Introdução à Análise de Dados

Estudo do censo estudantil brasileiro de ensino superior do ano de 2014

Autores: Gabriel Jacinto e João Pedro Carvalho Moreira
Data: 02/02/2022
"""
#%% LIBRARIES

import pandas as pd
import geopandas as gpd
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
1. Federal Public
2. State Public
3. Municipal Public
4. Private for profit
5. Private non-profit
6. Private - Private in the strict sense
7. Special
8. Community private
9. Confessional private
'''
census_raw['TP_CATEGORIA_ADMINISTRATIVA'].replace([1,2,3], "Public", inplace = True)            # Assigns "Public" to numbers 1, 2 and 3
census_raw['TP_CATEGORIA_ADMINISTRATIVA'].replace([4,5,6,7,8,9], "Private", inplace = True)     # Assigns "Private" to numbers 4, 5, 6, 7, 8 and 9
adm_category = census_raw['TP_CATEGORIA_ADMINISTRATIVA']                                        # Selects only Administrative Category column
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
census_raw['TP_TURNO'].replace(1, "Morning", inplace = True)                                    # Assigns "Morning" to number 1
census_raw['TP_TURNO'].replace(2, "Afternoon", inplace = True)                                  # Assigns "Afternoon" to number 2
census_raw['TP_TURNO'].replace(3, "Night", inplace = True)                                      # Assigns "Night" to number 3
census_raw['TP_TURNO'].replace(4, "Full", inplace = True)                                       # Assigns "Full" to number 4
course_shift = census_raw['TP_TURNO']                                                           # Selects only Course Shift column
count_course_shift = dict(course_shift.value_counts())                                          # Counts the shift of courses, and saves in dictionary 

plt.figure(2)                                                                                   # Creates the Figure 2    
plt.title('Courses Shift of the Students\n in Brazil Universities')                             # Sets the title                                                                                                                                                         
plt.xticks(range(len(count_course_shift)), count_course_shift.keys(), rotation='horizontal')    # Sets the x label sticks
plt.bar(range(len(count_course_shift)), count_course_shift.values(),
        color = plot_color[0:4])                                                                # Makes a bar plot
plt.xlabel('Shift')                                                                             # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.axes([.52, .45, .4, .4], facecolor='y')                                                     # Sets the axes of the next plot
plt.pie(count_course_shift.values(), startangle = 90, colors = plot_color[0:4])                 # Makes apie plot

#%% EDUCATION MODALITY
'''
EDUCATION MODALITY
Type of course teaching modality
1. In person
2. In Distance
'''
census_raw['TP_MODALIDADE_ENSINO'].replace(1, "In Person", inplace = True)                      # Assigns "In Person" to number 1
census_raw['TP_MODALIDADE_ENSINO'].replace(2, "In Distance", inplace = True)                    # Assigns "In Distance" to number 2
education_modality = census_raw['TP_MODALIDADE_ENSINO']                                         # Selects only Education Modality column
count_education_modality = dict(education_modality.value_counts())                              # Counts how many in person and in distance studants, and saves in dictionary 

plt.figure(3)                                                                                   # Creates the Figure 3
plt.suptitle('Education Modality of the Students\n in Brazil Universities')                     # Sets the title
plt.subplot(1,2,1)                                                                              # Creates a subplot                                                                                                                                                          
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
census_raw['TP_COR_RACA'].replace(0, "Not Declare", inplace = True)                             # Assigns "Not Declare" to number 0
census_raw['TP_COR_RACA'].replace(1, "White", inplace = True)                                   # Assigns "White" to number 1
census_raw['TP_COR_RACA'].replace(2, "Black", inplace = True)                                   # Assigns "Black" to number 2
census_raw['TP_COR_RACA'].replace(3, "Brown", inplace = True)                                   # Assigns "Brown" to number 3
census_raw['TP_COR_RACA'].replace(4, "Yellow", inplace = True)                                  # Assigns "Yellow" to number 4
census_raw['TP_COR_RACA'].replace(5, "Indigenous", inplace = True)                              # Assigns "Indigenous" to number 5
census_raw['TP_COR_RACA'].replace(9, "No response", inplace = True)                             # Assigns "No response" to number 9
color_race = census_raw['TP_COR_RACA']                                                          # Selects only Color/Race column
count_color_race = dict(color_race.value_counts())                                              # Counts the color/race of the students, and saves in dictionary 

plt.figure(4)                                                                                   # Creates the Figure 4
plt.title("Students's Color/Race in Brazil Universities")                                       # Sets the title
plt.xticks(range(len(count_color_race)), count_color_race.keys(), 
           rotation = 20)                                                                       # Sets the x label sticks
plt.bar(range(len(count_color_race)), count_color_race.values(),
        color = plot_color[0:7])                                                                # Makes a bar plot
plt.xlabel('Color/Race')                                                                        # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label      
plt.axes([.52, .45, .4, .4], facecolor='y')                                                     # Sets the axes of next plot
plt.pie(count_color_race.values(), startangle = 90, colors = plot_color[0:7])                   # Makes a pie plot inside the plot

#%% SEX
'''
SEX
Informs the student's gender
1. Famale
2. Male 
'''
census_raw['TP_SEXO'].replace(1, "Female", inplace = True)                                      # Assigns "Female" to number 1
census_raw['TP_SEXO'].replace(2, "Male", inplace = True)                                        # Assigns "Male" to number 2
male_female = census_raw['TP_SEXO']                                                             # Selects only Sex column
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
age_in_year = census_raw['NU_IDADE']                                                            # Selects only Age column
count_age_in_year = age_in_year.to_list()                                                       # Saves teh ages in a list 

plt.figure(6)                                                                                   # Creates the Figure 6
plt.title("Students's Age in Brazil Universities")                                              # Sets the title                                                     
plt.hist(count_age_in_year, bins=50)                                                            # Makes a bar plot
plt.xlabel('Age')                                                                               # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label      
plt.xlim((0, 70))                                                                               # Limits in x label

#%% FU OF BIRTH
'''
FU OF BIRTH
IBGE code of the Federation Unit of birth of the student
ps: To run this part of code you must install "geopandas" and "descartes"
'''
fu_code = [12,27,16,13,29,23,53,32,52,21,51,50,31,15,25,41,26,22,24,43,33,11,14,42,35,28,17]    # Federation Units IBGE code
fu_name = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR",
           "PE","PI","RN","RS","RJ","RO","RR","SC","SP","SE","TO"]                              # Federation Units names
census_raw['CO_UF_NASCIMENTO'].replace(fu_code, fu_name, inplace = True)                        # Assigns the FU name to the FU code
fu_of_birth = census_raw['CO_UF_NASCIMENTO']                                                    # Selects only FU of Birth column
count_fu_of_birth = dict(fu_of_birth.value_counts())
map_fu_of_birth = pd.DataFrame(fu_of_birth.value_counts())                                      # Counts the number of students per state and saves in DataFrame
map_fu_of_birth = map_fu_of_birth.reset_index()                                                 # Creates a column with FU name in DataFrame
map_fu_of_birth.rename({'index':'UF'}, axis = 1, inplace = True)                                # Renames the FU column

info_fus = gpd.read_file("bcim_2016_21_11_2018.gpkg", layer = 'lim_unidade_federacao_a')        # Opens the BCIM database with Geopandas
info_fus.rename({'sigla':'UF'}, axis = 1, inplace = True)                                       # Renames the FU column
brasil_map = info_fus.merge(map_fu_of_birth, on = 'UF', how = 'left')                           # Joins the two DataFrames


plt.figure(7)                                                                                   # Creates the Figure 7
plt.suptitle('Higher Education Students in Brazil by State')                                    # Sets the title 
plt.xticks(range(len(count_fu_of_birth)), count_fu_of_birth.keys(), 
           rotation = 'vertical')                                                               # Sets the x label sticks
plt.bar(range(len(count_fu_of_birth)), count_fu_of_birth.values(),
        color = plot_color)                                                                     # Makes a bar plot
plt.xlabel('Federation Units')                                                                  # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label

brasil_map.plot(column = 'CO_UF_NASCIMENTO', cmap = 'OrRd', legend = True, edgecolor = 'black') # Plot the Brazil map
plt.suptitle('Higher Education Students in Brazil by State - Map')                              # Sets the title
plt.xticks([])                                                                                  # Deletes the label
plt.yticks([])                                                                                  # Deletes the label

#%% PEOPLE WITH DISABILITIES
'''
PEOPLE WITH DISABILITIES
Informs if the student is a person with a disability, pervasive developmental disorder or high abilities/giftedness
0. No
1. yes
9. No information available (No response)
'''
census_raw['IN_DEFICIENCIA'].replace(0, "Without disabilities", inplace = True)                 # Assigns "Without disabilities" to number 0
census_raw['IN_DEFICIENCIA'].replace(1, "With disabilities", inplace = True)                    # Assigns "With disabilities" to number 1
census_raw['IN_DEFICIENCIA'].replace(9, "No response", inplace = True)                          # Assigns "No response" to number 9
disabilities = census_raw['IN_DEFICIENCIA']                                                     # Selects only Disabilities column
count_disabilities = dict(disabilities.value_counts())                                          # Counts how many studants with disabilities and saves in dictionary 

plt.figure(9)                                                                                   # Creates the Figure 9
plt.title('Students With Desabilities\n in Brazil Universities')                                # Sets the title                                                                               
plt.xticks(range(len(count_disabilities)), count_disabilities.keys(), rotation = 'horizontal')  # Sets the x label sticks
plt.bar(range(len(count_disabilities)), count_disabilities.values(),
        color = plot_color[1:4])                                                                # Makes a bar plot
plt.xlabel('Disabilities')                                                                      # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.axes([.52, .45, .4, .4], facecolor='y')                                                       # Sets the axes of next plot
plt.pie(count_disabilities.values(), startangle = 90, colors = plot_color[1:4])                 # Makes a pie plot inside the plot                                                                   

#%% COURSE SITUATION
'''
COURSE SITUATION
Type of student's link situation in the course
2. Attending
3. Locked enrollment
4. Unlinked from the course
5. Transferred to another course at the same HEI
6. Graduated 
7. Deceased
'''
situation_number = [2,3,4,5,6,7]                                                                # Sets the situation numbers
situation_name = ["Attending", "Locked", "Unlinked", "Transferred", "Graduated", "Deceased"]    # Sets the situations name
census_raw['TP_SITUACAO'].replace(situation_number, situation_name, inplace = True)             # Assigns the situation name to the situation number
course_situation = census_raw['TP_SITUACAO']                                                    # Selects only Course Situation column
count_course_situation = dict(course_situation.value_counts())                                  # Counts the number of students in a given situation and saves in dictionary 

plt.figure(10)                                                                                  # Creates the Figure 10
plt.title('Course Situation of Students at Universities in Brazil')                             # Sets the title                                                                               
plt.xticks(range(len(count_course_situation)), count_course_situation.keys(), rotation = 'horizontal')  # Sets the x label sticks
plt.bar(range(len(count_course_situation)), count_course_situation.values(),
        color = plot_color[0:7])                                                                # Makes a bar plot
plt.xlabel('Course Situation')                                                                  # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.axes([.52, .45, .4, .4], facecolor='y')                                                     # Sets the axes of next plot
plt.pie(count_course_situation.values(), startangle = 90, colors = plot_color[0:7])             # Makes a pie plot inside the plot 

#%% RESERVATION OF VACANCIES
'''
RESERVATION OF VACANCIES
Informs if the student participates in a place reservation program
0. No
1. Yes
'''
census_raw['IN_RESERVA_VAGAS'].replace(0, "No", inplace = True)                                 # Assigns "No" to number 0
census_raw['IN_RESERVA_VAGAS'].replace(1, "Yes", inplace = True)                                # Assigns "Yes" to number 1
reservation = census_raw['IN_RESERVA_VAGAS']                                                    # Selects only Reservation of Vacancies column
count_reservation = dict(reservation.value_counts())                                            # Counts how many studants with reservation of vacancies and saves in dictionary 

plt.figure(11)                                                                                  # Creates the Figure 11
plt.suptitle('Students With Reservation of Vacancies\n in Brazil Universities')                 # Sets the title 
plt.subplot(1,2,1)                                                                              # Creates a subplot                                                                         
plt.xticks(range(len(count_reservation)), count_reservation.keys(), rotation = 'horizontal')    # Sets the x label sticks
plt.bar(range(len(count_reservation)), count_reservation.values(),
        color = plot_color[0:2])                                                                # Makes a bar plot
plt.xlabel('Reservation of Vacancies')                                                          # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_reservation.values(), labels = count_reservation.keys(), labeldistance = 1.3, 
        pctdistance = 1.1, autopct = "%1.1f%%", startangle = 90, colors = plot_color[0:2])      # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout   

#%% STUDENT LOANS
'''
STUDENT LOANS
Informs if the student uses student financing
0. No
1. Yes
'''
census_raw['IN_FINANCIAMENTO_ESTUDANTIL'].replace(0, "No", inplace = True)                      # Assigns "No" to number 0
census_raw['IN_FINANCIAMENTO_ESTUDANTIL'].replace(1, "Yes", inplace = True)                     # Assigns "Yes" to number 1
student_loans = census_raw['IN_FINANCIAMENTO_ESTUDANTIL']                                       # Selects only Student Loans column
count_student_loans = dict(student_loans.value_counts())                                        # Counts how many studants have loans and saves in dictionary 

plt.figure(12)                                                                                  # Creates the Figure 12
plt.suptitle('Students With Loans\n in Brazil Universities')                                    # Sets the title 
plt.subplot(1,2,1)                                                                              # Creates a subplot                                                                         
plt.xticks(range(len(count_student_loans)), count_student_loans.keys(), rotation = 0)           # Sets the x label sticks
plt.bar(range(len(count_student_loans)), count_student_loans.values(),
        color = plot_color[3:5])                                                                # Makes a bar plot
plt.xlabel('Loans')                                                                             # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_student_loans.values(), labels = count_student_loans.keys(), 
        autopct = "%1.1f%%", startangle = 90, colors = plot_color[3:5])                         # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout  

#%% SOCIAL SUPPORT
'''
SOCIAL SUPPORT
Informs if the student receives any type of social support in the form of housing, transportation, 
food, teaching materials and scholarships (work/stay)
0. No
1. Yes
'''
census_raw['IN_APOIO_SOCIAL'].replace(0, "No", inplace = True)                                  # Assigns "No" to number 0
census_raw['IN_APOIO_SOCIAL'].replace(1, "Yes", inplace = True)                                 # Assigns "Yes" to number 1
social_support = census_raw['IN_APOIO_SOCIAL']                                                  # Selects only Social Support column
count_social_support = dict(social_support.value_counts())                                      # Counts how many studants have social support and saves in dictionary 

plt.figure(13)                                                                                  # Creates the Figure 13
plt.suptitle('Students With Social Support\n in Brazil Universities')                           # Sets the title 
plt.subplot(1,2,1)                                                                              # Creates a subplot                                                                         
plt.xticks(range(len(count_social_support)), count_social_support.keys(), rotation = 0)         # Sets the x label sticks
plt.bar(range(len(count_social_support)), count_social_support.values(),
        color = plot_color[0:2])                                                                # Makes a bar plot
plt.xlabel('Social Support')                                                                    # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_social_support.values(), labels = count_social_support.keys(), 
        autopct = "%1.1f%%", startangle = 90, colors = plot_color[0:2])                         # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout

#%% EXTRACURRICULAR ACTIVITY
'''
EXTRACURRICULAR ACTIVITY
Informs if the student participates in some type of extracurricular activity (non-mandatory internship, extension, monitoring and research)
0. No
1. Yes
'''
census_raw['IN_ATIVIDADE_EXTRACURRICULAR'].replace(0, "No", inplace = True)                     # Assigns "No" to number 0
census_raw['IN_ATIVIDADE_EXTRACURRICULAR'].replace(1, "Yes", inplace = True)                    # Assigns "Yes" to number 1
extracurricular = census_raw['IN_ATIVIDADE_EXTRACURRICULAR']                                    # Selects only Extracurricular Activity column
count_extracurricular = dict(extracurricular.value_counts())                                    # Counts how many studants do any extracurricular activity and saves in dictionary 

plt.figure(14)                                                                                  # Creates the Figure 14
plt.suptitle('Students Who Do Extracurricular Activities\n at Universities in Brazil')          # Sets the title 
plt.subplot(1,2,1)                                                                              # Creates a subplot                                                                         
plt.xticks(range(len(count_extracurricular)), count_extracurricular.keys(), rotation = 0)       # Sets the x label sticks
plt.bar(range(len(count_extracurricular)), count_extracurricular.values(),
        color = plot_color[1:3])                                                                # Makes a bar plot
plt.xlabel('Extracurricular Activity')                                                          # Names the x label
plt.ylabel('Frequency')                                                                         # Names the y label  
plt.subplot(1,2,2)                                                                              # Creates a subplot
plt.pie(count_extracurricular.values(), labels = count_extracurricular.keys(), 
        autopct = "%1.1f%%", startangle = 90, colors = plot_color[1:3])                         # Makes a pie plot
plt.tight_layout()                                                                              # Adjusts the layout

census_raw.to_csv('SUP_ALUNO_2014_NEW.csv')                                                     # Save a new .csv file with all changes