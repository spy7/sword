import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import AdvancedSearchBar from '../src/components/AdvancedSearchBar';

describe('AdvancedSearchBar Component', () => {
  const mockSetQuery = jest.fn();
  const mockSetPage = jest.fn();

  beforeEach(() => {
    mockSetQuery.mockClear();
    mockSetPage.mockClear();
  });

  test('renders input fields and search button', () => {
    render(<AdvancedSearchBar setQuery={mockSetQuery} setPage={mockSetPage} />);

    const titleInput = screen.getByPlaceholderText('Title');
    const authorInput = screen.getByPlaceholderText('Author');
    const isbnInput = screen.getByPlaceholderText('ISBN');
    const languageInput = screen.getByPlaceholderText('Language');
    const searchButton = screen.getByRole('button', { name: /search/i });

    expect(titleInput).toBeInTheDocument();
    expect(authorInput).toBeInTheDocument();
    expect(isbnInput).toBeInTheDocument();
    expect(languageInput).toBeInTheDocument();
    expect(searchButton).toBeInTheDocument();
  });

  test('updates input fields on user input', () => {
    render(<AdvancedSearchBar setQuery={mockSetQuery} setPage={mockSetPage} />);

    const titleInput = screen.getByPlaceholderText('Title');
    const authorInput = screen.getByPlaceholderText('Author');
    const isbnInput = screen.getByPlaceholderText('ISBN');
    const languageInput = screen.getByPlaceholderText('Language');

    fireEvent.change(titleInput, { target: { value: 'Book Title' } });
    fireEvent.change(authorInput, { target: { value: 'Author Name' } });
    fireEvent.change(isbnInput, { target: { value: '1234567890' } });
    fireEvent.change(languageInput, { target: { value: 'English' } });

    expect(titleInput.value).toBe('Book Title');
    expect(authorInput.value).toBe('Author Name');
    expect(isbnInput.value).toBe('1234567890');
    expect(languageInput.value).toBe('English');
  });

  test('calls setQuery and setPage when search button is clicked', () => {
    render(<AdvancedSearchBar setQuery={mockSetQuery} setPage={mockSetPage} />);

    const titleInput = screen.getByPlaceholderText('Title');
    const authorInput = screen.getByPlaceholderText('Author');
    const isbnInput = screen.getByPlaceholderText('ISBN');
    const languageInput = screen.getByPlaceholderText('Language');
    const searchButton = screen.getByRole('button', { name: /search/i });

    fireEvent.change(titleInput, { target: { value: 'Book Title' } });
    fireEvent.change(authorInput, { target: { value: 'Author Name' } });
    fireEvent.change(isbnInput, { target: { value: '1234567890' } });
    fireEvent.change(languageInput, { target: { value: 'English' } });

    fireEvent.click(searchButton);

    expect(mockSetQuery).toHaveBeenCalledWith('title=Book Title&authors=Author Name&isbn13=1234567890&language_code=English');
    expect(mockSetPage).toHaveBeenCalledWith(1);
  });

  test('calls setQuery and setPage when pressing Enter in any input field', () => {
    render(<AdvancedSearchBar setQuery={mockSetQuery} setPage={mockSetPage} />);

    const titleInput = screen.getByPlaceholderText('Title');
    const authorInput = screen.getByPlaceholderText('Author');
    const isbnInput = screen.getByPlaceholderText('ISBN');
    const languageInput = screen.getByPlaceholderText('Language');

    fireEvent.change(titleInput, { target: { value: 'Book Title' } });
    fireEvent.change(authorInput, { target: { value: 'Author Name' } });
    fireEvent.change(isbnInput, { target: { value: '1234567890' } });
    fireEvent.change(languageInput, { target: { value: 'English' } });

    fireEvent.keyDown(titleInput, { key: 'Enter', code: 'Enter' });

    expect(mockSetQuery).toHaveBeenCalledWith('title=Book Title&authors=Author Name&isbn13=1234567890&language_code=English');
    expect(mockSetPage).toHaveBeenCalledWith(1);
  });
});
