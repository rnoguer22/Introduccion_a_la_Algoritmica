# Introduccion_a_la_Algoritmica

[Pincha aqui para acceder al link de este repositorio]

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
