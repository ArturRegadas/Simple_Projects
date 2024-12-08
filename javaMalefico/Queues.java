import java.util.LinkedList;
import java.util.Queue;

public class Queues {
    public static void main(String[] args){
        Queue<String> fila = new LinkedList<>();
        fila.add("person1");
        fila.add("person2"); //retorna erro se tiver cheio
        fila.offer("person3");//retorna none se tiver cheio

        System.out.println(fila);
        String firstPerson = fila.remove(); // retorna erro se nao tiver
        String nextPerson = fila.poll();// retronar none se mao tiver

        String nextNoRemove = fila.element();
        //String nextNoRemove2 = fila.peek();

        
        System.out.printf("a pessoa %s saiu da fila%na pessoa %s tambem saiu %ne a pessoa %s sera a proxima%n", firstPerson, nextPerson, nextNoRemove);




    }
    
}
