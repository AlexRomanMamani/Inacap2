// src/pages/EditProduct.jsx

import React, { useState, useEffect } from 'react';
import { Container, Table, Row, Col, Button, Form } from 'react-bootstrap';
import './ProductList.css'; // Importar el archivo CSS personalizado

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
            <h1 className="my-4 text-center">Modificar Producto</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th className="col-id">ID</th>
                        <th className="col-name">Nombre Producto</th>
                        <th className="col-price">Precio</th>
                        <th className="col-stock">Stock</th>
                        <th className="col-description">Descripción</th>
                        <th className="col-actions">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td className="col-id">{product.id}</td>
                            <td className="col-name">
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="text"
                                        value={editProduct.name}
                                        onChange={(e) => setEditProduct({ ...editProduct, name: e.target.value })}
                                    />
                                ) : (
                                    product.name
                                )}
                            </td>
                            <td className="col-price">
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="number"
                                        value={editProduct.price}
                                        onChange={(e) => setEditProduct({ ...editProduct, price: parseFloat(e.target.value) })}
                                    />
                                ) : (
                                    product.price
                                )}
                            </td>
                            <td className="col-stock">
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="number"
                                        value={editProduct.stock}
                                        onChange={(e) => setEditProduct({ ...editProduct, stock: parseInt(e.target.value) })}
                                    />
                                ) : (
                                    product.stock
                                )}
                            </td>
                            <td className="col-description">
                                {editProduct && editProduct.id === product.id ? (
                                    <Form.Control
                                        type="text"
                                        value={editProduct.description}
                                        onChange={(e) => setEditProduct({ ...editProduct, description: e.target.value })}
                                    />
                                ) : (
                                    product.description
                                )}
                            </td>
                            <td className="col-actions">
                                {editProduct && editProduct.id === product.id ? (
                                    <Button variant="success" onClick={handleSave}>Confirmar</Button>
                                ) : (
                                    <Button variant="primary" onClick={() => handleEdit(product)}>Modificar</Button>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
};

export default EditProduct;
