import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-left">
        <h1>Sword</h1>
        <h2>FrontEnd</h2>
      </div>
      <div className="header-center">
        <h3>
          <Link to="/" className="header-link">
            Book
          </Link>
        </h3>
      </div>
    </header>
  );
};

export default Header;
