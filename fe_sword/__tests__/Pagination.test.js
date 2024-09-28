import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Pagination from '../src/components/Pagination';

describe('Pagination Component', () => {
    const mockOnPrev = jest.fn();
    const mockOnNext = jest.fn();

    beforeEach(() => {
        jest.clearAllMocks();
    });

    test('renders pagination with correct page and total pages', () => {
        render(<Pagination page={1} totalPages={5} onPrev={mockOnPrev} onNext={mockOnNext} />);
        
        expect(screen.getByText('Page 1 of 5')).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /previous/i })).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /next/i })).toBeInTheDocument();
    });

    test('disables the previous button on the first page', () => {
        render(<Pagination page={1} totalPages={5} onPrev={mockOnPrev} onNext={mockOnNext} />);
        
        const prevButton = screen.getByRole('button', { name: /previous/i });
        expect(prevButton).toBeDisabled();
    });

    test('does not disable the previous button on other pages', () => {
        render(<Pagination page={2} totalPages={5} onPrev={mockOnPrev} onNext={mockOnNext} />);
        
        const prevButton = screen.getByRole('button', { name: /previous/i });
        expect(prevButton).not.toBeDisabled();
    });

    test('disables the next button on the last page', () => {
        render(<Pagination page={5} totalPages={5} onPrev={mockOnPrev} onNext={mockOnNext} />);
        
        const nextButton = screen.getByRole('button', { name: /next/i });
        expect(nextButton).toBeDisabled();
    });

    test('calls onPrev when previous button is clicked', () => {
        render(<Pagination page={2} totalPages={5} onPrev={mockOnPrev} onNext={mockOnNext} />);
        
        const prevButton = screen.getByRole('button', { name: /previous/i });
        fireEvent.click(prevButton);
        expect(mockOnPrev).toHaveBeenCalledTimes(1);
    });

    test('calls onNext when next button is clicked', () => {
        render(<Pagination page={2} totalPages={5} onPrev={mockOnPrev} onNext={mockOnNext} />);
        
        const nextButton = screen.getByRole('button', { name: /next/i });
        fireEvent.click(nextButton);
        expect(mockOnNext).toHaveBeenCalledTimes(1);
    });
});
