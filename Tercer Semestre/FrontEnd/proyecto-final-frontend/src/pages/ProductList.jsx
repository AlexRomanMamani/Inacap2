// src/pages/ProductList.jsx

import React, { useState, useEffect } from 'react';
import { Container, Table, Image } from 'react-bootstrap';
import './ProductList.css'; // Importar el archivo CSS personalizado

const KEY = 'productList';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    return (
        <Container>
            <h1 className="my-4 text-center">Lista de Productos</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th className="col-id">ID</th>
                        <th className="col-name">Nombre</th>
                        <th className="col-price">Precio</th>
                        <th className="col-stock">Stock</th>
                        <th className="col-image">Imagen</th>
                        <th className="col-description">Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td className="col-id">{product.id}</td>
                            <td className="col-name">{product.name}</td>
                            <td className="col-price">${product.price}</td>
                            <td className="col-stock">{product.stock}</td>
                            <td className="col-image">
                                <Image src={product.image} alt={product.name} fluid style={{ maxWidth: '100px' }} />
                            </td>
                            <td className="col-description">{product.description}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
};

export default ProductList;
