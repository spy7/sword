import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import api from '../api';
import Header from '../components/Header';
import './BookDetail.css';

const BookDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [book, setBook] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBookDetail = async () => {
      try {
        const response = await api.get(`/book/${id}`);
        setBook(response.data);
      } catch (error) {
        console.error('Error fetching book details:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchBookDetail();
  }, [id]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (!book) {
    return <p>Book not found.</p>;
  }

  return (
    <div className="book-detail">
        <Header />
        <div className="book-detail-content">
            <img src={book.image_url} alt={book.title} className="book-detail-image" />
            <div className="book-info">
                <h1 className="book-title">{book.title}</h1>
                <h2 className="book-authors">Authors: {book.authors}</h2>
                <p><strong>ISBN:</strong> {book.isbn}</p>
                <p><strong>Publication Year:</strong> {book.original_publication_year}</p>
                <p><strong>Average Rating:</strong> {book.average_rating} ({book.ratings_count} ratings)</p>
                <p><strong>Language:</strong> {book.language_code}</p>
                <button onClick={() => navigate(-1)} className="go-back-button">
                    Go Back
                </button>
            </div>
        </div>
    </div>
  );
};

export default BookDetail;
