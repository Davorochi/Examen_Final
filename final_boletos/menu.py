import random
import psycopg2
archivo = open("finalp.txt","a")
def loop():
    while True: 
        print("=====================================================")
        print(" DAVID ALEJANDRO OROZCO OROZCO, 201612199, Examen Final")
        print("======================================================")
        print("Ingresar como:")
        print("1. Administrador ")
        print("2. Usuario ")
        print("0. Salir ")
        try:
            option = input("Usted desea: ")
            if option =='1':
                admin = input("NOMBRE: ")
                contra = input("CONTRASEÑA: ")
                if admin == 'DAVID' and contra == 'BCSPN123':
                    print("==============BIENVENIDO ", admin , " ======================")
                    print("1. Crear Usuario")
                    print("2. Eliminar Usuario")
                    deseo = input(" Deseo: ")
                    if deseo == '1':
                        nuevo_usuario = input("Ingrese Nombre de Usuario: ")
                        nueva_contra = input("Ingrese Contraseña:")
                        print(" ==============Usuario Creado==========")
                    if deseo == '2':
                        print("1. Juan")
                        print("2. Jose")
                        print("3. Maria")
                        print("4. Luis")
                        print("5. Pedro")
                        print("6. Mely")
                        eliminar = input("Que usuario desea eliminar")
                        if eliminar == '1':
                            print("Usuario Eliminado")
                        if eliminar == '2':
                            print("Usuario Eliminado")
                        if eliminar == '3':
                            print("Usuario Eliminado")
                        if eliminar == '4':
                            print("Usuario Eliminado")
                        if eliminar == '5':
                            print("Usuario Eliminado")
                        if eliminar == '6':
                            print("Usuario Eliminado")
                        else:
                            print("Usuario no existe")
                else:
                    print(" El nombre o la contraseña no coinciden")       
            if option =='2':
                usua = input( "NOMBRE: ")
                contra1 = input("CONTRASENA: ")
                if contra1 == '123456':
                    print("===============  BIENVENIDO ", usua , "===============")
                    print("Aplicacion Venta de boletos para aerolinea")
                    print("===================MENU======================")
                    print("1 Primera Clase ")
                    print("2 Segunda Clase ")
                    print("3 Tercera Clase ")
                    print("0 Salir")
                    print("=======================================================")
                    Tipo_de_clase = input("Que Clase de Boleto Desea: " )
                    if Tipo_de_clase == '1':
                        print("Primera Clase")
                        print("=======================================================")
                        print("1 Comida ")
                        print("2 Bebida ")
                        print("3 Peliculas ")
                        print("4 Comida y bebida ")
                        print("5 Bebida y Pelicula ")
                        print("6 Peliculas y Comida ")
                        print("7 Comida, bebida y pelicula")
                        print("=======================================================")
                        Tipo_de_servicio = input("Que Tipo de servicio desea: " )
                        if Tipo_de_servicio == '1':
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            comida = int(comida)
                            print(" La cantidad de servicios es: ", comida)
                            if comida > 10:
                                Clase = 1
                                Total_comida = comida * 50
                                Descuento = (Total_comida)*0.10
                                Total = Total_comida - Descuento
                                print("El subtotal es: Q", Total_comida)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de comida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_comida) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_comida, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif comida <= 10 and comida > 0:
                                Clase = 1
                                Descuento = 0
                                Total = comida * 50
                                print("El total por los servicio de comida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '2':
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            bebida = int(bebida)
                            print(" La cantidad de servicios es: ", bebida)
                            if bebida > 10:
                                Clase = 1
                                Total_bebida = bebida * 35
                                Descuento = (Total_bebida)*0.10
                                Total = Total_bebida - Descuento
                                print("El subtotal es: Q", Total_bebida)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de bebida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_bebida) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_bebida, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif bebida <= 10 and bebida > 0:
                                Clase = 1
                                Descuento = 0
                                Total = bebida * 35
                                print("El total por los servicio de bebida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '3':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            peliculas = int(peliculas)
                            print(" La cantidad de servicios es: ", peliculas)
                            if peliculas > 10:
                                Clase = 1
                                Total_peliculas = peliculas * 70
                                Descuento = (Total_peliculas)*0.10
                                Total = Total_peliculas - Descuento
                                print("El subtotal es: Q", Total_peliculas)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de peliculas es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_peliculas) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_peliculas, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif peliculas <= 10 and peliculas > 0:
                                Clase = 1
                                Descuento = 0
                                Total = peliculas * 70
                                print("El total por los servicio de peliculas es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '4':
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            comida = int(comida)
                            bebida = int(bebida)
                            print(" La cantidad de servicios de comida es: ", comida)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            cb = comida + bebida
                            cb = int(cb)
                            print(" La cantidad de servicios es: ", cb)
                            if cb > 10:
                                Clase = 1
                                Total_comida = comida * 50
                                Total_bebida = bebida * 35
                                Descuento = (Total_comida + Total_bebida)*0.10
                                Total = (Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif cb <= 10 and cb > 0:
                                Clase = 1
                                Descuento = 0
                                Total_comida = comida * 50
                                Total_bebida = bebida * 35
                                Total = Total_comida + Total_bebida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '5':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            peliculas = int(peliculas)
                            bebida = int(bebida)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            pb = peliculas + bebida
                            pb = int(pb)
                            print(" La cantidad de servicios es: ", pb)
                            if pb > 10:
                                Clase = 1
                                Total_peliculas = peliculas * 70
                                Total_bebida = bebida * 35
                                Descuento = (Total_peliculas + Total_bebida)*0.10
                                Total = (Total_peliculas + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif pb <= 10 and pb > 0:
                                Clase = 1
                                Descuento = 0
                                Total_peliculas = peliculas * 70
                                Total_bebida = bebida * 35
                                Total = Total_peliculas + Total_bebida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '6':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            peliculas = int(peliculas)
                            comida = int(comida)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de comida es: ", comida)
                            pc = peliculas + comida
                            pc = int(pc)
                            print(" La cantidad de servicios es: ", pc)
                            if pc > 10:
                                Clase = 1
                                Total_peliculas = peliculas * 70
                                Total_comida = comida * 50
                                Descuento = (Total_peliculas + Total_comida)*0.10
                                Total = (Total_peliculas + Total_comida) - Descuento
                                Total_todo = Total_peliculas + Total_comida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif pc <= 10 and pc > 0:
                                Clase = 1
                                Descuento = 0
                                Total_peliculas = peliculas * 70
                                Total_comida = comida * 50
                                Total = Total_peliculas + Total_comida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '7':
                            comida = input("Ingrese la cantidad de servicios de Comida que desea: ")
                            bebida = input("Ingrese la cantidad de servicios de Bebida que desea: ")
                            peliculas = input("Ingrese la cantidad de servicios de Pelicula que desea: ")
                            comida = int(comida)
                            bebida = int(bebida)
                            peliculas = int(peliculas)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            print(" La cantidad de servicios de comida es: ", comida)
                            nt = comida + bebida + peliculas
                            nt = int(nt)
                            print(" La cantidad de servicios es: ", nt)
                            if nt > 10:
                                Clase = 1
                                Total_peliculas = peliculas * 70
                                Total_comida = comida * 50
                                Total_bebida = bebida * 35
                                Descuento = (Total_peliculas + Total_comida + Total_bebida)*0.15
                                Total = (Total_peliculas + Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif nt <= 10 and nt > 0:
                                Clase = 1
                                Total_peliculas = peliculas * 70
                                Total_comida = comida * 50
                                Total_bebida = bebida * 35
                                Descuento = (Total_peliculas + Total_comida + Total_bebida)*0.05
                                Total = (Total_peliculas + Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                        else:
                            print("Escoja una opcion correcta: ")  
                    elif Tipo_de_clase == '2':
                        print("Segunda Clase")
                        print("=======================================================")
                        print("1 Comida ")
                        print("2 Bebida ")
                        print("3 Peliculas ")
                        print("4 Comida y bebida ")
                        print("5 Bebida y Pelicula ")
                        print("6 Peliculas y Comida ")
                        print("7 Comida, bebida y pelicula")
                        print("=======================================================")
                        Tipo_de_servicio = input("Que Tipo de servicio desea: " )
                        if Tipo_de_servicio == '1':
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            comida = int(comida)
                            print(" La cantidad de servicios es: ", comida)
                            if comida > 10:
                                Clase = 2
                                Total_comida = comida * 40
                                Descuento = (Total_comida)*0.10
                                Total = Total_comida - Descuento
                                print("El subtotal es: Q", Total_comida)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de comida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_comida) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_comida, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif comida <= 10 and comida > 0:
                                Clase = 2
                                Descuento = 0
                                Total = comida * 40
                                print("El total por los servicio de comida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '2':
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            bebida = int(bebida)
                            print(" La cantidad de servicios es: ", bebida)
                            if bebida > 10:
                                Clase = 2
                                Total_bebida = bebida * 25
                                Descuento = (Total_bebida)*0.10
                                Total = Total_bebida - Descuento
                                print("El subtotal es: Q", Total_bebida)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de bebida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_bebida) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_bebida, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif bebida <= 10 and bebida > 0:
                                Clase = 2
                                Descuento = 0
                                Total = bebida * 25
                                print("El total por los servicio de bebida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '3':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            peliculas = int(peliculas)
                            print(" La cantidad de servicios es: ", peliculas)
                            if peliculas > 10:
                                Clase = 2
                                Total_peliculas = peliculas * 55
                                Descuento = (Total_peliculas)*0.10
                                Total = Total_peliculas - Descuento
                                print("El subtotal es: Q", Total_peliculas)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de peliculas es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_peliculas) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_peliculas, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif peliculas <= 10 and peliculas > 0:
                                Clase = 2
                                Descuento = 0
                                Total = peliculas * 55
                                print("El total por los servicio de peliculas es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '4':
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            comida = int(comida)
                            bebida = int(bebida)
                            print(" La cantidad de servicios de comida es: ", comida)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            cb = comida + bebida
                            cb = int(cb)
                            print(" La cantidad de servicios es: ", cb)
                            if cb > 10:
                                Clase = 2
                                Total_comida = comida * 40
                                Total_bebida = bebida * 25
                                Descuento = (Total_comida + Total_bebida)*0.10
                                Total = (Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif cb <= 10 and cb > 0:
                                Clase = 2
                                Descuento = 0
                                Total_comida = comida * 40
                                Total_bebida = bebida * 25
                                Total = Total_comida + Total_bebida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '5':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            peliculas = int(peliculas)
                            bebida = int(bebida)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            pb = peliculas + bebida
                            pb = int(pb)
                            print(" La cantidad de servicios es: ", pb)
                            if pb > 10:
                                Clase = 2
                                Total_peliculas = peliculas * 55
                                Total_bebida = bebida * 25
                                Descuento = (Total_peliculas + Total_bebida)*0.10
                                Total = (Total_peliculas + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif pb <= 10 and pb > 0:
                                Clase = 2
                                Descuento = 0
                                Total_peliculas = peliculas * 55
                                Total_bebida = bebida * 25
                                Total = Total_peliculas + Total_bebida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '6':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            peliculas = int(peliculas)
                            comida = int(comida)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de comida es: ", comida)
                            pc = peliculas + comida
                            pc = int(pc)
                            print(" La cantidad de servicios es: ", pc)
                            if pc > 10:
                                Clase = 2
                                Total_peliculas = peliculas * 55
                                Total_comida = comida * 40
                                Descuento = (Total_peliculas + Total_comida)*0.10
                                Total = (Total_peliculas + Total_comida) - Descuento
                                Total_todo = Total_peliculas + Total_comida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif pc <= 10 and pc > 0:
                                Clase = 2
                                Descuento = 0
                                Total_peliculas = peliculas * 55
                                Total_comida = comida * 40
                                Total = Total_peliculas + Total_comida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '7':
                            comida = input("Ingrese la cantidad de servicios de Comida que desea: ")
                            bebida = input("Ingrese la cantidad de servicios de Bebida que desea: ")
                            peliculas = input("Ingrese la cantidad de servicios de Pelicula que desea: ")
                            comida = int(comida)
                            bebida = int(bebida)
                            peliculas = int(peliculas)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            print(" La cantidad de servicios de comida es: ", comida)
                            nt = comida + bebida + peliculas
                            nt = int(nt)
                            print(" La cantidad de servicios es: ", nt)
                            if nt > 10:
                                Clase = 2
                                Total_peliculas = peliculas * 55
                                Total_comida = comida * 40
                                Total_bebida = bebida * 25
                                Descuento = (Total_peliculas + Total_comida + Total_bebida)*0.10
                                Total = (Total_peliculas + Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif nt <=10 and nt >0:
                                Clase = 2
                                Descuento = 0
                                Total_peliculas = peliculas * 55
                                Total_comida = comida * 40
                                Total_bebida = bebida * 25
                                Total = (Total_peliculas + Total_comida + Total_bebida)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        else:
                            print("Escoja una opcion correcta: ")  
                    elif Tipo_de_clase == '3':
                        print("Tercera Clase")
                        print("=======================================================")
                        print("1 Comida ")
                        print("2 Bebida ")
                        print("3 Peliculas ")
                        print("4 Comida y bebida ")
                        print("5 Bebida y Pelicula ")
                        print("6 Peliculas y Comida ")
                        print("7 Comida, bebida y pelicula")
                        print("=======================================================")
                        Tipo_de_servicio = input("Que Tipo de servicio desea: " )
                        if Tipo_de_servicio == '1':
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            comida = int(comida)
                            print(" La cantidad de servicios es: ", comida)
                            if comida > 10:
                                Clase = 3
                                Total_comida = comida * 25
                                Descuento = (Total_comida)*0.10
                                Total = Total_comida - Descuento
                                print("El subtotal es: Q", Total_comida)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de comida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_comida) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_comida, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif comida <= 10 and comida > 0:
                                Clase = 3
                                Descuento = 0
                                Total = comida * 25
                                print("El total por los servicio de comida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '2':
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            bebida = int(bebida)
                            print(" La cantidad de servicios es: ", bebida)
                            if bebida > 10:
                                Clase = 3
                                Total_bebida = bebida * 10
                                Descuento = (Total_bebida)*0.10
                                Total = Total_bebida - Descuento
                                print("El subtotal es: Q", Total_bebida)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de bebida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_bebida) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_bebida, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif bebida <= 10 and bebida > 0:
                                Clase = 3
                                Descuento = 0
                                Total = bebida * 10
                                print("El total por los servicio de bebida es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '3':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            peliculas = int(peliculas)
                            print(" La cantidad de servicios es: ", peliculas)
                            if peliculas > 10:
                                Clase = 3
                                Total_peliculas = peliculas * 25
                                Descuento = (Total_peliculas)*0.10
                                Total = Total_peliculas - Descuento
                                print("El subtotal es: Q", Total_peliculas)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicio de peliculas es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_peliculas) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_peliculas, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif peliculas <= 10 and peliculas > 0:
                                Clase = 3
                                Descuento = 0
                                Total = peliculas * 25
                                print("El total por los servicio de peliculas es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '4':
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            comida = int(comida)
                            bebida = int(bebida)
                            print(" La cantidad de servicios de comida es: ", comida)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            cb = comida + bebida
                            cb = int(cb)
                            print(" La cantidad de servicios es: ", cb)
                            if cb > 10:
                                Clase = 3
                                Total_comida = comida * 25
                                Total_bebida = bebida * 10
                                Descuento = (Total_comida + Total_bebida)*0.10
                                Total = (Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif cb <= 10 and cb > 0:
                                Clase = 3
                                Descuento = 0
                                Total_comida = comida * 25
                                Total_bebida = bebida * 10
                                Total = Total_comida + Total_bebida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '5':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            bebida = input("Ingrese cantidad de servicios de bebida que desea: ")
                            peliculas = int(peliculas)
                            bebida = int(bebida)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            pb = peliculas + bebida
                            pb = int(pb)
                            print(" La cantidad de servicios es: ", pb)
                            if pb > 10:
                                Clase = 3
                                Total_peliculas = peliculas * 25
                                Total_bebida = bebida * 10
                                Descuento = (Total_peliculas + Total_bebida)*0.10
                                Total = (Total_peliculas + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif pb <= 10 and pb > 0:
                                Clase = 3
                                Descuento = 0
                                Total_peliculas = peliculas * 25
                                Total_bebida = bebida * 10
                                Total = Total_peliculas + Total_bebida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '6':
                            peliculas = input("Ingrese cantidad de servicios de peliculas que desea: ")
                            comida = input("Ingrese cantidad de servicios de comida que desea: ")
                            peliculas = int(peliculas)
                            comida = int(comida)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de comida es: ", comida)
                            pc = peliculas + comida
                            pc = int(pc)
                            print(" La cantidad de servicios es: ", pc)
                            if pc > 10:
                                Clase = 3
                                Total_peliculas = peliculas * 25
                                Total_comida = comida * 25
                                Descuento = (Total_peliculas + Total_comida)*0.10
                                Total = (Total_peliculas + Total_comida) - Descuento
                                Total_todo = Total_peliculas + Total_comida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif pc <= 10 and pc > 0:
                                Clase = 3
                                Descuento = 0
                                Total_peliculas = peliculas * 25
                                Total_comida = comida * 25
                                Total = Total_peliculas + Total_comida
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        if Tipo_de_servicio == '7':
                            comida = input("Ingrese la cantidad de servicios de Comida que desea: ")
                            bebida = input("Ingrese la cantidad de servicios de Bebida que desea: ")
                            peliculas = input("Ingrese la cantidad de servicios de Pelicula que desea: ")
                            comida = int(comida)
                            bebida = int(bebida)
                            peliculas = int(peliculas)
                            print(" La cantidad de servicios de peliculas es: ", peliculas)
                            print(" La cantidad de servicios de bebida es: ", bebida)
                            print(" La cantidad de servicios de comida es: ", comida)
                            nt = comida + bebida + peliculas
                            nt = int(nt)
                            print(" La cantidad de servicios es: ", nt)
                            if nt > 10:
                                Clase = 3
                                Total_peliculas = peliculas * 25
                                Total_comida = comida * 25
                                Total_bebida = bebida * 10
                                Descuento = (Total_peliculas + Total_comida + Total_bebida)*0.10
                                Total = (Total_peliculas + Total_comida + Total_bebida) - Descuento
                                Total_todo = Total_peliculas + Total_comida + Total_bebida
                                print("El subtotal es: Q", Total_todo)
                                print("El descuento es: Q", Descuento)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total_todo) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total_todo, Descuento, Total))
                                conn.commit()
                                conn.close()
                            elif nt <=10 and nt >0:
                                Clase = 3
                                Descuento = 0
                                Total_peliculas = peliculas * 25
                                Total_comida = comida * 25
                                Total_bebida = bebida * 10
                                Total = (Total_peliculas + Total_comida + Total_bebida)
                                print("El total por los servicios es de: Q", Total)
                                numero = Total
                                identificador = format(id(numero), 'x')
                                print("El identificador de la venta es: ", identificador)
                                print("=======================================================")
                                archivo.write('Usted escogio la clase ' + str(Clase) + ', el subtotal de los servivios es Q'+str(Total) +  ', se desconto  Q'+str(Descuento) + ' por lo que su total es Q'+ str(Total) +  ' \n ')
                                conn = psycopg2.connect(database="Final", user="postgres", password="BCSPN123",host='localhost', port= '5432')
                                conn.autocommit = True
                                cursor = conn.cursor()
                                cursor.execute('''insert into facturas( clase, numero_factura, subtotal, descuento, total) values (%s,%s,%s,%s,%s)''',
                                (Clase, identificador, Total, Descuento, Total))
                                conn.commit()
                                conn.close()
                        else:
                            print("Escoja una opcion correcta: ")
                else:
                    print("Usuario o contraseña incorrecta...")
            if option == '0':
                print("Salir...")
                print("")
                print("Saliendo...\n")
                break
            input("\nPresiona ENTER para continuar...")
        except:
            print("Operacion Invalida")
            print("=======================================================")