from consola_calculo_imc import crear_persona
from calculadora_indices import calcular_IMC

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kg: "))
    altura_metros = float(input("Ingrese su altura en metros (ej. 1.75): "))
    altura_centimetros = int(altura_metros * 100)
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero:\nm: masculino\nf: femenino\n")
    actividad = input("Ingrese el numero segun corresponda a su actividad fisica: \n1: poco o ningún ejercicio\n2: ejercicio ligero (1 a 3 días a la semana)\n3: ejercicio moderado (3 a 5 días a la semana)\n4: deportista (6 -7 días a la semana)\n5: atleta (entrenamientos mañana y tarde)\n")

    persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

    response_IMC = calcular_IMC(persona["peso"], persona["altura_m"])
    print(response_IMC)