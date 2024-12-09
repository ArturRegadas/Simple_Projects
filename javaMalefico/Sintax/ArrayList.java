package Sintax;
import java.util.ArrayList;

class List{
    public static void main(String[] args){
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);

        System.out.println("Lista " + nums);
        System.out.println("elemento no index 0" + nums.get(0));

        nums.remove(0);

        System.out.println("Lista pos remoção "+nums);

        int size = nums.size();
        boolean exist = nums.contains(2);
        int index = nums.indexOf(3);  

        System.out.printf("tamanho: %d , se 2 esta em nums %b, indice do numero 3: %d%n", size, exist, index);

        nums.set(0, 20);

        System.out.println("Lista pós substituição: "+nums);

        nums.add(1, 4);

        System.out.println("Lista pós insercao: "+nums);

        nums.clear();


    }
}