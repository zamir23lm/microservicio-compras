package com.example.microserviciosproductojava.Producto.Domain;


import com.example.microserviciosproductojava.Categoria.Domain.Categoria;
import com.example.microserviciosproductojava.Categoria.Infrastructructure.CategoriaRepository;
import com.example.microserviciosproductojava.Producto.DTOS.ProductoRequestDto;
import com.example.microserviciosproductojava.Producto.DTOS.ProductoResponseDTO;
import com.example.microserviciosproductojava.Producto.Infrastructure.ProductoRepository;
import jakarta.persistence.EntityNotFoundException;
import lombok.NoArgsConstructor;
import org.antlr.v4.runtime.atn.SemanticContext;
import org.apache.coyote.Request;
import org.springframework.data.domain.Page;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;


@NoArgsConstructor
@Service
public class ProductoService {
    @Autowired
    private CategoriaRepository categoriaRepository;
    @Autowired
    private ProductoRepository productoRepository;

    public ProductoResponseDTO postearProducto(ProductoRequestDto producto) {
        Producto producto1 = new Producto();
        Categoria categoria = categoriaRepository.findById(producto.getCategoriaId()).
                orElseThrow(()->new EntityNotFoundException("Categoria no encontrada"));
        producto1.setNombre(producto.getNombre());
        producto1.setDescripcion(producto.getDescripcion());
        producto1.setPrecio(producto.getPrecio());
        producto1.setStock(producto.getStock());
        producto1.setCategoria(categoria);
        producto1.setCantidadReseñas(0);
        productoRepository.save(producto1);
        categoria.getProductos().add(producto1);
        categoria.setTotalProductos(categoria.getTotalProductos() + 1);
        categoriaRepository.save(categoria);
        return convertoDto(producto1);
    }

    public ProductoResponseDTO getProducto(Integer id){
        Producto producto = productoRepository.findById(id).orElseThrow(()->new EntityNotFoundException("Producto no encontrado"));
        ProductoResponseDTO productoResponseDTO = new ProductoResponseDTO();
        productoResponseDTO.setNombre(producto.getNombre());
        productoResponseDTO.setDescripcion(producto.getDescripcion());
        productoResponseDTO.setPrecio(producto.getPrecio());
        productoResponseDTO.setStock(producto.getStock());
        productoResponseDTO.setId(producto.getId());
        productoResponseDTO.setCantidadReseñas(producto.getCantidadReseñas());
        productoResponseDTO.setCategoriaId(producto.getCategoria().getId());
        return productoResponseDTO;
    }

    public Page<ProductoResponseDTO>  obtenerProductos(int page, int size){
        Pageable pageable = PageRequest.of(page, size);
        Page<Producto> productos = productoRepository.findAll(pageable);
        List<ProductoResponseDTO> productosresponse = productos.getContent().stream()
                .map(this::convertoDto).collect(Collectors.toList());
        return new PageImpl<>(productosresponse, pageable, productos.getTotalElements());
    }

    public void actualizarProducto(Integer id, ProductoRequestDto productoRequestDto){
        Producto producto = productoRepository.findById(id).orElseThrow(()->new EntityNotFoundException("Producto no encontrado"));
        if(!productoRequestDto.getDescripcion().isEmpty()){
            producto.setDescripcion(productoRequestDto.getDescripcion());
        }
        if(!productoRequestDto.getNombre().isEmpty()){
            producto.setNombre(productoRequestDto.getNombre());
        }
        if(productoRequestDto.getPrecio() != null){
            producto.setPrecio(productoRequestDto.getPrecio());
        }
        if(productoRequestDto.getStock() != null){
            producto.setStock(producto.getStock() - productoRequestDto.getStock());
            if(producto.getStock() == 0){
                producto.getCategoria().setTotalProductos(producto.getCategoria().getTotalProductos() - 1);
            }
        }

        productoRepository.save(producto);
    }

    public void eliminarProducto(Integer id){
        Producto producto = productoRepository.findById(id).orElseThrow(()->new EntityNotFoundException("Producto no encontrado"));
        producto.getCategoria().getProductos().remove(producto);
        producto.getCategoria().setTotalProductos(producto.getCategoria().getTotalProductos() - 1);
        categoriaRepository.save(producto.getCategoria());
        productoRepository.delete(producto);
    }
    public void actualizarStock(int id, int cantidad){
        Producto producto = productoRepository.findById(id).orElseThrow(()->new EntityNotFoundException("Producto no encontrado"));
        producto.setStock(producto.getStock() + cantidad);
        productoRepository.save(producto);
    }
    public void reducirStock(int id, int cantidad){
        Producto producto = productoRepository.findById(id).orElseThrow(()->new EntityNotFoundException("Producto no encontrado"));
        producto.setStock(producto.getStock() - cantidad);
        if(producto.getStock() == 0){
            producto.getCategoria().setTotalProductos(producto.getCategoria().getTotalProductos() - 1);
        }
        productoRepository.save(producto);
    }

    public Page<ProductoResponseDTO> obtenerProductosPorCategoria(int id, int page, int size){
        Pageable pageable = PageRequest.of(page, size);
        Page<Producto> productos = productoRepository.findAllByCategoriaId(id, pageable);
        List<ProductoResponseDTO> productosresponse = productos.getContent().stream()
                .map(this::convertoDto).collect(Collectors.toList());
        return new PageImpl<>(productosresponse, pageable, productos.getTotalElements());
    }
    public Page<ProductoResponseDTO> obtenerProductosPorNombre(String nombre, int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        nombre =nombre.toLowerCase(Locale.ROOT);
        Page<Producto> productos = productoRepository.findByNombreContainingIgnoreCase(nombre, pageable);
        List<ProductoResponseDTO> productosresponse = productos.getContent().stream()
                .map(this::convertoDto).collect(Collectors.toList());
        return new PageImpl<>(productosresponse, pageable, productos.getTotalElements());
    }

    private ProductoResponseDTO convertoDto(Producto producto){
        ProductoResponseDTO productoResponseDTO = new ProductoResponseDTO();
        productoResponseDTO.setNombre(producto.getNombre());
        productoResponseDTO.setDescripcion(producto.getDescripcion());
        productoResponseDTO.setPrecio(producto.getPrecio());
        productoResponseDTO.setStock(producto.getStock());
        productoResponseDTO.setId(producto.getId());
        productoResponseDTO.setCantidadReseñas(producto.getCantidadReseñas());
        productoResponseDTO.setCategoriaId(producto.getCategoria().getId());
        return productoResponseDTO;
    }
}
