package com.example.microserviciosproductojava.Reseña.Domain;

import com.example.microserviciosproductojava.Producto.Domain.Producto;
import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class Reseña {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String comentario;
    private Integer calificacion;
    private int usuarioId;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "producto_id", nullable = false)
    private Producto producto;
}
