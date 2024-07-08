// src/pages/HomePage.jsx

import React, { useContext, useEffect, useState } from 'react';
import { CartContext } from '../context/CartContext';
import { Container, Row, Col, Card, Button, Form } from 'react-bootstrap';
import './HomePage.css'; // Importar el archivo CSS personalizado

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
            <h1 className="my-4 text-center">Productos a la Venta</h1>
            <Row>
                {products.map(product => (
                    <Col md={4} key={product.id} className="mb-4">
                        <Card className="product-card">
                            <Card.Img variant="top" src={product.image} alt={product.name} className="product-image" />
                            <Card.Body>
                                <Card.Title>{product.name}</Card.Title>
                                <Card.Text>
                                    <strong>Precio:</strong> ${product.price}<br />
                                    <strong>Stock:</strong> {product.stock}<br />
                                    <strong>Descripción:</strong> {product.description}
                                </Card.Text>
                                <div className="d-flex justify-content-between align-items-center">
                                    <div>
                                        <Button variant="outline-secondary" onClick={() => handleQuantityChange(product.id, -1)} disabled={(quantities[product.id] || 0) <= 0}>-</Button>
                                        <span className="mx-2">{quantities[product.id] || 0}</span>
                                        <Button variant="outline-secondary" onClick={() => handleQuantityChange(product.id, 1)} disabled={(quantities[product.id] || 0) >= product.stock}>+</Button>
                                    </div>
                                    <Button variant="primary" onClick={() => handleAddToCart(product)} disabled={(quantities[product.id] || 0) === 0 || (quantities[product.id] || 0) > product.stock}>
                                        Agregar al Carrito
                                    </Button>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default HomePage;
