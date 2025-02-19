from srcbase import src_exect
import os

if __name__ == "__main__":
    # Parametros de entrada.
    # Agregar del lado izquierdo el nombre de la hoja y del lado derecho la consulta.
    queries = {
        "Anticipos_vivos": "SELECT * FROM NexusFuel.dbo.Sinergia_Anticipos_vivos",
        "Ant-Fact-NC":"SELECT * FROM NexusFuel.dbo.Sinergia_Anticipos_F_NC",
        "AnticiposConBalance":"SELECT * FROM NexusFuel.dbo.Sinergia_Anticipos_con_Balance",
        "AnticiposBanco":"SELECT * FROM NexusFuel.dbo.AnticiposBank"
    }
    filename = os.path.basename(__file__).split('.')[0]

    # Ejecución
    src_exect(queries,filename)