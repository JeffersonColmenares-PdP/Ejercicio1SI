# PASOS PARA EJECUTAR PROYECTO

# 1. Descomprimir el .zip CampusVirtualDiepo.zip

# 2. Desde Visual Studio Code abrir la carpeta CRUD

# 3. Ejecutar los siguiente comandos
# -----------------------------------------------
# crear el entorno v
python -m venv .venv

# verificar instalacion python
python --version

# activar entorno v
.venv\Scripts\activate  

# SI TE SALE ERROR AL EJECUTAR EL COMANDO ANTERIOR (SOLO SI SALE ERROR SINO AVANZAR AL SIGUIENTE COMANDO)
# ABRIR WINDOWS POWERSHELL COMO ADMINISTRADOR E INGRESAR ESTOS COMANDOS
    Get-ExecutionPolicy -list
    Set-ExecutionPolicy RemoteSigned -Force
# VOLVER A EJECUTAR 
.venv\Scripts\activate  

# Instalar dependencias desde un requirements.txt
pip install -r requirements.txt

# Buscar entre los archivos ---> application.py y cambiar el host (este debe ser la ip del computador de cada uno)
    if __name__ == '__main__':
        application.run(debug=True, host='192.168.241.1', port=5000)

# ejecutar entorno
python .\application.py
-----------------------------------------------

# 4. En la carpeta CampusVirtualDiepo
# Ingresar carpeta educacion.policia.edu.co y abrir index.html. En la línea 59 cambiar nuevamente la ip en el fetch
    --> 'http://192.168.241.1:5000/usuario/crear'

# 5. En la carpeta estructuraCorreo
Esta el mensaje.html --> Esta es la estructura del correo que le llegaria al usuario, es lo que se que se envía en la página https://emkei.cz/ 
Esta users.txt --> Son las credenciales para abrir el correo electronico