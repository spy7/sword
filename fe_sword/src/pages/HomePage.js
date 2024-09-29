import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api';
import AdvancedButton from '../components/AdvancedButton';
import AdvancedSearchBar from '../components/AdvancedSearchBar';
import Header from '../components/Header';
import Pagination from '../components/Pagination';
import SearchBar from '../components/SearchBar';
import './HomePage.css';

const HomePage = () => {
    const [books, setBooks] = useState([]);
    const [page, setPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [loading, setLoading] = useState(false);
    const [query, setQuery] = useState('');
    const [advanced, setAdvanced] = useState(false);

    const books_per_page = 30;

    useEffect(() => {
        const fetchBooks = async () => {
            setLoading(true);
            try {
                const response = await api.get(`/v1/books/?limit=${books_per_page}&offset=${books_per_page * (page - 1)}&${query}`);
                setBooks(response.data.results);
                setTotalPages(Math.ceil(response.data.count / books_per_page));
            } catch (error) {
                console.error('Error fetching books:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchBooks();
    }, [page, query]);

    const nextPage = () => {
        if (page < totalPages) {
            setPage(prevPage => prevPage + 1);
        }
    };

    const prevPage = () => {
        if (page > 1) {
            setPage(prevPage => prevPage - 1);
        }
    };

    const toggleAdvancedSearch = () => {
        setAdvanced(prev => !prev);
    };

    return (
        <div className="homepage">
            <Header />

            <div className="search-container">
                <div className="search-bar">
                    {advanced ?
                        <AdvancedSearchBar setQuery={setQuery} setPage={setPage} /> :
                        <SearchBar setQuery={setQuery} setPage={setPage} />}
                </div>
                <div className="advanced-button">
                    <AdvancedButton advanced={advanced} toggleAdvancedSearch={toggleAdvancedSearch} />
                </div>
            </div>

            <Pagination page={page} totalPages={totalPages} onPrev={prevPage} onNext={nextPage} />

            <div className="book-list">
                {books.map(book => (
                    <Link to={`/book/${book.book_id}`} key={book.book_id} className="book-item">
                        <img src={book.image_url} alt={book.title} className="book-image" />
                        <h3>{book.title}</h3>
                        <p>{book.authors}</p>
                    </Link>
                ))}
            </div>

            <Pagination page={page} totalPages={totalPages} onPrev={prevPage} onNext={nextPage} />
        </div>
    );
};

export default HomePage;
