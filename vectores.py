import math

#Calculo de componentes cartesianas con angulo estandar
def calcular_componentes(magnitud, angulo_grados):
    angulo_radianes = math.radians(angulo_grados)
    # Componente x
    componente_x = magnitud * math.cos(angulo_radianes)

    # Componente y
    componente_y = magnitud * math.sin(angulo_radianes)
    # Datos del vector
    
    # Resultados
    print(f"Magnitud: {magnitud}m")
    print(f"Ángulo: {angulo_grados}°")
    print(f"Componente X: {componente_x:.2f}m") 
    print(f"Componente Y: {componente_y:.2f}m")

calcular_componentes(42, 37)
calcular_componentes(25, 338)
calcular_componentes(30, 240)



# magnitud_A = 42  # metros
# angulo_grados_A = 37 # grados

# # Convertir el ángulo de grados a radianes
# angulo_radianes_A = math.radians(angulo_grados_A)

# # Componente x
# componente_x_A = magnitud_A * math.cos(angulo_radianes_A)

# # Componente y
# componente_y_A = magnitud_A * math.sin(angulo_radianes_A)

# # Resultados
# print(f"Magnitud: {magnitud_A}m")
# print(f"Ángulo: {angulo_grados_A}°")
# print(f"Componente X: {componente_x_A:.2f}m") 
# print(f"Componente Y: {componente_y_A:.2f}m")

# # Datos del vector B
# magnitud_B = 25  # m/s
# angulo_grados_B = 22 # grados

# # Convertir el ángulo de grados a radianes
# angulo_radianes_B = math.radians(angulo_grados_B)

# # Componente x
# componente_x_B = magnitud_B * math.cos(angulo_radianes_B)

# # Componente y
# componente_y_B = magnitud_B * -math.sin(angulo_radianes_B)

# # Imprimir los resultados
# print(f"Magnitud: {magnitud_B}m/s")
# print(f"Ángulo: {angulo_grados_B}°")
# print(f"Componente X: {componente_x_B:.2f}m/s")
# print(f"Componente Y: {componente_y_B:.2f}m/s")

# # Datos del vector C
# magnitud_C = 30  # Newtons (N)
# angulo_grados_C = 30 # grados

# # Convertir el ángulo de grados a radianes
# angulo_radianes_C = math.radians(angulo_grados_C)

# # Componente x
# componente_x_C = -magnitud_C * math.sin(angulo_radianes_C)

# # Componente y
# componente_y_C = -magnitud_C * math.cos(angulo_radianes_C)

# # Imprimir los resultados
# print(f"Magnitud: {magnitud_C}N")
# print(f"Ángulo: {angulo_grados_C}°")
# print(f"Componente X: {componente_x_C:.2f}N")
# print(f"Componente Y: {componente_y_C:.2f}N")
