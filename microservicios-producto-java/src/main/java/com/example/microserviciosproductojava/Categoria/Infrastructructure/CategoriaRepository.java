package com.example.microserviciosproductojava.Categoria.Infrastructructure;

import com.example.microserviciosproductojava.Categoria.Domain.Categoria;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface CategoriaRepository extends JpaRepository<Categoria, Integer> {
    @Query("SELECT c FROM Categoria c WHERE LOWER(c.nombre) LIKE LOWER(CONCAT('%', :nombre, '%'))")
    Page<Categoria> findByNombreContainingIgnoreCase(String nombre, Pageable pageable);
}
