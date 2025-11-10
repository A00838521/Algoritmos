
#include <iostream>
#include <stdio.h>
#include <stdlib.h>




using namespace std;


// Funcion que calcule e imprima:
// las coordenadas de los dos puntos mas cercanos y su distancia
void closetPair (  )
{	// tu codigo aqui... 

}


void stringMAtch ()
{
	
	
}

int main(int argc, char* argv[]) 
{	

	// Sintaxis de declaracion de arreglos: 	
	//	type arrayName[size];
	// int numbers[5];
	// int arr[5] = {1, 2, 3, 4, 5};	// tamaño explicito
	// int arr2[]  = {10, 20, 30};		// tamaño implicito

	int n_points = 5; 		// numero de puntos

	// coordenadas de cada punto
	double coors[n_points][2] = 
				{ 	{ -2.423,   -8.469 },
					{  5.721,    9.354 },
					{  6.766,   -3.823 },
					{  4.129,    6.744 },
					{  5.371,   -5.404 } 
				} ;


	char texto[] = "Es este un texto algo largo, que contiene multi-multiples caracteres en un arreglo de tipo char";
	char patron[] = "texto de prueba";  // los arreglos char terminan en \0


	int n_texto = sizeof( texto ) / sizeof( texto[0] );
	int n_patron = sizeof( patron ) / sizeof( patron[0] );


	cout << texto << endl;
	cout << patron << endl;

	cout << "len texto:\t" << n_texto << endl;
	cout << "len patron:\t" << n_patron << patron[n_patron-1] << endl;


}

