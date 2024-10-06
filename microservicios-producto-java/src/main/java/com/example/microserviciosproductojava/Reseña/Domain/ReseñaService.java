package com.example.microserviciosproductojava.Reseña.Domain;

import com.example.microserviciosproductojava.Producto.DTOS.ProductoResponseDTO;
import com.example.microserviciosproductojava.Producto.Domain.Producto;
import com.example.microserviciosproductojava.Producto.Infrastructure.ProductoRepository;
import com.example.microserviciosproductojava.Reseña.DTOS.PostReseñadto;
import com.example.microserviciosproductojava.Reseña.DTOS.ResponseReseñadto;
import com.example.microserviciosproductojava.Reseña.DTOS.patchdto;
import com.example.microserviciosproductojava.Reseña.DTOS.promediodto;
import com.example.microserviciosproductojava.Reseña.Infrastructure.ReseñaRepository;
import jakarta.transaction.Transactional;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@NoArgsConstructor
public class ReseñaService {
    @Autowired
    private ReseñaRepository reseñaRepository;

    @Autowired
    private ProductoRepository productoRepository;


    @Transactional
    public void crearReseña(PostReseñadto post) {
        // Buscar el producto por ID
        System.out.println("dto  " + post);
        Producto producto = productoRepository.findById(post.getProductoId())
                .orElseThrow(() -> new RuntimeException("Producto no encontrado"));

        System.out.println("Producto encontrado: " + producto.getId());
        Reseña reseña = new Reseña();
        reseña.setCalificacion(post.getCalificacion());
        reseña.setComentario(post.getComentario());
        reseña.setUsuarioId(post.getUsuarioId());

        // Asignar el producto a la reseña
        reseña.setProducto(producto);

        // Verificar que el producto se está enlazando correctamente
        System.out.println("Producto en la reseña: " + reseña.getProducto().getId());

        // Guardar la reseña
        reseñaRepository.save(reseña);
        reseñaRepository.flush();  // Forzar sincronización

        // Actualizar el producto con la nueva reseña
        if (producto.getCantidadReseñas() == null) {
            producto.setCantidadReseñas(1);
        } else {
            producto.setCantidadReseñas(producto.getCantidadReseñas() + 1);
        }
        productoRepository.save(producto);
    }


    public Page<ResponseReseñadto> ObtenerReseñasPorProducto(Integer productoId, int page, int size){
        Pageable pageable = PageRequest.of(page, size);
        Page<Reseña> reseñas = reseñaRepository.findAllByProductoId(productoId, pageable);
        List<ResponseReseñadto> responseReseñadtos = reseñas.getContent().stream()
                .map(this::converToDto).collect(Collectors.toList());
        return new PageImpl<>(responseReseñadtos, pageable, reseñas.getTotalElements());
    }

    public ResponseReseñadto ObtenerReseñaPorProducto(Integer productoId, Integer reseñaId){
        Reseña reseña = reseñaRepository.findById(reseñaId).orElseThrow(()-> new RuntimeException("Reseña no encontrada"));
        if(reseña.getProducto().getId() != productoId){
            throw new RuntimeException("Reseña no encontrada");
        }
        return converToDto(reseña);
    }
    public void EliminarReseña(Integer productoId, Integer reseñaId){
        Reseña reseña = reseñaRepository.findById(reseñaId).orElseThrow(()-> new RuntimeException("Reseña no encontrada"));
        if(reseña.getProducto().getId() != productoId){
            throw new RuntimeException("Reseña no encontrada");
        }
        Producto producto = reseña.getProducto();
        producto.getReseñas().remove(reseña);
        producto.setCantidadReseñas(producto.getCantidadReseñas() - 1);
        productoRepository.save(producto);
        reseñaRepository.delete(reseña);
    }
    public promediodto ObtenerPromedio(Integer productoId){
        Double promedio = reseñaRepository.findAllByProductoId(productoId, PageRequest.of(0, Integer.MAX_VALUE))
                .getContent()
                .stream()
                .mapToDouble(Reseña::getCalificacion)
                .average()
                .orElse(0.0);
        promediodto promdto = new promediodto();
        promdto.setProductoId(productoId);
        promdto.setPromedio(promedio);
        return promdto;
    }
    public void ActualizarReseña(Integer productoId, Integer reseñaId, patchdto post) {
        // Buscar la reseña por ID o lanzar una excepción si no existe
        Reseña reseña = reseñaRepository.findById(reseñaId)
                .orElseThrow(() -> new RuntimeException("Reseña no encontrada"));

        // Verificar que el usuario tiene permisos para modificar la reseña
        System.out.println("UsuarioId: " + reseña.getUsuarioId());
        System.out.println("ProductoId: " + reseña.getProducto().getId());
        System.out.println("Usuariodto: " + post.getUsuariId());
        if (reseña.getUsuarioId()!= post.getUsuariId()) {
            throw new RuntimeException("Usuario no autorizado para actualizar esta reseña");
        }

        if (!reseña.getProducto().getId().equals(productoId)        // Verificar que el usuario tiene permisos para modificar la reseña
) {
            throw new RuntimeException("Reseña no encontrada para este producto");
        }

        if (post.getCalificacion() != null) {
            reseña.setCalificacion(post.getCalificacion());
        }

        if (post.getComentario() != null && !post.getComentario().isEmpty()) {
            reseña.setComentario(post.getComentario());
        }

        // Guardar los cambios
        reseñaRepository.save(reseña);
    }

    private ResponseReseñadto converToDto(Reseña reseña){
        ResponseReseñadto responseReseñadto = new ResponseReseñadto();
        responseReseñadto.setCalificacion(reseña.getCalificacion());
        responseReseñadto.setComentario(reseña.getComentario());
        responseReseñadto.setId(reseña.getId());
        responseReseñadto.setUsuarioId(reseña.getUsuarioId());
        responseReseñadto.setProductoId(reseña.getProducto().getId());
        return responseReseñadto;
    }



}
