from serial import Serial
from time import sleep



def mandaNomeArduino(nome):
	nome = nome.split('.')[0]
	meu_serial = Serial('/dev/cu.usbmodem11101', 9600)
	sleep(2)
	nome = "Face reconhecida: " + nome + "\n"
	meu_serial.write(nome.encode("UTF-8"))
	print(nome)
	return 