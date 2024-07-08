// src/pages/ProductList.jsx

import React, { useState, useEffect } from 'react';
import { Container, Table } from 'react-bootstrap';

const KEY = 'productList';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    return (
        <Container>
            <h1 className="my-4">Lista de Productos</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Precio</th>
                        <th>Stock</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td>{product.id}</td>
                            <td>{product.name}</td>
                            <td>${product.price}</td>
                            <td>{product.stock}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
};

export default ProductList;
