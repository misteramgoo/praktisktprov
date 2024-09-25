#Author: Liam Dvoretsky
#Date: 2024-09-92

product = 1
for num in input("Ange siffror separerade med mellanslag: ").split():
        if num.isdigit():
            num = int(num)
            print(f"\nMultiplikationstabell för {num}:")
            for i in range(1, 11):
                print(f"{num} * {i} = {num * i}")
        else:
            print("Fel: Ange endast siffror separerade med mellanslag")
print("\nProgram avslutat.")


values = input ("Vilka tabeller vill du beräkna?: ")
