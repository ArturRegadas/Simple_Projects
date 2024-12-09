package Sintax;
import java.util.Stack;

public class Stacks {
    public static void main(String[] args){
        Stack<String> pilha = new Stack<>();
        pilha.push("Person1");
        pilha.push("Person2");
        pilha.push("Person3");

        System.out.println(pilha);

        String first = pilha.pop();
        String nextNoRemove = pilha.peek();

        
        System.out.println("O proximo é "+first+" e depois dele sera "+nextNoRemove);



    }
    
}
