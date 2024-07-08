// src/pages/CartPage.jsx

import React, { useContext, useState, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { CartContext } from '../context/CartContext';
import { Container, Row, Col, Button, ListGroup, Table } from 'react-bootstrap';

const PURCHASE_KEY = 'purchaseList';
const PRODUCT_KEY = 'productList';

const CartPage = () => {
    const { cart, clearCart, removeFromCart, totalPrice } = useContext(CartContext);
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

    const confirmPurchase = () => {
        const purchase = {
            id: uuidv4(),
            date: new Date(),
            products: cart,
            totalPrice,
            status: 'completada'
        };
        const newPurchases = [...purchases, purchase];
        setPurchases(newPurchases);
        clearCart();
    };

    const handleRemoveFromCart = (product) => {
        removeFromCart(product);
        const updatedProducts = products.map(p => {
            if (p.id === product.id) {
                return { ...p, stock: p.stock + product.quantity };
            }
            return p;
        });
        setProducts(updatedProducts);
    };

    return (
        <Container>
            <h1 className="my-4">Carrito</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Nombre Producto</th>
                        <th>Precio Unitario</th>
                        <th>Cantidad</th>
                        <th>Total Producto</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {cart.map((item, index) => (
                        <tr key={index}>
                            <td>{item.name}</td>
                            <td>${item.price}</td>
                            <td>x {item.quantity}</td>
                            <td>= ${item.total}</td>
                            <td>
                                <Button variant="danger" onClick={() => handleRemoveFromCart(item)}>Eliminar</Button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
            <h2 className="my-4">Total Compra: ${totalPrice}</h2>
            <Button variant="success" onClick={confirmPurchase}>Confirmar Compra</Button>
        </Container>
    );
};

export default CartPage;
