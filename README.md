# Introduccion_a_la_Algoritmica

[Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Introduccion_a_la_Algoritmica.git)

##  Ejericicio 8
### Porcentajes, IVA e Inversiones
#### Parte 1)
```
Algoritmo Porcentajes_IVA_Inversiones_1
	
	//Definimos las variables
	Definir precio_sin_impuestos, IVA, precio_con_impuestos Como Real
	Escribir "Dame el precio sin impuestos y el IVA (porcentaje): "
	Leer precio_sin_impuestos, IVA
	
	//Calculamos el precio con impuestos
	precio_con_impuestos = precio_sin_impuestos + precio_sin_impuestos*0.01*IVA
	Escribir "El precio con IVA es de ", precio_con_impuestos, " euros"

FinAlgoritmo
```
#### Parte 2)
```
Algoritmo Porcentajes_IVA_Inversiones_2
	
	//Definimos las variables
	Definir capital_invertido, interes Como Real
	Definir meses Como Entero
	
	//Introducimos los datos por pantalla
	Escribir "Introduzca el capital invertido, el interes y el numero de meses: "
	Leer capital_invertido, interes, meses
	
	//Definimos una variable que nos calcula el importe de interes
	importe_interes = capital_invertido*interes*meses
	
	//Mostramos el resultado por pantalla
	Escribir "El importe de interes de ", capital_invertido, " a un ", interes*100, "% durante ", meses, " meses es de ", importe_interes, " euros"
	
FinAlgoritmo
```

## Ejercicio 9
### Media Aritmetica Ponderada
#### Parte 1)
```
Algoritmo Media_Aritmetica_1
	
	//Introducimos las variables por teclado
	Definir num1, num2, num3 Como Real
	Escribir "Introduzca 3 numeros: "
	Leer num1, num2, num3
	
	//Definimos la variable media_aritmetica que calcula la media aritmetica de los tres numeros introducidos por teclado
	media_aritmetica = (num1+num2+num3)/3
	
	//Mostramos el resultado por pantalla
	Escribir media_aritmetica
	
FinAlgoritmo
```
#### Parte 2)
```
Algoritmo Media_Aritmetica_2
	
	//Introducimos las variables por teclado
	Definir num1, num2, num3 Como Real
	Escribir "Introduzca 3 numeros: "
	Leer num1, num2, num3
	
	//Definimos la variable media_aritmetica que calcula la media aritmetica de los tres numeros introducidos por teclado
	media_aritmetica = (num1+num2+num3)/3
	
	//Definimos el parametro de ponderacion
	ponderacion = 0.5
	
	//Mostramos el resultado por pantalla
	Escribir media_aritmetica
	
FinAlgoritmo
```
