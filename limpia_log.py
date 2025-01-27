import sys
sys.argv[1]

try:
    f_nombre = sys.argv[1].split("LOG_")[1]
    f_entrada = open(sys.argv[1], "r")
    f_salida = open("LIM_" + f_nombre, "w")

    for l in f_entrada:
        linea = (l.split(" recibido "))[1]
        linea = linea.split(" desde ")[0]

        #'1416ffffff7e003610300000000054a48e80 00 09 da 00 005b4eb094050000000000 01 2012 0081303839353433343130313233343633363336303234'
        #'1416ffffff7e001d10710000000067936340 00 04 1a 00 034f1d0338023000018102 01'
        lineaLista = list(linea)
        lineaLista.insert(45,' ')
        lineaLista.insert(43,' ')
        lineaLista.insert(41,' ')
        lineaLista.insert(39,' ')
        lineaLista.insert(37,' ')
        #>>> hash = '355879ACB6'
        #>>> hashlist = list(hash)
        #>>> hashlist.insert(4, '-')
        #>>> ''.join(hashlist)
        #'3558-79ACB6
        f_salida.write(''.join(lineaLista) + "\n")



    f_entrada.close()
    f_salida.close()
finally:
    f_entrada.close()
    f_salida.close()
