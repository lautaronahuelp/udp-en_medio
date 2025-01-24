from __future__ import print_function
import datetime

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
# 72.142.104.2 on port UDP 3061
# https://mnwb.connect24.com/default.aspx

ipServidor = "127.0.0.1" #dsc sg test
puertoServidor = 3061 #dsc sg test

estamSesion = datetime.datetime.now().strftime("LOG_%Y%m%d_%H%M%S")

class LadoServidor(DatagramProtocol):
    def __init__(self, arch, otro = None):
        self._otroLado = otro
        self._archivo = arch

    def setOtroLado(self, otro):
        self._otroLado = otro

    def datagramReceived(self, data, addr):
        linea = "(SER %s) recibido %r desde %s" % (datetime.datetime.now().strftime("%H:%M:%S_%d/%m/%y"), data.hex(), addr)
        self._archivo.write("%s\n" % linea)
        print(linea)
        self._otroLado.transport.write(data, (self._otroLado.ipCom, self._otroLado.puertoCom))

class LadoComunicador(DatagramProtocol):
    def __init__(self, ips, pus, arch, otro = None):
        self._otroLado = otro
        self._ipServ = ips
        self._puServ = pus
        self._archivo = arch
        self.ipCom = ""
        self.puertoCom = 0
    
    def setOtroLado(self, otro):
        self._otroLado = otro

    def datagramReceived(self, data, addr):
        self.ipCom = addr[0]
        self.puertoCom = addr[1]
        
        linea = "(COM %s) recibido %r desde %s" % (datetime.datetime.now().strftime("%H:%M:%S_%d/%m/%y"), data.hex(), addr)
        self._archivo.write("%s\n" % linea)
        print(linea)
        self._otroLado.transport.write(data, (self._ipServ, self._puServ))

try:
    print(estamSesion)
    nombreArchivo = estamSesion + ".txt"

    f = open(nombreArchivo, "w")

    ladoComunicador = LadoComunicador(ipServidor, puertoServidor, f)
    ladoServidor = LadoServidor(f, ladoComunicador)
    ladoComunicador.setOtroLado(ladoServidor)


    reactor.listenUDP(9999, ladoComunicador)
    reactor.listenUDP(9998, ladoServidor)
    reactor.run()
 
finally:
    f.close()
    print("Fin de programa.")