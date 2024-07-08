// src/pages/DeleteProduct.jsx

import React, { useState, useEffect } from 'react';
import { Container, Table, Button } from 'react-bootstrap';
import './ProductList.css'; // Importar el archivo CSS personalizado

const KEY = 'productList';

const DeleteProduct = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    const handleDelete = (productId) => {
        if (window.confirm('¿Estás seguro de que deseas eliminar este producto?')) {
            const updatedProducts = products.filter(product => product.id !== productId);
            setProducts(updatedProducts);
            localStorage.setItem(KEY, JSON.stringify(updatedProducts));
        }
    };

    return (
        <Container>
            <h1 className="my-4 text-center">Eliminar Producto</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th className="col-id">ID</th>
                        <th className="col-name">Nombre Producto</th>
                        <th className="col-price">Precio</th>
                        <th className="col-stock">Stock</th>
                        <th className="col-description">Descripción</th>
                        <th className="col-actions">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td className="col-id">{product.id}</td>
                            <td className="col-name">{product.name}</td>
                            <td className="col-price">${product.price}</td>
                            <td className="col-stock">{product.stock}</td>
                            <td className="col-description">{product.description}</td>
                            <td className="col-actions">
                                <Button variant="danger" onClick={() => handleDelete(product.id)}>Eliminar</Button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
};

export default DeleteProduct;
