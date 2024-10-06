package com.example.microserviciosproductojava.Producto.DTOS;

import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@Data
public class ProductoResponseDTO {
    private Integer id;
    private String nombre;
    private String descripcion;
    private Double precio;
    private Integer stock;
    private Integer categoriaId;
    private Integer cantidadReseñas;
}
