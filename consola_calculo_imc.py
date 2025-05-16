from calculadora_indices import calcular_IMC

def crear_persona(peso: float, altura_m: float, altura_cm: int, edad:int, genero:str, actividad:str):
    try:
        if genero.lower() == 'm':
            if actividad.replace(" ","") == "1":
                valor_actividad = 1.2
            elif actividad.replace(" ","") == "2":
                valor_actividad = 1.375
            elif actividad.replace(" ","") == "3":
                valor_actividad = 1.55
            elif actividad.replace(" ","") == "4":
                valor_actividad = 1.72
            elif actividad.replace(" ","") == "5":
                valor_actividad = 1.9

            hombre={
                "peso": peso,
                "altura_m": altura_m,
                "altura_cm": altura_cm,
                "edad": edad,
                "valor_genero_GC": 10.8,
                "valor_genero_TMB": 5,
                "valor_actividad": valor_actividad}
            return hombre

        elif genero.lower() == 'f':
            if actividad.replace(" ","") == "1":
                valor_actividad = 1.2
            elif actividad.replace(" ","") == "2":
                valor_actividad = 1.375
            elif actividad.replace(" ","") == "3":
                valor_actividad = 1.55
            elif actividad.replace(" ","") == "4":
                valor_actividad = 1.72
            elif actividad.replace(" ","") == "5":
                valor_actividad = 1.9

            mujer={
                "peso":peso,
                "altura_m":altura_m,
                "altura_cm":altura_cm,
                "edad":edad,
                "valor_genero_GC": 0,
                "valor_genero_TMB": -161,
                "valor_actividad": valor_actividad}
            return mujer
    
    except TypeError as tp:
        return tp
    except ValueError as ve:
        return ve


# persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

# response_IMC = calcular_IMC(persona["peso"], persona["altura_m"])
# print(response_IMC)