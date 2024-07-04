def verificar_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "VLAN en el rango normal"
    elif 1006 <= vlan <= 4094:
        return "VLAN en el rango extendido"
    else:
        return "Número de VLAN fuera de rango"

if __name__ == "__main__":
    vlan = int(input("Ingrese el número de VLAN: "))
    resultado = verificar_vlan(vlan)
    print(resultado)
