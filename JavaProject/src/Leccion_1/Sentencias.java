package Leccion_1;

public class Sentencias {
	public static void MostrarSentencia() {
		System.out.println("SENTENCIAS");
		System.out.println("SENTENCIAS DE CONTROL");
		int numero = 5;
		int numero2 = -14;
		if (numero > 0) {
            System.out.println("El número es positivo");
        }else {
        	System.out.println("El número es negativo");
        }
		if (numero2 < 0) {
			System.out.println("el numero es negativo");
		}
		
		
		//SWITCH CASE
		switch (numero) {
        case 0:
            System.out.println("Domingo");
            break;
        case 1:
            System.out.println("Lunes");
            break;
        case 2:
            System.out.println("Martes");
            break;
        case 3:
            System.out.println("Miércoles");
            break;
        case 4:
            System.out.println("Jueves");
            break;
        case 5:
            System.out.println("Viernes");
            break;
        case 6:
            System.out.println("Sábado");
            break;
        default:
            System.out.println("Valor inválido");
            break;
		}
		System.out.println("\n");
		System.out.println("SENTENCIAS DE REPETICION");
        while (numero <= 10) {
            System.out.println(numero);
            numero += 2;
        }
        
        System.out.println("DO-WHILE");
		System.out.println("\n");

		System.out.println("menu ejemplo do while");
		int a =0;
		do {
			System.out.println("CONtar");
			a=a+1;
		} while (a<5);
	}
	
}
