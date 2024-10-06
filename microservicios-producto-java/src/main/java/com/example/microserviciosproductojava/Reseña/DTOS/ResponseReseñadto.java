package com.example.microserviciosproductojava.Reseña.DTOS;

import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@Data
public class ResponseReseñadto {
    private Integer id;
    private String comentario;
    private Integer calificacion;
    private int usuarioId;
    private Integer productoId;

}
