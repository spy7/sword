import { act, render, fireEvent, screen } from '@testing-library/react';
import React from 'react';
import BookReserveModal from '../src/pages/BookReserveModal';

const onReserveMock = jest.fn();
const onCloseMock = jest.fn();

describe('BookReserveModal Component', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  test('should not render the modal when isOpen is false', async () => {
    await act(async () => {
      render(
        <BookReserveModal isOpen={false} onReserve={onReserveMock} onClose={onCloseMock} />
      );
    });
    expect(screen.queryByText(/Reserve Book/i)).not.toBeInTheDocument();
  });

  test('should render the modal when isOpen is true', async () => {
    await act(async () => {
      render(
        <BookReserveModal isOpen={true} onReserve={onReserveMock} onClose={onCloseMock} />
      );
    });
    expect(screen.getByText(/Reserve Book/i)).toBeInTheDocument();
  });

  test('should focus on the customer_name input when the modal is opened', async () => {
    await act(async () => {
      render(
        <BookReserveModal isOpen={true} onReserve={onReserveMock} onClose={onCloseMock} />
      );
    });
    const nameInput = screen.getByPlaceholderText('Your name');
    expect(nameInput).toHaveFocus();
  });

  test('should call onReserve with form data when Reserve button is clicked', async () => {
    await act(async () => {
      render(
        <BookReserveModal isOpen={true} onReserve={onReserveMock} onClose={onCloseMock} />
      );
    });

    const nameInput = screen.getByPlaceholderText('Your name');
    const emailInput = screen.getByPlaceholderText('Your e-mail');
    const reserveButton = screen.getAllByText(/Reserve/i)[1];

    fireEvent.change(nameInput, { target: { value: 'Someone' } });
    fireEvent.change(emailInput, { target: { value: 'some@example.com' } });
    fireEvent.click(reserveButton);

    expect(onReserveMock).toHaveBeenCalledWith({
      customer_name: 'Someone',
      customer_email: 'some@example.com',
    });
  });

  test('should clear the form data and call onClose when clicking the close button', async () => {
    await act(async () => {
      render(
        <BookReserveModal isOpen={true} onReserve={onReserveMock} onClose={onCloseMock} />
      );
    });

    const closeButton = screen.getByText('×');
    fireEvent.click(closeButton);

    expect(onCloseMock).toHaveBeenCalled();
    expect(screen.queryByPlaceholderText('Your name').value).toBe('');
    expect(screen.queryByPlaceholderText('Your e-mail').value).toBe('');
  });
});
