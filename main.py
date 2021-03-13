import os 
import sys

## variables globales

nombre_archivo = sys.argv[1]
try:
    handler = open(nombre_archivo)
except FileNotFoundError:
    print('File not fuond:', nombre_archivo)
    exit()

if __name__ == "__main__":

    for linea in handler:
        
        cmd = './ip_fraud.sh {}'.format(linea)

        os.system(cmd)
        
