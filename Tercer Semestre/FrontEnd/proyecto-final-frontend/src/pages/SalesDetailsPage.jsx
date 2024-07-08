// src/pages/SalesDetailsPage.jsx

import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Button, ListGroup } from 'react-bootstrap';
import './SalesDetailsPage.css';

const PURCHASE_KEY = 'purchaseList';
const PRODUCT_KEY = 'productList';

const SalesDetailsPage = () => {
    const [purchases, setPurchases] = useState([]);
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const storedPurchases = JSON.parse(localStorage.getItem(PURCHASE_KEY));
        if (storedPurchases) setPurchases(storedPurchases);

        const storedProducts = JSON.parse(localStorage.getItem(PRODUCT_KEY));
        if (storedProducts) setProducts(storedProducts);
    }, []);

    useEffect(() => {
        localStorage.setItem(PURCHASE_KEY, JSON.stringify(purchases));
    }, [purchases]);

    useEffect(() => {
        localStorage.setItem(PRODUCT_KEY, JSON.stringify(products));
    }, [products]);

    const annulPurchase = (id) => {
        const confirmAnnulment = window.confirm('¿Estás seguro de que deseas anular esta venta?');

        if (!confirmAnnulment) return;

        const updatedPurchases = purchases.map(purchase => {
            if (purchase.id === id) {
                const updatedProducts = products.map(product => {
                    const purchasedItem = purchase.products.find(item => item.id === product.id);
                    if (purchasedItem) {
                        return { ...product, stock: product.stock + purchasedItem.quantity };
                    }
                    return product;
                });

                setProducts(updatedProducts);
                return { ...purchase, status: 'anulada' };
            }
            return purchase;
        });

        setPurchases(updatedPurchases);
    };

    return (
        <Container>
            <h1 className="my-4">Detalles de Ventas</h1>
            {purchases.length === 0 ? (
                <p>No hay detalles de ventas disponibles.</p>
            ) : (
                <ListGroup>
                    {purchases.map(purchase => (
                        <ListGroup.Item key={purchase.id}>
                            <Row className="d-flex align-items-center">
                                <Col>
                                    Código: {purchase.id} - Fecha: {new Date(purchase.date).toLocaleString()} - Estado: <span className="text-nowrap">{purchase.status}</span>
                                </Col>
                                <Col className="text-right d-flex align-items-center justify-content-end">
                                    <h5 className="mr-3 mb-0">Total Venta: ${purchase.totalPrice}</h5>
                                    {purchase.status !== 'anulada' && (
                                        <Button variant="warning" onClick={() => annulPurchase(purchase.id)}>Anular Venta</Button>
                                    )}
                                </Col>
                            </Row>
                            <ListGroup className="mt-2">
                                <ListGroup.Item>
                                    <Row>
                                        <Col><strong>Nombre Producto</strong></Col>
                                        <Col><strong>Precio</strong></Col>
                                        <Col><strong>Cantidad</strong></Col>
                                        <Col><strong>Total</strong></Col>
                                    </Row>
                                </ListGroup.Item>
                                {purchase.products.map((product, index) => (
                                    <ListGroup.Item key={index}>
                                        <Row>
                                            <Col>{product.name}</Col>
                                            <Col>${product.price}</Col>
                                            <Col>{product.quantity}</Col>
                                            <Col>${product.total}</Col>
                                        </Row>
                                    </ListGroup.Item>
                                ))}
                            </ListGroup>
                        </ListGroup.Item>
                    ))}
                </ListGroup>
            )}
        </Container>
    );
};

export default SalesDetailsPage;
