# import pandas as pd
# import io

# data_frm = pd.read_csv('/home/abdeljalil/Desktop/youcode/Brief_Nettoyage_des_Donn-es/data_scrap.csv', encoding='latin1')

# # Capture the info output to a string
# buffer = io.StringIO()
# data_frm.info(buf=buffer)
# data_info = buffer.getvalue()

# # Get the first few rows of the dataframe and describe it
# data_head = data_frm.head()
# data_description = data_frm.describe()

# # Save everything to a single CSV file
# with open('Analyse_Preliminaire_Donnees.csv', 'w', encoding='utf-8') as f:
#     # Write data_info to the file as the first section
#     f.write("Data Info:\n")
#     f.write(data_info)
#     f.write("\n\n")  # Add space between sections

#     # Write data_head to the file as the second section
#     f.write("Data Head:\n")
#     data_head.to_csv(f, index=False)
#     f.write("\n\n")  # Add space between sections

#     # Write data_description to the file as the third section
#     f.write("Data Description:\n")
#     data_description.to_csv(f)

# print("Data has been written to 'Analyse_Preliminaire_Donnees.csv'")



# data_info.to_csv('Analyse_Preliminaire_Donnees.csv', index=False)

# # Capture the info output to a string
# buffer = io.StringIO()
# data_frm.info(buf=buffer)
# data_info = buffer.getvalue()

# # Get the first few rows of the dataframe and describe it
# data_head = data_frm.head()
# data_description = data_frm.describe()

# # Save data_info to CSV
# with open('Analyse_Preliminaire_Donnees.csv', 'w', encoding='utf-8') as f:
#     f.write(data_info)

# # Optionally, you can save the data_head and data_description as well
# data_head.to_csv('Analyse_Preliminaire_Head.csv', index=False)
# data_description.to_csv('Analyse_Preliminaire_Description.csv')




# data_frm.info()
# data_info = data_frm.info()
# data_head = data_frm.head()
# data_description = data_frm.describe()

# print (data_info, data_head, data_description)



# data_cpy['Price'] = pd.to_numeric(data_cpy['Price'], errors='coerce')

# data_cpy['Price'] = data_cpy['Price'].fillna(data_cpy['Price'].mean())
# data_cpy['Price'] = data_cpy['Price'].fillna(data_cpy['Price'].median())

# price_moyenne = data_cpy.groupby('Title')['Price'].mean().sort_values(ascending=False)
# price_médiane = data_cpy.groupby('Title')['Price'].median().sort_values(ascending=False)

# print (price_moyenne, price_médiane)






