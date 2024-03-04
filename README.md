# app-reconocimiento-facial
- App para el registro y reconocimiento facil.

### Creación entorno virtual
* cmd : `python -m venv ven_reconocimiento_facial` 

#### Activación entorno vritual 
 1. primero nos dirigimos a la carpeta ven_reconocimiento_facial asi: cd ven_reconocimiento_facia.

 2. luego a la carpeta Scripts y luego a activate asi: Scripts\activate.

  fin.


### Reestauración del proyecto mediante bibliotecas

- Antes de instalar las dependencias cree y active el entorno virtual como `ven_reconocimiento_facial`.
Para instalar la lista de dependencias en cualquier otra instalación de Python dirijase a
la terminal `cmd` y ejecute el comando `pip install -r requerimientos.txt`

### Bibliotecas
* PyMysql - comando: `pip install pymysql`

#### Generar archivo de bibliotecas y dependencias
- comando: `python -m pip freeze > requerimientos.txt`

### Apuntes 
1- (1049, "Unknown database 'reconocimiento_facial'")