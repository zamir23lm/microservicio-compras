package com.example.microserviciosproductojava.Categoria.Domain;

import com.example.microserviciosproductojava.Categoria.DTOS.RequestCategoria;
import com.example.microserviciosproductojava.Categoria.DTOS.ResponseCategoriaDto;
import com.example.microserviciosproductojava.Categoria.Infrastructructure.CategoriaRepository;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.Locale;

@NoArgsConstructor
@Service
public class CategoriaService {
    @Autowired
    private CategoriaRepository categoriaRepository;
    
    public ResponseCategoriaDto publicarCategoria(RequestCategoria requestCategoria) {
        Categoria categoria = new Categoria();
        categoria.setNombre(requestCategoria.getNombre());
        categoria.setDescripcion(requestCategoria.getDescripcion());
        categoria.setTotalProductos(0);
        categoriaRepository.save(categoria);
        ResponseCategoriaDto responseCategoriaDto = new ResponseCategoriaDto();
        responseCategoriaDto.setId(categoria.getId());
        responseCategoriaDto.setNombre(categoria.getNombre());
        responseCategoriaDto.setDescripcion(categoria.getDescripcion());
        responseCategoriaDto.setTotalProductos(categoria.getTotalProductos());
        return responseCategoriaDto;
    }
    
    public void actualizarCategoria(Integer id, RequestCategoria requestCategoria) {
        Categoria categoria = categoriaRepository.findById(id).orElseThrow(() -> new RuntimeException("Categoria no encontrada"));
        categoria.setNombre(requestCategoria.getNombre());
        categoria.setDescripcion(requestCategoria.getDescripcion());
        categoriaRepository.save(categoria);
    }
    
    public void eliminarCategoria(Integer id) {
        try {
            categoriaRepository.deleteById(id);
        } catch (Exception e) {
            throw new RuntimeException("Categoria no encontrada");
        }
    }
    
    public ResponseCategoriaDto obtenerCategoria(Integer id) {
        Categoria categoria = categoriaRepository.findById(id).orElseThrow(() -> new RuntimeException("Categoria no encontrada"));
        ResponseCategoriaDto responseCategoriaDto = new ResponseCategoriaDto();
        responseCategoriaDto.setId(categoria.getId());
        responseCategoriaDto.setNombre(categoria.getNombre());
        responseCategoriaDto.setDescripcion(categoria.getDescripcion());
        responseCategoriaDto.setTotalProductos(categoria.getTotalProductos());
        return responseCategoriaDto;
    }
    
    public Page<ResponseCategoriaDto> obtenerCategorias(int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        return categoriaRepository.findAll(pageable).map(categoria -> {
            ResponseCategoriaDto responseCategoriaDto = new ResponseCategoriaDto();
            responseCategoriaDto.setId(categoria.getId());
            responseCategoriaDto.setNombre(categoria.getNombre());
            responseCategoriaDto.setDescripcion(categoria.getDescripcion());
            responseCategoriaDto.setTotalProductos(categoria.getTotalProductos());
            return responseCategoriaDto;
        });
    }
    public Page<ResponseCategoriaDto> obtenerCategoriasPorNombre(String nombre, int page, int size) {
        Pageable pageable = PageRequest.of(page, size);
        nombre = nombre.toLowerCase(Locale.ROOT);
        Page<Categoria> categorias = categoriaRepository.findByNombreContainingIgnoreCase(nombre, pageable);
        return categorias.map(categoria -> {
            ResponseCategoriaDto responseCategoriaDto = new ResponseCategoriaDto();
            responseCategoriaDto.setId(categoria.getId());
            responseCategoriaDto.setNombre(categoria.getNombre());
            responseCategoriaDto.setDescripcion(categoria.getDescripcion());
            responseCategoriaDto.setTotalProductos(categoria.getTotalProductos());
            return responseCategoriaDto;
        });
    }
}
