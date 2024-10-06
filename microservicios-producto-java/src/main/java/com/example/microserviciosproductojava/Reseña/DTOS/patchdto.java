package com.example.microserviciosproductojava.Reseña.DTOS;

import lombok.Data;

@Data
public class patchdto {
    private String comentario;
    private Integer calificacion;
    private int usuariId;
}
