dinero = 2000
precio_helado = 100
hambre = edad
edad = 18
helados_consumidos = 0

while (hambre) < 85 and (dinero - precio_helado) > 0:
    dinero = dinero - precio_helado
    precio_helado = precio_helado + (precio_helado * 0.2)
    helados_consumidos += 1
    hambre = hambre + edad
    if (hambre + edad) >=100:
        break
    print("Helados consumidos:" + str(helados_consumidos))
    print("Dinero restante" + str(dinero))
    print("Nivel de saciedad:" +  str(hambre))



