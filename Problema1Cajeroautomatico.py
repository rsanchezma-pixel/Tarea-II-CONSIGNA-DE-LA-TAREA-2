# CAJERO AUTOMÁTICO

# Constantes
SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# Variables
saldo = SALDO_INICIAL
retiros_exitosos = 0

print("Bienvenido al cajero automático")
print("Saldo inicial: ₡", saldo)

continuar = input("¿Desea realizar un retiro? (s/n): ").lower()

# Ciclo de retiros
while (continuar == "s" or continuar == "si") and saldo >= RETIRO_MINIMO:

    monto = int(input("Ingrese el monto a retirar: ₡"))

    # Validar el monto solicitado
    if monto < RETIRO_MINIMO:
        print("El monto es menor al mínimo permitido.")

    elif monto > RETIRO_MAXIMO:
        print("El monto supera el máximo permitido.")

    elif monto > saldo:
        print("Saldo insuficiente.")

    else:
        saldo = saldo - monto
        retiros_exitosos += 1
        print("Retiro realizado exitosamente.")

    print("Saldo disponible: ₡", saldo)

    # Preguntar si desea continuar
    if saldo >= RETIRO_MINIMO:
        continuar = input("¿Desea realizar otro retiro? (s/n): ").lower()
    else:
        print("No tiene saldo suficiente para otro retiro.")
        continuar = "n"

# Resultados finales
print("\nResumen de operaciones")
print("Saldo restante: ₡", saldo)
print("Total de retiros exitosos:", retiros_exitosos)