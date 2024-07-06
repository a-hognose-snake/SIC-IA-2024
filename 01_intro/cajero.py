# Simulador de cajero automático

cuentas = [
    ["12345678", 5000],
    ["11111111", 2000],
    ["22222222", 3000]
]

def encontrar_cuenta(numero_cuenta):
    for cuenta in cuentas:
        if cuenta[0] == numero_cuenta:
            return cuenta
    return None

def consultar_saldo(cuenta):
    saldo = cuenta[1]
    print(f"Saldo actual: ${saldo}")

def retirar_dinero(cuenta):
    cantidad = int(input("Cantidad a retirar: $"))
    if cantidad <= cuenta[1]:
        cuenta[1] -= cantidad
        print(f"Retiro de ${cantidad} Ok. \nSaldo actual: ${cuenta[1]}")
    else:
        print("Fondos insuficientes :c")

def depositar_dinero(cuenta):
    cantidad = int(input("Cantidad a depositar: $"))
    cuenta[1] += cantidad
    print(f"Depósito de ${cantidad} Ok. \nSaldo actual: ${cuenta[1]}")

def transferir_dinero(cuenta):
    cuenta_destino_num = input("Número de cuenta de destino: ")
    cuenta_destino = encontrar_cuenta(cuenta_destino_num)
    if cuenta_destino:
        cantidad = int(input("Cantidad a transferir: $"))
        if cantidad <= cuenta[1]:
            cuenta[1] -= cantidad
            cuenta_destino[1] += cantidad
            print(f"Transferencia de ${cantidad} a la cuenta {cuenta_destino_num} Ok. \nSaldo actual: ${cuenta[1]}.")
        else:
            print("Fondos insuficientes :c")
    else:
        print("Número de cuenta de destino no válida.")

def cajero_automatico():
    print("Simulador de cajero automático")
    numero_cuenta = input("Número de cuenta: ")
    
    cuenta = encontrar_cuenta(numero_cuenta)
    if cuenta is None:
        print("Número de cuenta no válido.")
        return
    
    while True:
        print("\nOperaciones:")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Transferir dinero a otra cuenta")
        print("5. Salir")
        
        opcion = input("\nOperación: ")
        
        if opcion == "1":
            consultar_saldo(cuenta)
        elif opcion == "2":
            retirar_dinero(cuenta)
        elif opcion == "3":
            depositar_dinero(cuenta)
        elif opcion == "4":
            transferir_dinero(cuenta)
        elif opcion == "5":
            print("Fin.")
            break
        else:
            print("Operación no válida.")

# Main
cajero_automatico()
