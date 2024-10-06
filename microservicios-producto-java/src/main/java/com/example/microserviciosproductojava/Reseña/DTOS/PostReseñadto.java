    package com.example.microserviciosproductojava.Reseña.DTOS;

    import jakarta.persistence.Entity;
    import lombok.Data;

    @Data
    public class PostReseñadto {
        private int usuarioId;
        private String comentario;
        private Integer calificacion;
        private Integer productoId;
    }
