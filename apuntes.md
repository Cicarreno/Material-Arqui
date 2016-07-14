#Apuntes Lean C the HardWay
Como hacer un print:

```c
#include <stdio.h>
int main(int argc, char const *argv[])
{
	puts("Hello world.");
	puts("Jhonny");
	
	return 0;
}
```
El make se usa para compilar archivos, make ex1 buscara en la carpeta ex1.c y lo compilará, para hacer un mejor uso se puede usar un Makefile.

```c
CFLAGS=-Wall -g
clean:
	rm -f ex1
all: ex1 ex3

```
Este es un ej de Makefile, el `CFLAGS` hace que los warnings sean visibles en consola al momento de compilar, clean se usa para borrar ex1 ejecutando un comando de consola, siempre usar tabs!, si en el archivo de C colocamos '#include <stdio.h>' en el header no saldrán las warnings de prints (puts en este caso).
all: sirve para compilar todos los archivos que le siguen despues con un simple `make`a secas, es bueno colocarlo al inicio de todo para que el `make`se tome por defecto y compilar todo de forma simple.

Format Print: 
Muy parecido al estilo antiguo de python, importante los `;`después de cada instrucción y también declarar el tipo de dato de las variables (en todo el programa de C). Al usar `%d`es decimal, puede ser float, char, u otro tipo de dato.

```c
#include <stdio.h>

int main()
{
	int age = 21;
	float height = 1.81;

	printf("Tengo %d años de edad.\n", age);
	printf("Mido esto: %f.\n", height);

	return 0;
}

```



