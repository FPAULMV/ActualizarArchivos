from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "VentasPetro":"SELECT * FROM NexusFuel_Petrodiesel.dbo.VentasPetro",
        "FLETE_PETRO":"SELECT * FROM NexusFuel_Petrodiesel.dbo.FLETE_PETRO",
        "Facturas_Canceladas":"SELECT * FROM NexusFuel_Petrodiesel.dbo.Facturas_Canceladas",
        "PetroSinservicios":"SELECT * FROM NexusFuel_Petrodiesel.dbo.PetroSinservicios"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)
