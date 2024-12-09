package Spring.helloword.src.main.java.com.example.helloword.controller;
import java.util.HashMap;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/hello")
    public Map<String, String> hello() {
        Map<String, String> Person = new HashMap<>();
        Person.put("Hello", "Word");
        return Person;
    }
}
