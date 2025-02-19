# Definir variables
        $VenvPath = "C:\Users\Administrator\Sinergia\ServerDev - Server.53\Actualizar.Archivos\Virtual.Env\venv\Scripts"
        $ScriptPath = "C:\Users\Administrator\Sinergia\ServerDev - Server.53\Actualizar.Archivos\scrips\Logistica"
        $ScriptName = "Autoabasto.py"

        # Activar el entorno virtual
        Set-Location -Path $VenvPath
        .\activate 
        Write-Output "----- ENTORNO VIRTUAL ACTIVADO -----"


        # Cambiar al directorio del script
        Set-Location -Path $ScriptPath

        # Ejecutar el script Python
        python.exe ".\$ScriptName"

        # Desactivar el entorno virtual
        deactivate
        Write-Output "----- ENTORNO VIRTUAL DESACTIVADO -----"
        Write-Output "Finalizado!"
        