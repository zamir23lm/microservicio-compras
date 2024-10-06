package com.example.microserviciosproductojava.Producto.Infrastructure;

import com.example.microserviciosproductojava.Producto.Domain.Producto;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductoRepository extends JpaRepository<Producto, Integer> {
    Page<Producto> findAllByCategoriaId(Integer categoriaId, Pageable pageable);
    @Query("SELECT p FROM Producto p WHERE LOWER(p.nombre) LIKE LOWER(CONCAT('%', :nombre, '%'))")
    Page<Producto> findByNombreContainingIgnoreCase(String nombre, Pageable pageable);
}
