package com.example.microserviciosproductojava.Reseña.Application;

import com.example.microserviciosproductojava.Reseña.DTOS.PostReseñadto;
import com.example.microserviciosproductojava.Reseña.DTOS.ResponseReseñadto;
import com.example.microserviciosproductojava.Reseña.DTOS.patchdto;
import com.example.microserviciosproductojava.Reseña.DTOS.promediodto;
import com.example.microserviciosproductojava.Reseña.Domain.ReseñaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/reseñas")
public class ReseñaController {
    @Autowired
    private ReseñaService reseñaService;

    @PostMapping("/postear")
    public ResponseEntity<Void> crearReseña(@RequestBody PostReseñadto postReseñadto) {
        reseñaService.crearReseña(postReseñadto);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/producto/{productoId}")
    public ResponseEntity<Page<ResponseReseñadto>> ObtenerReseñasPorProducto(@PathVariable Integer productoId, @RequestParam int page, @RequestParam int size) {
        return ResponseEntity.ok(reseñaService.ObtenerReseñasPorProducto(productoId, page, size));
    }

    @GetMapping("/{productoId}/{reseñaId}")
    public ResponseEntity<ResponseReseñadto> ObtenerReseñaPorProducto(@PathVariable Integer productoId, @PathVariable Integer reseñaId) {
        return ResponseEntity.ok(reseñaService.ObtenerReseñaPorProducto(productoId, reseñaId));
    }

    @DeleteMapping("/{productoId}/{reseñaId}")
    public ResponseEntity<Void> EliminarReseña(@PathVariable Integer productoId, @PathVariable Integer reseñaId) {
        reseñaService.EliminarReseña(productoId, reseñaId);
        return ResponseEntity.ok().build();
    }
    @GetMapping("/promedio/{productoId}/")
    public ResponseEntity<promediodto> ObtenerPromedio(@PathVariable Integer productoId) {
        return ResponseEntity.ok(reseñaService.ObtenerPromedio(productoId));
    }

    @PatchMapping("/{productoId}/{reseñaId}")
    public ResponseEntity<Void> ActualizarReseña(@PathVariable Integer productoId, @PathVariable Integer reseñaId, @RequestBody patchdto postReseñadto) {
        reseñaService.ActualizarReseña(productoId, reseñaId, postReseñadto);
        return ResponseEntity.ok().build();
    }





}
