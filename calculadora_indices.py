hombre={
    "peso":81,
    "altura_m":1.75,
    "altura_cm":175,
    "edad":20,
    "valor_genero_GC": 10.8,
    "valor_genero_TMB": 5,
    "valor_actividad": 1.55}
mujer={
    "peso":58,
    "altura_m":1.69,
    "altura_cm":169,
    "edad":21,
    "valor_genero_GC": 0,
    "valor_genero_TMB": -161,
    "valor_actividad": 1.725}

def calcular_IMC(peso: float, altura: float) -> float:
    """
    Calcula el IMC en base a:
        - peso/(altura)**2\n
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura (float): Altura de la persona en metros.\n
    Retorno IMC(float) Índice de masa corporal de la persona, type_imc(str) la categoria a la que pertenece segun el IMC calculado\n

    Valor de IMC Categoría:\n
    <16 = Delgadez severa\n 
    16 - 16.99 = Delgadez moderada\n
    17 - 18.49 = Delgadez aceptable\n
    18.5 - 24.99 = Peso normal\n
    25 - 29.99 = Sobrepeso\n
    30 - 34.99 = Obesidad tipo I\n
    35 - 39.99 = Obesidad tipo II\n
    40 - 49.99 = Obesidad tipo III o mórbida\n
    >50 = Obesidad tipo IV o extrema\n
    """
    
    try:
        IMC = round(float(peso/(altura)**2),2)
        
        if IMC < 16:
            return IMC,"Delgadez severa"
        elif 16 < IMC < 16.99:
            return IMC,"Delgadez moderada"
        elif 17 < IMC < 18.49:
            return IMC,"Delgadez aceptable"
        elif 18.5 < IMC < 24.99:
            return IMC,"Peso normal"
        elif 25 < IMC < 29.99:
            return IMC,"Sobrepeso"
        elif 30 < IMC < 34.99:
            return IMC,"Obesidad tipo I" 
        elif 35 < IMC < 39.99:
            return IMC,"Obesidad tipo II"
        elif 40 < IMC < 49.99: 
            return IMC,"Obesidad tipo III o mórbida"
        elif IMC > 50: 
            return IMC,"Obesidad tipo IV o extrema"
        else:
            return IMC,"Valores no contemplados"
        
    except ZeroDivisionError as zd:
        return f"Error de divison por cero: {zd}"
    except ValueError as ve:
        return ve
    except TypeError as tp:
        return f"Error de tipado {tp}"
    
imc_hombre = calcular_IMC(hombre["peso"], hombre["altura_m"])
imc_mujer = calcular_IMC(mujer["peso"], mujer["altura_m"])


def calcular_porcentaje_grasa(IMC:float, peso:float, altura:float, edad:int, valor_genero:float) -> float:
    """
    %GC: Medida (porcentual) que permite establecer si una persona tiene un nivel adecuado o excesivo de grasa en su cuerpo.\n
        - %GC = 1.2 * IMC + 0.23 * edad(años) - 5.4 - valor_genero
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura (float): Altura de la persona en metros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (float): Valor que varía según el género de la persona: en caso de ser masculino debe ser 10.8 y en caso de ser femenino debe ser 0.\n

    Retorno (float): El porcentaje de grasa que tiene el cuerpo de la persona.\n
    """
    GC = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero

    """
    rango_de_edad: 20 - 29; hombres: 11% - 20%; mujeres: 16% - 28%
    rango_de_edad: 30 - 39; hombres: 12% - 21%; mujeres: 17% - 29%
    rango_de_edad: 40 - 49; hombres: 14% - 23%; mujeres: 18% - 30%
    rango_de_edad: 50 - 59; hombres: 15% - 24%; mujeres: 19% - 31%
    """
    # if 20 < edad < 29 and 11< GC <20 and valor_genero == 10.8:
    #     pass
    return round(float(GC),2)


cg_hombre = calcular_porcentaje_grasa(imc_hombre[0],hombre["peso"],hombre["altura_m"], hombre["edad"], hombre["valor_genero_GC"]) # Hombre
cg_mujer = calcular_porcentaje_grasa(imc_mujer[0], mujer["peso"], mujer["altura_m"], mujer["edad"], mujer["valor_genero_GC"]) # Mujer
# print(f"{cg_hombre}%")
# print(f"{cg_mujer}%")

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:int)-> float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo
        - TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero 
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura (float): Altura de la persona en centimetros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (int): Valor que varía según el género de la persona:
        - En caso de ser masculino: 5
        - En caso de ser femenino: -161\n
    Retornado (float) La cantidad de calorías que la persona quema en reposo.\n
    """
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    # TMB = ((10*peso) + (6.25*altura)) - ((5*edad) + valor_genero)
            # (810    +    10,9375)   -    (100    +     5)
            #       820.9375    -   105
            #               715.9375
    return round(TMB,2)

TMB_hombre = calcular_calorias_en_reposo(hombre["peso"],hombre["altura_cm"],hombre["edad"],hombre["valor_genero_TMB"])
TMB_mujer = calcular_calorias_en_reposo(mujer["peso"], mujer["altura_cm"], mujer["edad"], mujer["valor_genero_TMB"])
# print(f"{TMB_hombre} cal")
# print(f"{TMB_mujer} cal")

def calcular_calorias_en_actividad(TMB:float, peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float) -> float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física:
        - TMB_(actividad_fisica) = TMB * valor_actividad 

    *parm TMB (float): Tasa metabólica basal.\n
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura (float): Altura de la persona en centimetros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (int): Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.\n
    *parm valor_actividad (float): Valor que depende de la actividad física semanal y toma los valores:
        - 1.2: poco o ningún ejercicio 
        - 1.375: ejercicio ligero (1 a 3 días a la semana) 
        - 1.55: ejercicio moderado (3 a 5 días a la semana) 
        - 1.72: deportista (6 -7 días a la semana) 
        - 1.9: atleta (entrenamientos mañana y tarde. 

    Retorno (float): La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente. 
    """

    TMB_actividad_fisica = TMB * valor_actividad
    return round(TMB_actividad_fisica,2)

tmb_actividad_fisica_hombre = calcular_calorias_en_actividad(TMB_hombre, hombre["peso"], hombre["altura_cm"], hombre["edad"], hombre["valor_genero_TMB"], hombre["valor_actividad"])
tmb_actividad_fisica_mujer = calcular_calorias_en_actividad(TMB_mujer, mujer["peso"], mujer["altura_cm"], mujer["edad"], mujer["valor_genero_TMB"], mujer["valor_actividad"])
# print(f"{tmb_actividad_fisica_hombre} cal")
# print(f"{tmb_actividad_fisica_mujer} cal")

def consumo_calorias_recomendado_para_adelgazar(TMB: float, peso: float, altura: float, edad: int, valor_genero: int) -> str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar.\n
        - calorias_recomendadas: TMB - 15% o 20%

    *parm TMB (float): Tasa metabólica basal.\n
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura (float): Altura de la persona en centimetros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (int): Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.\n
    """
    valor_minimo_para_adelgazar = (TMB*15)/100
    valor_maximo_para_adelgazar = (TMB*20)/100
    
    calorias_minimas_recomendadas_para_adelgazar = round(TMB - valor_minimo_para_adelgazar,2)
    calorias_maximas_recomendadas_para_adelgazar = round(TMB - valor_maximo_para_adelgazar,2)

    return f"Para adelgazar es recomendado que consumas entre: {calorias_maximas_recomendadas_para_adelgazar} y {calorias_minimas_recomendadas_para_adelgazar} calorías al día." 

recom_para_adelgazar_hombres = consumo_calorias_recomendado_para_adelgazar(TMB_hombre,hombre["peso"], hombre["altura_cm"], hombre["edad"],hombre["valor_genero_TMB"])
recom_para_adelgazar_mujeres = consumo_calorias_recomendado_para_adelgazar(TMB_mujer,mujer["peso"], mujer["altura_cm"], mujer["edad"],mujer["valor_genero_TMB"])

# print(recom_para_adelgazar_hombres)
# print(recom_para_adelgazar_mujeres)