from srcbase import src_exect
import os

if __name__ == "__main__":

    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "SinergiaFCasadas": "select * from NexusFuel.dbo.sinergiafcasadas"
    }

    # Parametros de entrada.
    filename = os.path.basename(__file__).split('.')[0]
    src_exect(queries,filename)