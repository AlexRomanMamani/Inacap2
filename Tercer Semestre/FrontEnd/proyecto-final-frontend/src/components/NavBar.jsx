import React, { useContext } from 'react';
import { Navbar, Nav, NavDropdown, Container, OverlayTrigger, Tooltip } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { CartContext } from '../context/CartContext';
import './NavBar.css'; // Importar el archivo CSS personalizado
import logo from '../assets/logo-pokeball.png'; // Importar la imagen

export function NavBar() {
    const { cart } = useContext(CartContext);

    return (
        <Navbar expand="lg" className="navbar-custom mb-4">
            <Container>
                <Navbar.Brand as={Link} to="/">
                    <img
                        src={logo} // Usar la imagen importada
                        width="30"
                        height="30"
                        className="d-inline-block align-top"
                        alt="PokéTienda logo"
                    />
                    {' '}
                    PokéTienda
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link as={Link} to="/">Inicio</Nav.Link>
                        <NavDropdown title="Mantenedor de Productos" id="basic-nav-dropdown">
                            <NavDropdown.Item as={Link} to="/products/list">Enlistar</NavDropdown.Item>
                            <NavDropdown.Item as={Link} to="/products/add">Agregar</NavDropdown.Item>
                            <NavDropdown.Item as={Link} to="/products/edit">Modificar</NavDropdown.Item>
                            <NavDropdown.Item as={Link} to="/products/delete">Eliminar</NavDropdown.Item>
                        </NavDropdown>
                        <Nav.Link as={Link} to="/purchase">Comprar</Nav.Link>
                        <Nav.Link as={Link} to="/sales-details">Detalles de Ventas</Nav.Link>
                    </Nav>
                    <Nav>
                        <OverlayTrigger
                            placement="bottom"
                            overlay={
                                <Tooltip id="cart-tooltip">
                                    {cart.length > 0 ? `Tienes ${cart.length} productos en el carrito` : 'No tienes productos en el carrito'}
                                </Tooltip>
                            }
                        >
                            <Nav.Link as={Link} to="/cart">
                                <i className={`bi bi-cart-fill ${cart.length > 0 ? 'cart-icon-filled' : 'cart-icon'}`}></i> ({cart.length})
                            </Nav.Link>
                        </OverlayTrigger>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}
