// src/pages/ProductPage.jsx

import React, { useState, useRef, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Container, Row, Col, Button, ListGroup, Form } from 'react-bootstrap';

const KEY = 'productList';

const ProductPage = () => {
    const [products, setProducts] = useState([]);

    const nameRef = useRef();
    const priceRef = useRef();
    const stockRef = useRef();

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    useEffect(() => {
        localStorage.setItem(KEY, JSON.stringify(products));
    }, [products]);

    const addProduct = () => {
        const name = nameRef.current.value;
        const price = priceRef.current.value;
        const stock = stockRef.current.value;
        if (name === '' || price === '' || stock === '') return;

        setProducts(prevProducts => {
            return [...prevProducts, { id: uuidv4(), name, price: parseFloat(price), stock: parseInt(stock) }];
        });

        nameRef.current.value = null;
        priceRef.current.value = null;
        stockRef.current.value = null;
    };

    const deleteProduct = (id) => {
        setProducts(products.filter(product => product.id !== id));
    };

    return (
        <Container>
            <h1 className="my-4">Mantenedor de Productos</h1>
            <Form>
                <Row className="align-items-end mb-3">
                    <Col md={4}>
                        <Form.Group controlId="formProductName">
                            <Form.Label>Nombre del Producto</Form.Label>
                            <Form.Control type="text" placeholder="Nombre del producto" ref={nameRef} />
                        </Form.Group>
                    </Col>
                    <Col md={3}>
                        <Form.Group controlId="formProductPrice">
                            <Form.Label>Precio del Producto</Form.Label>
                            <Form.Control type="number" placeholder="Precio del producto" ref={priceRef} />
                        </Form.Group>
                    </Col>
                    <Col md={3}>
                        <Form.Group controlId="formProductStock">
                            <Form.Label>Stock del Producto</Form.Label>
                            <Form.Control type="number" placeholder="Stock del producto" ref={stockRef} />
                        </Form.Group>
                    </Col>
                    <Col md={2}>
                        <Button variant="primary" onClick={addProduct}>Agregar Producto</Button>
                    </Col>
                </Row>
            </Form>
            <ListGroup>
                {products.map(product => (
                    <ListGroup.Item key={product.id}>
                        <Row className="align-items-center">
                            <Col>{product.name}</Col>
                            <Col>${product.price}</Col>
                            <Col>Stock: {product.stock}</Col>
                            <Col>
                                <Button variant="danger" onClick={() => deleteProduct(product.id)}>Eliminar</Button>
                            </Col>
                        </Row>
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </Container>
    );
};

export default ProductPage;
