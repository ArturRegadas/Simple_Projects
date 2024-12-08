import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Hash{
    public static void main(String[] args){
        Map<String, Integer> Person = new HashMap<>();
        
        Person.put("Artur", 16);
        Person.put("Maria", 22);
        System.out.println(Person);

        Integer age = Person.get("Artur");
        System.out.println("The Artur have "+age+" ages");
        
        Person.remove("Artur");
        System.out.println("The map before remove: "+ Person);

        boolean existKey = Person.containsKey("Maria");
        boolean existValue = Person.containsValue(22);
        Integer size = Person.size();

        System.out.printf("O Map esta com tamanho %d/Maria esta no Map como chave %b e 22 esta no map como valor: %b%n",size, existKey, existValue);;

        Set<String> keysInSet = Person.keySet();
        Collection<Integer> ValuesInSet = Person.values();

        System.out.println(keysInSet);
        System.out.println(ValuesInSet);

        Person.putIfAbsent("Maria", 25);//adciona se a chave nao tiver no Map

        Person.replace("Maria", 26); //vai trocar o valor da chave se ela existir
        System.out.println("Map before replace "+ Person);

        Person.replace("Maria", 25, 26); // Substitui 25 por 26, se o valor de "Alice" for 25

        Person.forEach((key, value) -> System.out.println(key + ": " + value));

        for (Map.Entry<String, Integer> entry : Person.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }




    }
}