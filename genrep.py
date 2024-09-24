#Author: Liam 
#Date: 2024-09-24   
print('Välkommen!') 
resistorer = input("Ange resistorer: ")
if resistorer == "":
       print("Seriresistans: 0 ohms")
       print("Parallellresistans: 0 ohms")
else:
       resistorer_list = list(map(int, resistorer.split()))
       serieresistans = sum(resistorer_list)
       parallellresistans = 1 / sum(1 / r for r in resistorer_list)
       print(f"Seriresistans: {serieresistans} ohms")
       print(f"Parallellresistans: {parallellresistans} ohms")


