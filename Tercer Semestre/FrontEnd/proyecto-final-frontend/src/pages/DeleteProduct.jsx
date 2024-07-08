// src/pages/DeleteProduct.jsx

import React, { useState, useEffect } from 'react';
import { Container, ListGroup, Row, Col, Button } from 'react-bootstrap';

const KEY = 'productList';

const DeleteProduct = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    const handleDelete = (id) => {
        const updatedProducts = products.filter(product => product.id !== id);
        setProducts(updatedProducts);
        localStorage.setItem(KEY, JSON.stringify(updatedProducts));
    };

    return (
        <Container>
            <h1 className="my-4">Eliminar Producto</h1>
            <ListGroup>
                {products.map(product => (
                    <ListGroup.Item key={product.id}>
                        <Row className="align-items-center">
                            <Col>ID: {product.id}</Col>
                            <Col>Nombre: {product.name}</Col>
                            <Col>Precio: ${product.price}</Col>
                            <Col>Stock: {product.stock}</Col>
                            <Col>
                                <Button variant="danger" onClick={() => handleDelete(product.id)}>Eliminar</Button>
                            </Col>
                        </Row>
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </Container>
    );
};

export default DeleteProduct;
