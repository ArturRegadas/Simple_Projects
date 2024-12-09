package Sintax;
import java.util.Scanner;

class Scan{
    public static void main(String[] args){
        String name;
        int date;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Your Name: ");
        name = scanner.next();

        System.out.print("date of birth: ");
        date = scanner.nextInt();

        System.out.printf("Hello %s%nyou have %d age%n", name, 2024-date);

        scanner.close();




    }
}