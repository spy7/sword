import { act, render, screen, waitFor, fireEvent } from '@testing-library/react';
import React from 'react';
import { BrowserRouter, useNavigate } from 'react-router-dom';
import BookDetail from '../src/pages/BookDetail';
import { mockApiBook } from '../src/setupMocks';
import api from '../src/api';

jest.mock('../src/api');
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useParams: () => ({ id: '1' }),
  useNavigate: jest.fn(),
}));

describe('BookDetail Component', () => {
  const mockNavigate = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    require('react-router-dom').useNavigate.mockImplementation(() => mockNavigate);
  });

  test('renders book details after fetching data', async () => {
    mockApiBook();

    await act(async () => {
      render(
        <BrowserRouter>
          <BookDetail />
        </BrowserRouter>
      );
    });

    await waitFor(() => {
      expect(screen.getByText(/book one/i)).toBeInTheDocument();
      expect(screen.getByText(/authors: author one/i)).toBeInTheDocument();
    });
  });

  test('renders "Book not found" if no book data is returned', async () => {
    api.get.mockResolvedValueOnce({ data: null });

    await act(async () => {
      render(
        <BrowserRouter>
          <BookDetail />
        </BrowserRouter>
      );
    });

    await waitFor(() => {
      expect(screen.getByText(/book not found/i)).toBeInTheDocument();
    });
  });

  test('navigates back when "Go Back" button is clicked', async () => {
    mockApiBook();

    await act(async () => {
      render(
        <BrowserRouter>
          <BookDetail />
        </BrowserRouter>
      );
    });

    await waitFor(() => {
      expect(screen.getByText(/book one/i)).toBeInTheDocument();
    });

    const goBackButton = screen.getByText(/go back/i);
    fireEvent.click(goBackButton);

    expect(mockNavigate).toHaveBeenCalledWith(-1);
  });
});
