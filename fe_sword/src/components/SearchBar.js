import React, { useEffect, useState } from 'react';
import './SearchBar.css';

const SearchBar = ({ setQuery, setPage }) => {
    
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        handleSearchSubmit()
    }, []);

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const handleSearchSubmit = () => {
        setQuery(`search=${searchTerm}`);
        setPage(1);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            handleSearchSubmit();
        }
    };

    return (
        <div className="search-bar">
            <input 
                type="text" 
                placeholder="Search by Title and Author..." 
                value={searchTerm} 
                onChange={handleSearchChange} 
                onKeyDown={handleKeyDown}
            />
            <button onClick={handleSearchSubmit}>Search</button>
        </div>
    );
};

export default SearchBar;
