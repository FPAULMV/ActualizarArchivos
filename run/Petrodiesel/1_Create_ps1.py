import os

class Crearbat:
    def __init__(self) -> None:
        # Ruta de la carpeta donde se encuentran los archivos Python de los cuales se generará un archivo .bat
        self.carpeta_de_busqueda = r"C:\Users\Administrator\Sinergia\ServerDev - Server.53\Actualizar.Archivos\scrips\Petrodiesel"
        self.a = os.listdir(self.carpeta_de_busqueda)

    def archivos(self):
        excepciones = ['.env', 'srcbase.py', '.env', '.gitignore', '__pycache__']
        if excepciones:
            self.excepciones = excepciones
        
        self.lista_de_archivos = []
        for a in self.a:
            if a not in self.excepciones:
                self.lista_de_archivos.append(a)
    
        carpeta_actual = os.getcwd()
        file_type = '.ps1'
        # Esta es la ruta donde se activa el entorno virtual. 
        venv_path = "C:\\Users\\Administrator\\Sinergia\\ServerDev - Server.53\\Actualizar.Archivos\\Virtual.Env\\venv\\Scripts"
        # Esta es la ruta donde se encuentran los archivos de python que se van a ejecutar. 
        script_path = self.carpeta_de_busqueda
        # Contenido del archivo con placeholders
        template_content = f"""# Definir variables
        $VenvPath = "{venv_path}"
        $ScriptPath = "{script_path}"
        $ScriptName = "__file_name__"

        # Activar el entorno virtual
        Set-Location -Path $VenvPath
        .\\activate 
        Write-Output "----- ENTORNO VIRTUAL ACTIVADO -----"


        # Cambiar al directorio del script
        Set-Location -Path $ScriptPath

        # Ejecutar el script Python
        python.exe ".\\$ScriptName"

        # Desactivar el entorno virtual
        deactivate
        Write-Output "----- ENTORNO VIRTUAL DESACTIVADO -----"
        Write-Output "Finalizado!"
        """
        for i in self.lista_de_archivos:
            contenido = template_content.replace("__file_name__", i)
            new_name = i.replace(".py", file_type)
            new_file = os.path.join(carpeta_actual,new_name)
            with open(new_file,'w') as file:
                file.write(contenido)

        return True

if __name__ == '__main__':
    archivos = Crearbat()
    filtrados = archivos.archivos()
    print('Finalizado!')