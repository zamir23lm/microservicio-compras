package com.example.microserviciosproductojava.Reseña.Infrastructure;

import com.example.microserviciosproductojava.Reseña.Domain.Reseña;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Page;


@Repository
public interface ReseñaRepository extends JpaRepository<Reseña, Integer> {
    Page<Reseña> findAllByProductoId(Integer productoId, Pageable pageable);
}
