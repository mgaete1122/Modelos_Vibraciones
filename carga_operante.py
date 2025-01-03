import matplotlib.pyplot as plt

charges = []
hole_times = []
tol = []
charges_number = int(input("Ingresa el numero de cargas: "))

for i in range(charges_number):
    charges.append(i+1)
    hole_times.append(int(input("Ingresa el tiempo de la carga " 
                                + str(i+1) + ": ")))
    tol.append(int(input("Ingresa la tolerancia de la carga " 
                         + str(i+1) + ": ")))

time_ranges = []

for i in range(charges_number):
    time_ranges.append([hole_times[i] - tol[i], 
                        hole_times[i] + tol[i]])
    
for i in range(charges_number):
    plt.plot([time_ranges[i][0], time_ranges[i][1]], 
             [charges[i], charges[i]], color = 'blue')

plt.xlabel('Tiempo de retardo (ms)')
plt.ylabel('Carga')
plt.title('Visualización de detonaciones simultáneas')
plt.grid(True)
plt.show()
