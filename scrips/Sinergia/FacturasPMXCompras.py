from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "ComprasPMX": "SELECT * FROM NexusFuel.dbo.Sinergia_Fpemex",
        "Servicios":"SELECT * FROM NexusFuel.dbo.Sinergia_Servicios",
        "Canceladas.":"SELECT * FROM NexusFuel.dbo.SinergiaInvoiceCancelPMX"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)
