package Leccion_1;
import java.util.Scanner;

public class Intro {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("INTRODUCCION TIPO DE DATO; ");
		
		//TIPO DE DATOS		
		//byte,short,int, long
		//2.3 		float	double
		//			bool
		//caracteres char
		//String
		String nombre = "Enzo";
		int n ;
		n = 32;
		System.out.println(n);
		System.out.println(nombre);
		
		float numero;
		numero = 3.14f;
		numero = 2.71f;
		
		boolean encendido;
		encendido = true;
		encendido = false;
		System.out.println(encendido);
		System.out.println(numero);
		
		final int numeroF = 5;
		System.out.println("constante "+numeroF);
		System.out.println("\n");
		
		
		//OPERADORES
		System.out.println("OPERADORES");
		int contador = 0;
		contador++;
		contador++;
		contador++;
		System.out.println("Contador: "+contador);
		//Asignación
		//x += y es equivalente a x = x + y
		//x -= y es equivalente a x = x - y
		//x *= y es equivalente a x = x * y
		//x /= y es equivalente a x = x / y
		//x %= y es equivalente a x = x % y modulo
		
		/*
		 * OPERADORES DE COMPARACIÓN
		==	Igual a	x == y
		!=	Distinto de	x != y
		>	Mayor que	x > y
		<	Menor que	x < y
		>=	Mayor o igual que	x >= y
		<=	Menor o igual que	x <= y
		
		
		OPERADORES LOGICOS
		&&	AND	Devuelve true si todos los valores booleanos son true	x && y
		||	OR	Devuelve true si al menos uno de los valores booleanos es true	x || y
		!	NOT	Devuelve el valor opuesto del valor booleano	!x
		 */
		System.out.println("\n");
		
		
		//CONVERSION DE TIPOS
		Conversion.conversion(args);
		
		
		//SENTENCIAS
		Sentencias.MostrarSentencia();
		
		
		//ENTRADA DE DATOS
		System.out.println("Entrada de DATOS");
		Scanner scanner = new Scanner(System.in);
		//byte numeroByte = scanner.nextByte();
		//short numeroShort = scanner.nextShort();
		//int numeroInt = scanner.nextInt();
		//long numeroLong = scanner.nextLong();
		//float numeroFloat = scanner.nextFloat();
		//double numeroDouble = scanner.nextDouble();
		//boolean booleano = scanner.nextBoolean();
		//String cadena = scanner.nextLine();
		
		int numeroEn = scanner.nextInt();
		System.out.println("NUMERO DE ESCANER: "+ numeroEn);
		System.out.println("\n");
		
		
	}

}
