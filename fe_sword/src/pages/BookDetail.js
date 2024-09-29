import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import api from '../api';
import Header from '../components/Header';
import './BookDetail.css';
import BookReserveModal from './BookReserveModal';

const BookDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [book, setBook] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isReserved, setIsReserved] = useState(false);

  useEffect(() => {
    const fetchBookDetail = async () => {
      try {
        const response = await api.get(`/v1/book/${id}/`);
        setBook(response.data);
        setIsReserved(response.data.is_reserved);
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

  const handleReserve = async (formData) => {
    try {
      const response = await api.post(`/v1/book/${id}/reserve/`, JSON.stringify(formData), {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.status === 201) {
        setIsReserved(true);
      } else if (response.status === 409) {
        alert('This book was already reserved.');
        setIsReserved(true);
      } else {
        const errorData = await response.json();
        alert(`Error: ${errorData.message || 'Something went wrong.'}`);
      }
    } catch (error) {
      const errorMessages = error.response.data;
      const formattedMessages = Object.values(errorMessages).flat().join(', ');
      alert(`${formattedMessages}`);
    }
  };

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
          <button onClick={() => setIsModalOpen(true)} disabled={isReserved} className="reserve-button">
            {isReserved ? 'Reserved' : 'Reserve Book'}
          </button>
          <button onClick={() => navigate(-1)} className="go-back-button">
            Go Back
          </button>
          <BookReserveModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} onReserve={handleReserve} />
        </div>
      </div>
    </div>
  );
};

export default BookDetail;
