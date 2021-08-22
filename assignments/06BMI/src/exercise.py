def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    IMC= peso/altura**2
    if peso >0 and altura>0:
        if IMC<20:
            print ("PESO BAJO")
        elif IMC>=20 and IMC<25:
            print ("NORMAL")
        elif IMC>=25 and IMC<30:
            print ("SOBREPESO")
        elif IMC >=30 and IMC<40:
            print ("OBESIDAD")
        else: print("OBESIDAD MORBIDA")
    else: print ("Revisa tus datos, alguno de ellos es erróneo.")
    





if __name__=='__main__':
    main()