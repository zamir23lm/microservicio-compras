package com.example.microserviciosproductojava;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Controller {

    @GetMapping("/")
    public String welcome() {
        return "Bienvenido al microservicio de Producto";
    }
}
