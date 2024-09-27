import React, { useEffect, useState } from 'react';
import './AdvancedSearchBar.css';

const AdvancedSearchBar = ({ setQuery, setPage }) => {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [isbn, setIsbn] = useState('');
    const [language, setLanguage] = useState('');

    useEffect(() => {
        handleAdvancedSearch()
    }, []);

    const handleAdvancedSearch = () => {
        setQuery(`title=${title}&authors=${author}&isbn13=${isbn}&language_code=${language}`);
        setPage(1);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            handleAdvancedSearch();
        }
    };

    return (
        <div className="advanced-search">
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                onKeyDown={handleKeyDown}
            />
            <input
                type="text"
                placeholder="Author"
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                onKeyDown={handleKeyDown}
            />
            <input
                type="text"
                placeholder="ISBN"
                value={isbn}
                onChange={(e) => setIsbn(e.target.value)}
                onKeyDown={handleKeyDown}
            />
            <input
                type="text"
                placeholder="Language"
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                onKeyDown={handleKeyDown}
            />
            <button onClick={handleAdvancedSearch}>Search</button>
        </div>
    );
};

export default AdvancedSearchBar;
