from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "Sinergia_NCSAPAnticipos": "SELECT * FROM NexusFuel.dbo.Sinergia_NCSAPAnticipos",
        "Sinergia_ANT_NC_SAP":"SELECT * FROM NexusFuel.dbo.Sinergia_ANTNCSAP"
    }   
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)