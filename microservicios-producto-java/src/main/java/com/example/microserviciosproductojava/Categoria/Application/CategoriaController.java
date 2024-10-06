package com.example.microserviciosproductojava.Categoria.Application;

import com.example.microserviciosproductojava.Categoria.DTOS.RequestCategoria;
import com.example.microserviciosproductojava.Categoria.DTOS.ResponseCategoriaDto;
import com.example.microserviciosproductojava.Categoria.Domain.CategoriaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/categoria")
public class CategoriaController {
    @Autowired
    private CategoriaService categoriaService;

    @PostMapping("/postear")
    public ResponseEntity<ResponseCategoriaDto> publicarCategoria(@RequestBody RequestCategoria requestCategoria) {
        return ResponseEntity.ok(categoriaService.publicarCategoria(requestCategoria));
    }

    @GetMapping("/all")
    public ResponseEntity<Page<ResponseCategoriaDto>> obtenerCategorias(@RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(categoriaService.obtenerCategorias(page, size));
    }

    @GetMapping("/{id}")
    public ResponseEntity<ResponseCategoriaDto> obtenerCategoria(@PathVariable Integer id) {
        return ResponseEntity.ok(categoriaService.obtenerCategoria(id));
    }

    @PatchMapping("/{id}")
    public ResponseEntity<Void> actualizarCategoria(@PathVariable Integer id, @RequestBody RequestCategoria requestCategoria) {
        categoriaService.actualizarCategoria(id, requestCategoria);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/nombre")
    public ResponseEntity<Page<ResponseCategoriaDto>> obtenerCategoriasPorNombre(@RequestParam String nombre, @RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(categoriaService.obtenerCategoriasPorNombre(nombre, page, size));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarCategoria(@PathVariable Integer id) {
        categoriaService.eliminarCategoria(id);
        return ResponseEntity.ok().build();
    }

}
