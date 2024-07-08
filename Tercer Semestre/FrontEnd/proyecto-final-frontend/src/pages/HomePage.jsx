// src/pages/HomePage.jsx

import React, { useContext, useEffect, useState } from 'react';
import { CartContext } from '../context/CartContext';
import { Container, Row, Col, Button, ListGroup, Form } from 'react-bootstrap';

const KEY = 'productList';

const HomePage = () => {
    const [products, setProducts] = useState([]);
    const { addToCart } = useContext(CartContext);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem(KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    const [quantities, setQuantities] = useState({});

    const handleQuantityChange = (productId, amount) => {
        setQuantities(prevQuantities => {
            const newQuantities = { ...prevQuantities };
            newQuantities[productId] = Math.max(0, (newQuantities[productId] || 0) + amount);
            return newQuantities;
        });
    };

    const handleAddToCart = (product) => {
        const quantity = quantities[product.id] || 0;
        if (quantity > 0 && quantity <= product.stock) {
            addToCart({ ...product, quantity });
            setProducts(products.map(p => p.id === product.id ? { ...p, stock: p.stock - quantity } : p));
            localStorage.setItem(KEY, JSON.stringify(products.map(p => p.id === product.id ? { ...p, stock: p.stock - quantity } : p)));
            setQuantities({ ...quantities, [product.id]: 0 });
        }
    };

    return (
        <Container>
            <h1 className="my-4">Productos a la Venta</h1>
            <ListGroup>
                {products.map(product => (
                    <ListGroup.Item key={product.id}>
                        <Row className="align-items-center">
                            <Col>{product.name}</Col>
                            <Col>${product.price}</Col>
                            <Col>Stock: {product.stock}</Col>
                            <Col>
                                <Button variant="outline-secondary" onClick={() => handleQuantityChange(product.id, -1)} disabled={(quantities[product.id] || 0) <= 0}>-</Button>
                                <span className="mx-2">{quantities[product.id] || 0}</span>
                                <Button variant="outline-secondary" onClick={() => handleQuantityChange(product.id, 1)} disabled={(quantities[product.id] || 0) >= product.stock}>+</Button>
                            </Col>
                            <Col>
                                <Button variant="primary" onClick={() => handleAddToCart(product)} disabled={(quantities[product.id] || 0) === 0 || (quantities[product.id] || 0) > product.stock}>
                                    Agregar al Carrito
                                </Button>
                            </Col>
                        </Row>
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </Container>
    );
};

export default HomePage;
