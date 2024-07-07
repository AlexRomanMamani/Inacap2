// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NavigationBar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Policies from './pages/Policies';
import Products from './pages/Products';
import Purchase from './pages/Purchase';
import SalesDetails from './pages/SalesDetails';

function App() {
  return (
    <Router>
      <div>
        <NavigationBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" component={About} />
          <Route path="/policies" component={Policies} />
          <Route path="/products" component={Products} />
          <Route path="/purchase" component={Purchase} />
          <Route path="/sales-details" component={SalesDetails} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
