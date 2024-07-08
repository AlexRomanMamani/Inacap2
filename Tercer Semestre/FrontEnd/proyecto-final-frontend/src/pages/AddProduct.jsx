// src/pages/AddProduct.jsx

import React, { useRef } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Container, Form, Row, Col, Button } from 'react-bootstrap';

const KEY = 'productList';

const AddProduct = () => {
    const nameRef = useRef();
    const priceRef = useRef();
    const stockRef = useRef();

    const addProduct = () => {
        const name = nameRef.current.value;
        const price = priceRef.current.value;
        const stock = stockRef.current.value;

        if (name === '' || price === '' || stock === '') return;

        const newProduct = {
            id: uuidv4(),
            name,
            price: parseFloat(price),
            stock: parseInt(stock),
        };

        const storedProducts = JSON.parse(localStorage.getItem(KEY)) || [];
        storedProducts.push(newProduct);
        localStorage.setItem(KEY, JSON.stringify(storedProducts));

        nameRef.current.value = null;
        priceRef.current.value = null;
        stockRef.current.value = null;
    };

    return (
        <Container>
            <h1 className="my-4">Agregar Producto</h1>
            <Form>
                <Row className="justify-content-center">
                    <Col md={6}>
                        <Form.Group controlId="formProductName">
                            <Form.Label>Nombre del Producto</Form.Label>
                            <Form.Control type="text" placeholder="Nombre del producto" ref={nameRef} />
                        </Form.Group>
                        <Form.Group controlId="formProductPrice">
                            <Form.Label>Precio del Producto</Form.Label>
                            <Form.Control type="number" placeholder="Precio del producto" ref={priceRef} />
                        </Form.Group>
                        <Form.Group controlId="formProductStock">
                            <Form.Label>Stock del Producto</Form.Label>
                            <Form.Control type="number" placeholder="Stock del producto" ref={stockRef} />
                        </Form.Group>
                        <Button variant="primary" onClick={addProduct}>Agregar Producto</Button>
                    </Col>
                </Row>
            </Form>
        </Container>
    );
};

export default AddProduct;
