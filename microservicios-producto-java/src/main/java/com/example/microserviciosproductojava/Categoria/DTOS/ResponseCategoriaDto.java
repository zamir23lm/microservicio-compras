package com.example.microserviciosproductojava.Categoria.DTOS;

import lombok.Data;

@Data
public class ResponseCategoriaDto {
    private Integer id;
    private String nombre;
    private String descripcion;
    private Integer totalProductos;
}
