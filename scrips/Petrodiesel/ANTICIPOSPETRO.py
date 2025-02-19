from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "Anticipo_NC": "SELECT * FROM NexusFuel_Petrodiesel.dbo.Anticipo_NC",
        "Anticipos":"SELECT * FROM NexusFuel_Petrodiesel.dbo.Anticipos"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)
