package com.example.microserviciosproductojava.Producto.Application;

import com.example.microserviciosproductojava.Producto.DTOS.ProductoRequestDto;
import com.example.microserviciosproductojava.Producto.DTOS.ProductoResponseDTO;
import com.example.microserviciosproductojava.Producto.Domain.ProductoService;
import lombok.NoArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@NoArgsConstructor
@RestController
@RequestMapping("/api/producto")
public class ProductoController {
    @Autowired
    private ProductoService productoService;

    @PostMapping("/postear")
    public ResponseEntity<ProductoResponseDTO> postearProducto(@RequestBody ProductoRequestDto productoRequestDto) {
        return ResponseEntity.ok(productoService.postearProducto(productoRequestDto));
    }
    @GetMapping("/{id}")
    public ResponseEntity<ProductoResponseDTO> getProducto(@PathVariable Integer id) {
        return ResponseEntity.ok(productoService.getProducto(id));
    }
    @GetMapping("/all")
    public ResponseEntity<Page<ProductoResponseDTO>> obtenerProductos(@RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(productoService.obtenerProductos(page, size));
    }
    @PutMapping("/{id}")
    public ResponseEntity<Void> actualizarProducto(@PathVariable Integer id, @RequestBody ProductoRequestDto productoRequestDto) {
        productoService.actualizarProducto(id, productoRequestDto);
        return ResponseEntity.ok().build();
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarProducto(@PathVariable int id) {
        productoService.eliminarProducto(id);
        return ResponseEntity.ok().build();
    }
    @PatchMapping("/{id}")
    public ResponseEntity<Void> actualizarStock(@PathVariable int id, @RequestParam int cantidad) {
        productoService.actualizarStock(id, cantidad);
        return ResponseEntity.ok().build();
    }
    @PatchMapping("/reducir/{id}")
    public ResponseEntity<Void> reducirStock(@PathVariable int id, @RequestParam int cantidad) {
        productoService.reducirStock(id, cantidad);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/categoria/{id}")
    public ResponseEntity<Page<ProductoResponseDTO>> obtenerProductosPorCategoria(@PathVariable int id, @RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(productoService.obtenerProductosPorCategoria(id, page, size));
    }
    @GetMapping("/nombre/")
    public ResponseEntity<Page<ProductoResponseDTO>> obtenerProductosPorNombre(@RequestParam String nombre, @RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(productoService.obtenerProductosPorNombre(nombre, page, size));
    }

}
