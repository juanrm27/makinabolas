import makinabolas

maquina = makinabolas.MakinaBolas()
SEGUIR = True

while SEGUIR:
    moneda = input('Introduce una moneda válida (Euro_1)')
    if maquina.aceptar_moneda(moneda):
        try:
            giro = int(input('Gira la manivela unos grados (360 = OK)'))
        except ValueError:
            print('Sólo se admiten números enteros.')
            giro = 0

        if maquina.girar_manivela(giro):
            print(maquina.soltar_bola())
            print(f'Quedan {maquina.deposito} bolas')
            print(f'Hay {maquina.monedero} Euros\n\n')
        else:
            print('Debes girar 360º si quieres una bola. Operación cancelada.')
            continue
    else:
        print('Debes introducir 1€ si quieres una bola. Operación cancelada.')
        continue
    resp = input('¿Quieres más bolas s/n?').upper()
    if resp == 'N'     :
        SEGUIR = False
