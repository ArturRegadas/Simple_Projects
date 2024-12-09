package Sintax;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

public class Sort {
    public static void main(String[] args){
        ArrayList<Integer> nums = new ArrayList<>(Arrays.asList(2,3,1,4));
        ArrayList<Integer> nums2 = new ArrayList<>(nums);

        Collections.sort(nums);
        System.out.println(nums);

        Collections.sort(nums2, Collections.reverseOrder());
        System.out.println(nums2);

        Map<String, Integer> Person1 = new HashMap<>(); 
        Person1.put("breno", 29);
        Person1.put("Artur", 25);

        Map<String, Integer> sortedPerson1 = new TreeMap<>(Person1);
        System.out.println("sorted Map: [key] "+sortedPerson1);

        Map<String, Integer> sortedPerson2 = new HashMap<>(Person1);
        List<Map.Entry<String, Integer>> entries = new ArrayList<>(sortedPerson2.entrySet());
        entries.sort(Map.Entry.comparingByValue());

        Map<String, Integer> sortedByValue = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> entry : entries) {
            sortedByValue.put(entry.getKey(), entry.getValue());
        }
        System.out.println("Sorted map by value: "+sortedByValue);


    }
    
}
