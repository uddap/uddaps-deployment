import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <div className="App">
      <nav>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#products">Products</a></li>
          <li><a href="#contact-us">Contact Us</a></li>
          {isLoggedIn ? (
            <li><a href="#logout" onClick={handleLogout}>Logout</a></li>
          ) : (
            <>
              <li><a href="#register">Register</a></li>
              <li><a href="#login" onClick={handleLogin}>Login</a></li>
            </>
          )}
          <li>
            <form>
              <input type="text" placeholder="Search" value={searchTerm} onChange={handleSearch} />
              <button type="submit">Search</button>
            </form>
          </li>
        </ul>
      </nav>
      <div className="content">
        {/* your content here */Welcome to umaz web application}
      </div>
    </div>
  );
};

export default App;
