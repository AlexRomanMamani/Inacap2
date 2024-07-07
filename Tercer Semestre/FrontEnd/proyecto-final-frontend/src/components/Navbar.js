// src/components/Navbar.js

import React from 'react';
import { Navbar, Nav, NavDropdown } from 'react-bootstrap';

const NavigationBar = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="/">Nombre de la Empresa</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="/">Inicio</Nav.Link>
                    <Nav.Link href="/about">Sobre Nosotros</Nav.Link>
                    <Nav.Link href="/policies">Políticas de Ventas</Nav.Link>
                    <NavDropdown title="Productos" id="basic-nav-dropdown">
                        <NavDropdown.Item href="/products">Mantenedor de Productos</NavDropdown.Item>
                        <NavDropdown.Item href="/purchase">Módulo de Compra</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="/sales-details">Detalles de Ventas</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default NavigationBar;
