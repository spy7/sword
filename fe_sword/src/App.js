import React from 'react';
import { Route, Routes } from 'react-router-dom';
import BookDetail from './pages/BookDetail';
import HomePage from './pages/HomePage';

function App() {
    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/book/:id" element={<BookDetail />} />
        </Routes>
    );
}

export default App;
