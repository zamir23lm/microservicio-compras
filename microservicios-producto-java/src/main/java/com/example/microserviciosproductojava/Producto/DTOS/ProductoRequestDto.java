package com.example.microserviciosproductojava.Producto.DTOS;


import lombok.Data;

@Data
public class ProductoRequestDto {
    private String nombre;
    private String descripcion;
    private Double precio;
    private Integer stock;
    private Integer categoriaId;
}
