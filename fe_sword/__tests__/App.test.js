import { act, render, screen } from '@testing-library/react';
import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import App from '../src/App';
import { mockApiBook, mockApiBooks } from '../src/setupMocks';

jest.mock('../src/api');

test('renders HomePage at the root path', async () => {
    mockApiBooks();

    await act(async () => {
        render(
            <MemoryRouter initialEntries={['/']}>
                <App />
            </MemoryRouter>
        );
    });

    expect(screen.getByText(/sword/i)).toBeInTheDocument();
    expect(screen.getByText(/book one/i)).toBeInTheDocument();
    expect(screen.getByText(/advanced/i)).toBeInTheDocument();
});

test('renders BookDetail when navigating to a book', async () => {
    mockApiBook();
    
    await act(async () => {
        render(
            <MemoryRouter initialEntries={[`/book/1`]}>
                <App />
            </MemoryRouter>
        );
    });

    expect(screen.getByText(/book one/i)).toBeInTheDocument();
});
