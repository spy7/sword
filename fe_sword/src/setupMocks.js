import api from './api';

const mock_books = [
    {
        book_id: 1,
        title: 'Book One',
        authors: 'Author One',
        isbn13: '1234567890123',
        original_publication_year: 2000,
        average_rating: 4.5,
        ratings_count: 200,
        language_code: 'eng',
        image_url: 'image1.jpg'
    },
    {
        book_id: 2,
        title: 'Mock book',
        authors: 'Somebody',
        isbn13: '5555555555555',
        original_publication_year: 1999,
        average_rating: 4.0,
        ratings_count: 50,
        language_code: 'pt',
        image_url: 'image2.jpg'
    },
];

export const mockApiBook = () => {
    api.get.mockResolvedValueOnce({ data: mock_books[0] });
};

export const mockApiBooks = () => {
    api.get.mockResolvedValue({ data: { count: 50, results: mock_books } });
};

