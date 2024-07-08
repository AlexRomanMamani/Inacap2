// src/context/CartContext.js

import React, { createContext, useState, useEffect } from 'react';

const CART_KEY = 'cartItems';

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
    const [cart, setCart] = useState([]);
    const [totalPrice, setTotalPrice] = useState(0);

    useEffect(() => {
        const storedCart = JSON.parse(localStorage.getItem(CART_KEY));
        if (storedCart) setCart(storedCart);

        const storedTotalPrice = JSON.parse(localStorage.getItem('totalPrice'));
        if (storedTotalPrice) setTotalPrice(storedTotalPrice);
    }, []);

    useEffect(() => {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
        localStorage.setItem('totalPrice', JSON.stringify(totalPrice));
    }, [cart, totalPrice]);

    const addToCart = (product) => {
        setCart((prevCart) => {
            const existingProduct = prevCart.find(item => item.id === product.id);
            if (existingProduct) {
                return prevCart.map(item =>
                    item.id === product.id ? { ...item, quantity: item.quantity + product.quantity, total: (item.quantity + product.quantity) * item.price } : item
                );
            }
            return [...prevCart, { ...product, total: product.quantity * product.price }];
        });
        setTotalPrice(prevTotal => prevTotal + product.price * product.quantity);
    };

    const removeFromCart = (product) => {
        setCart((prevCart) => prevCart.filter(item => item.id !== product.id));
        setTotalPrice(prevTotal => prevTotal - product.total);
    };

    const clearCart = () => {
        setCart([]);
        setTotalPrice(0);
    };

    return (
        <CartContext.Provider value={{ cart, addToCart, removeFromCart, clearCart, totalPrice }}>
            {children}
        </CartContext.Provider>
    );
};
