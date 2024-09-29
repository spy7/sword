import { act, fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import api from '../src/api';
import BookDetail from '../src/pages/BookDetail';
import { mockApiBook } from '../src/setupMocks';

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
    jest.spyOn(window, 'alert').mockImplementation(() => {});
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

  test('displays modal and handles reservation submission', async () => {

    mockApiBook();

    api.post.mockResolvedValueOnce({ status: 201 });

    await act(async () => {
      render(
        <BrowserRouter>
          <BookDetail />
        </BrowserRouter>
      );
    });

    await waitFor(() => {
      expect(screen.getByText(/Book One/i)).toBeInTheDocument();
    });

    const reserveButton = screen.getByText(/Reserve Book/i);
    fireEvent.click(reserveButton);

    expect(screen.getByPlaceholderText(/Your name/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Your e-mail/i)).toBeInTheDocument();

    fireEvent.change(screen.getByPlaceholderText(/Your name/i), { target: { value: 'Someone' } });
    fireEvent.change(screen.getByPlaceholderText(/Your e-mail/i), { target: { value: 'some@example.com' } });

    fireEvent.click(screen.getAllByText(/Reserve/i)[2]);

    await waitFor(() => {
      expect(api.post).toHaveBeenCalledWith(
        '/v1/book/1/reserve/',
        JSON.stringify({ customer_name: 'Someone', customer_email: 'some@example.com' }),
        { headers: { 'Content-Type': 'application/json' } }
      );
    });

    await waitFor(() => {
      expect(screen.getByText('Reserved')).toBeDisabled();
    });
  });

  test('displays error if reservation fails (409 conflict)', async () => {

    mockApiBook();

    api.post.mockRejectedValueOnce({
      response: {
        status: 409,
        data: {
          message: 'This book was already reserved.'
        }
      }
    });

    await act(async () => {
      render(
        <BrowserRouter>
          <BookDetail />
        </BrowserRouter>
      );
    });

    await waitFor(() => {
      expect(screen.getByText(/Book One/i)).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText(/Reserve Book/i));

    fireEvent.change(screen.getByPlaceholderText(/Your name/i), { target: { value: 'Someone' } });
    fireEvent.change(screen.getByPlaceholderText(/Your e-mail/i), { target: { value: 'some@example.com' } });

    fireEvent.click(screen.getAllByText(/Reserve/i)[2]);

    await waitFor(() => {
      expect(window.alert).toHaveBeenCalledWith('This book was already reserved.');
    });

    expect(screen.getByText(/Reserve Book/i)).toBeEnabled();
  });
});
