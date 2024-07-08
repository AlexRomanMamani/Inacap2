// src/components/NavBar.jsx

import React, { useContext } from 'react';
import { Navbar, Nav, NavDropdown } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { CartContext } from '../context/CartContext';

export function NavBar() {
	const { cart } = useContext(CartContext);

	return (
		<Navbar bg="light" expand="lg">
			<Navbar.Brand as={Link} to="/">Nombre de la Empresa</Navbar.Brand>
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="mr-auto">
					<NavDropdown title="Productos" id="basic-nav-dropdown">
						<NavDropdown.Item as={Link} to="/products/list">Enlistar</NavDropdown.Item>
						<NavDropdown.Item as={Link} to="/products/add">Agregar</NavDropdown.Item>
						<NavDropdown.Item as={Link} to="/products/edit">Modificar</NavDropdown.Item>
						<NavDropdown.Item as={Link} to="/products/delete">Eliminar</NavDropdown.Item>
					</NavDropdown>
					<Nav.Link as={Link} to="/purchase">Comprar</Nav.Link>
					<Nav.Link as={Link} to="/sales-details">Detalles de Ventas</Nav.Link>
				</Nav>
				<Nav>
					<Nav.Link as={Link} to="/cart">
						<i className="bi bi-cart-fill"></i> ({cart.length})
					</Nav.Link>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
	);
}
