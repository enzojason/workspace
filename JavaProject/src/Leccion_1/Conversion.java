package Leccion_1;

public class Conversion {
	public static void conversion(String[] args){
		System.out.println("CONVERSION DE TIPOS; CASTING");
		System.out.println("\n");
		
		System.out.println("Conversion impilicita");
		/*
		 * La conversión implícita o generalización (widening) 
		 * es aquella que se realiza automáticamente por el compilador, 
		 * sin necesidad de indicar que debe realizarse
		 * 
		 */
		int num1 = 5;
		float num2 = 5.5f;
		float suma = num1 + num2; // 10.5
		System.out.println("SUMA " + suma);
		System.out.println("\n");
		
		System.out.println("Conversion explícita");
		/*
		*Las conversiones explícitas solo se realizan entre tipos de datos primitivos, 
		*respetando el tamaño que ocupa en memoria cada tipo de dato.
		*/
		//double → float → long → int → char → short → byte
		
		float num4 = 5.5f;
		float num5 = 5.5f;
		int resultadonum;
		resultadonum = (int) (num4 + num5); // 11
		System.out.println("RESULTADO: " + resultadonum);
		System.out.println("\n");
	}
	
}
