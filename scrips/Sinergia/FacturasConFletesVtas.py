from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "DatosMaestros": "SELECT * FROM NexusFuel.dbo.Fact_Flete_Sinergia",
        "DatosM_Cancelados":"SELECT * FROM NexusFuel.dbo.Fact1Sinergia_cancelado",
        "SinergiaServicios":"SELECT * FROM NexusFuel.dbo.Sinergia_Servicios",
        "SinServicios":"SELECT * FROM NexusFuel.dbo.Sinergia_SinServicios"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)
