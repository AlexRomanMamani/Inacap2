// src/pages/EditProduct.jsx

import React, { useState, useEffect } from 'react';
import { Container, ListGroup, Row, Col, Button, Form } from 'react-bootstrap';

const KEY = 'productList';

const EditProduct = () => {
    const [products, setProducts] = useState([]);
    const [editProduct, setEditProduct] = useState(null);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    const handleEdit = (product) => {
        setEditProduct(product);
    };

    const handleSave = () => {
        const updatedProducts = products.map(p =>
            p.id === editProduct.id ? editProduct : p
        );
        setProducts(updatedProducts);
        localStorage.setItem(KEY, JSON.stringify(updatedProducts));
        setEditProduct(null);
    };

    return (
        <Container>
            <h1 className="my-4">Modificar Producto</h1>
            <ListGroup>
                {products.map(product => (
                    <ListGroup.Item key={product.id}>
                        <Row className="align-items-center">
                            <Col>
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="text"
                                        value={editProduct.name}
                                        onChange={(e) => setEditProduct({ ...editProduct, name: e.target.value })}
                                    />
                                ) : (
                                    `Nombre: ${product.name}`
                                )}
                            </Col>
                            <Col>
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="number"
                                        value={editProduct.price}
                                        onChange={(e) => setEditProduct({ ...editProduct, price: parseFloat(e.target.value) })}
                                    />
                                ) : (
                                    `Precio: ${product.price}`
                                )}
                            </Col>
                            <Col>
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="number"
                                        value={editProduct.stock}
                                        onChange={(e) => setEditProduct({ ...editProduct, stock: parseInt(e.target.value) })}
                                    />
                                ) : (
                                    `Stock: ${product.stock}`
                                )}
                            </Col>
                            <Col>
                                {editProduct && editProduct.id === product.id ? (
                                    <Button variant="success" onClick={handleSave}>Confirmar</Button>
                                ) : (
                                    <Button variant="primary" onClick={() => handleEdit(product)}>Modificar</Button>
                                )}
                            </Col>
                        </Row>
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </Container>
    );
};

export default EditProduct;
