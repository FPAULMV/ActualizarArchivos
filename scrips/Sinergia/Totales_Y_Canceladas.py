from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "VentasTotales":"SELECT * FROM NexusFuel.dbo.Sinergia_FSales",
        "SinServicios":"SELECT * FROM NexusFuel.dbo.Sinergia_SinServicios",
        "Canceladas":"SELECT * FROM NexusFuel.dbo.Sinergia_CancelFSales"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)
