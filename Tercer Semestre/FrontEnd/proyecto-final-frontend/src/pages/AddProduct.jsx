// src/pages/AddProduct.jsx

import React, { useRef, useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { Container, Form, Row, Col, Button } from 'react-bootstrap';

const KEY = 'productList';

const AddProduct = () => {
    const nameRef = useRef();
    const priceRef = useRef();
    const stockRef = useRef();
    const imageRef = useRef();
    const descriptionRef = useRef();
    const [imagePreview, setImagePreview] = useState(''); // Nuevo estado para la vista previa de la imagen

    const addProduct = () => {
        const name = nameRef.current.value;
        const price = priceRef.current.value;
        const stock = stockRef.current.value;
        const image = imageRef.current.value;
        const description = descriptionRef.current.value;

        if (name === '' || price === '' || stock === '' || image === '' || description === '') return;

        const newProduct = {
            id: uuidv4(),
            name,
            price: parseFloat(price),
            stock: parseInt(stock),
            image,
            description
        };

        const storedProducts = JSON.parse(localStorage.getItem(KEY)) || [];
        storedProducts.push(newProduct);
        localStorage.setItem(KEY, JSON.stringify(storedProducts));

        nameRef.current.value = null;
        priceRef.current.value = null;
        stockRef.current.value = null;
        imageRef.current.value = null;
        descriptionRef.current.value = null;
        setImagePreview(''); // Limpiar la vista previa de la imagen
    };

    const handleImageChange = () => {
        const imageUrl = imageRef.current.value;
        setImagePreview(imageUrl); // Actualizar la vista previa de la imagen
    };

    return (
        <Container>
            <h1 className="my-4 text-center">Agregar Producto</h1>
            <Row className="justify-content-center">
                <Col md={6}>
                    <Form>
                        <Form.Group controlId="formProductName" className="mb-3">
                            <Form.Label>Nombre del Producto</Form.Label>
                            <Form.Control type="text" placeholder="Nombre del producto" ref={nameRef} />
                        </Form.Group>
                        <Form.Group controlId="formProductPrice" className="mb-3">
                            <Form.Label>Precio del Producto</Form.Label>
                            <Form.Control type="number" placeholder="Precio del producto" ref={priceRef} />
                        </Form.Group>
                        <Form.Group controlId="formProductStock" className="mb-3">
                            <Form.Label>Stock del Producto</Form.Label>
                            <Form.Control type="number" placeholder="Stock del producto" ref={stockRef} />
                        </Form.Group>
                        <Form.Group controlId="formProductImage" className="mb-3">
                            <Form.Label>URL de la Imagen del Producto</Form.Label>
                            <Form.Control type="text" placeholder="URL de la imagen" ref={imageRef} onChange={handleImageChange} />
                        </Form.Group>
                        <Form.Group controlId="formProductDescription" className="mb-3">
                            <Form.Label>Descripción del Producto</Form.Label>
                            <Form.Control as="textarea" rows={3} placeholder="Descripción del producto" ref={descriptionRef} />
                        </Form.Group>
                        <Button variant="primary" onClick={addProduct} className="w-100">Agregar Producto</Button>
                    </Form>
                </Col>
                <Col md={6} className="d-flex align-items-center justify-content-center">
                    {imagePreview && <img src={imagePreview} alt="Vista previa del producto" style={{ maxWidth: '100%', maxHeight: '200px' }} />}
                </Col>
            </Row>
        </Container>
    );
};

export default AddProduct;
