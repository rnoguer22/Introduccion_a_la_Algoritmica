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

## Ejercicio 10
### Área del triángulo
```
Algoritmo Area_Triangulo
	
	//Definimos las variables
	Definir lado, altura Como Real
	
	//Introducimos los datos por teclado
	Escribir "Introduzca la medida del lado y la altura relativa a ese lado:"
	Leer lado, altura
	
	//Calculamos el area
	area = (lado*altura)/2
	
	//Mostramos el area por pantalla
	Escribir "El area es ", area 
	
	//Si se trata de un triangulo rectangulo en el que nos dan la medida de los dos catetos, el area seria la misma
	//Ya que un cateto seria el lado y el otro seria la altura
	
FinAlgoritmo
```

## Ejercicio 11
### Salario y horas extra
```
Algoritmo horas_extra
    // Establece la remuneración de `horas_ext' adicionales para
    // salario mensual bruto de `salario_mensual_bruto'.
	
//ENTRADA
	Definir salario_mensual_bruto Como Real
	Definir horas_ext Como Entero
	Escribir "Introduzca el salario mensual bruto y las horas extra:"
	Leer salario_mensual_bruto, horas_ext
	
	//Definimos las constantes
	Definir HORAS_MAX_, HORAS_SEMANA, SEMANAS Como Entero
	SEMANAS <- 52
	HORAS_SEMANA <- 35
	HORAS_MAX_ <- 8
	
	Definir PRECIO_1, PRECIO_2 Como Real
	PRECIO_1 <- 1.25
	PRECIO_2 <- 1.50
	
//VARIABLES
	//Estas variables nos van a almacenar la cantidad de horas extra con PRECIO_1 y PRECIO_2 respectivamente
	Definir horas_ext_1, horas_ext_2 Como ENTERO
	Definir precio_hora Como Real
	
//REALIZACION
    	//Vamos a hallar el precio_hora de la remuneración bruta básica
	precio_hora <- (salario_mensual_bruto*12)/(HORAS_SEMANA*SEMANAS)
	//Ahora ya podemos calcular la remuneracion de las horas extra
    Resultado <- precio_hora x (inf(horas_ext, CANTIDAD_HORAS_MAX_1) x PRECIO_1 + sup(horas_ext - CANTIDAD_HORAS_MAX_1, 0) x PRECIO_2)
	
fin Algoritmo
```
