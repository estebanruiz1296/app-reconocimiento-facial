# app-reconocimiento-facial
- App para el registro y reconocimiento facil. Se recomienda el uso de la version de python 3.8.10 
`Windows installer (64-bit)`:[Descarga recomendada](https://www.python.org/downloads/release/python-3810/), 
para tener mejor compatividad con mediapipe.

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
* PyMysql 1.1.0 - comando: `pip install pymysql`
* decouple 0.0.7 - comando: `pip install decouple`
* opencv-python 4.9.0.80 - comando: `pip install opencv-python`
* mediapipe 0.8.8.1 - comando: `pip install mediapipe==0.8.8.1`
* bcrypt 4.1.2 - comando: `pip install bcrypt`
* face-recognition 1.3.0 - comando: `pip install face-recognition`
* imutils 0.5.4 - comando: `pip install imutils`

### Generar archivo de bibliotecas y dependencias
- comando: `python -m pip freeze > requerimientos.txt`

### Recursos
- para usar con face-recognition: [Dlib compiled wheels for Python 3.7, 3.8, 3.9](https://github.com/sachadee/Dlib)

### Apuntes 
1. para actulizar todos los paquetes pip - comando: `pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}`
2. para desinstalar una bibliteca especifica: `pip uninstall nombre_biblioteca`