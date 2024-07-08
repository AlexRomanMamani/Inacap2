// src/App.jsx

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { NavBar } from './components/NavBar';
import HomePage from './pages/HomePage';
import CartPage from './pages/CartPage';
import SalesDetailsPage from './pages/SalesDetailsPage';
import ProductList from './pages/ProductList';
import AddProduct from './pages/AddProduct';
import EditProduct from './pages/EditProduct';
import DeleteProduct from './pages/DeleteProduct';
import { CartProvider } from './context/CartContext';

function App() {
    return (
        <CartProvider>
            <Router>
                <NavBar />
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/cart" element={<CartPage />} />
                    <Route path="/sales-details" element={<SalesDetailsPage />} />
                    <Route path="/products/list" element={<ProductList />} />
                    <Route path="/products/add" element={<AddProduct />} />
                    <Route path="/products/edit" element={<EditProduct />} />
                    <Route path="/products/delete" element={<DeleteProduct />} />
                </Routes>
            </Router>
        </CartProvider>
    );
}

export default App;
