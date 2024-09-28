import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import SearchBar from '../src/components/SearchBar';

describe('SearchBar Component', () => {
    let setQueryMock, setPageMock;

    beforeEach(() => {
        setQueryMock = jest.fn();
        setPageMock = jest.fn();
    });

    test('renders search input and button', () => {
        render(<SearchBar setQuery={setQueryMock} setPage={setPageMock} />);
       
        const inputElement = screen.getByPlaceholderText(/Search by Title and Author.../i);
        const buttonElement = screen.getByText(/Search/i);

        expect(inputElement).toBeInTheDocument();
        expect(buttonElement).toBeInTheDocument();
    });

    test('updates the search term on user input', () => {
        render(<SearchBar setQuery={setQueryMock} setPage={setPageMock} />);

        const inputElement = screen.getByPlaceholderText(/Search by Title and Author.../i);
       
        fireEvent.change(inputElement, { target: { value: 'React' } });

        expect(inputElement.value).toBe('React');
    });

    test('calls setQuery and setPage when clicking the search button', () => {
        render(<SearchBar setQuery={setQueryMock} setPage={setPageMock} />);

        const inputElement = screen.getByPlaceholderText(/Search by Title and Author.../i);
        const buttonElement = screen.getByText(/Search/i);
       
        fireEvent.change(inputElement, { target: { value: 'React' } });

        fireEvent.click(buttonElement);
       
        expect(setQueryMock).toHaveBeenCalledWith('search=React');
        expect(setPageMock).toHaveBeenCalledWith(1);
    });

    test('calls setQuery and setPage when pressing Enter key', () => {
        render(<SearchBar setQuery={setQueryMock} setPage={setPageMock} />);

        const inputElement = screen.getByPlaceholderText(/Search by Title and Author.../i);

        fireEvent.change(inputElement, { target: { value: 'JavaScript' } });
       
        fireEvent.keyDown(inputElement, { key: 'Enter', code: 'Enter' });
       
        expect(setQueryMock).toHaveBeenCalledWith('search=JavaScript');
        expect(setPageMock).toHaveBeenCalledWith(1);
    });
});
