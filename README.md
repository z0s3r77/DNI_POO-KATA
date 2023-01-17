# DNI-POO-KATA
![DNI_DDD](https://user-images.githubusercontent.com/80277545/212742395-296e74d5-1fdc-4c45-961e-dc3b2340e0c8.jpg)

El KATA consiste en escribir un programa que dado un número de DNI obtenga la letra resultante. Dicha letra se calcula con el siguiente algoritmo:

- Se obtiene el resto de dividir el número de DNI entre 23.
- El número resultante indica la posición de la letra correspondiente a ese DNI en la siguiente cadena:


__Tabla de asignación__

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| T | R | W | A | G | M | Y | F | P | D | X | B | N | J | Z | S | Q | V | H | L | C | K | E |


Se debe construir un programa utilizando un vector para almacenar cada una de las letras de la tabla anterior. Luego se debe utilizar un diccionario para almacenar la tabla de asignación. Se debe dividir el código mediante una capa de lógica y una capa de acceso a datos para que los cambios en la estrutura de datos utilizada (vector o diccionario) no supongan modificaciones en el código correspondiente a la lógica.

# Manual
## Pre-requisitos

    - `Git`
    - `Python3`
    - `pip3`

## Instalación
Se recomienda utilizar en 'virtualenv' para instalar todas las dependencias utilizadas por el programa.

```
sudo apt-get install python3-venv
```
Crea y situate en un directorio para clonar este repositorio en tu maquina local.

```
mkdir ./DNI-z0s3r77
cd DNI-z0s3r77
```

Dentro del directorio, clona el repositorio.
```
git clone https://github.com/z0s3r77/DNI-KATA.git
```

Ejecuta el siguiente comando para activar el entorno virtual e instalar *requirements.txt*
```
./setup.sh
```

En caso de no funcionar correctamente ejecuta los comandos manualmente.

```
python3 -m venv venv

source ./venv/bin/activate

pip3 install -r requirements.txt
```

## Uso

Para usar el programa ejecuta:

```
python3 src/dni.py
```

Se te solicitará un numero de DNI y se te dará la letra correspondiente.

![image](https://user-images.githubusercontent.com/80277545/210390609-754ff8f9-0099-49b3-8f6c-8eb25c602889.png)

