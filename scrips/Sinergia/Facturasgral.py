from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "Facturasgral": "SELECT * FROM NexusFuel.dbo.Facturasgral"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)
