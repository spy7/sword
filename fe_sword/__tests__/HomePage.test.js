import { act, fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import api from '../src/api';
import HomePage from '../src/pages/HomePage';
import { mockApiBooks } from '../src/setupMocks';

jest.mock('../src/api');

describe('HomePage Component', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    test('should fetch and display books', async () => {
        mockApiBooks();

        await act(async () => {
            render(
                <MemoryRouter>
                    <HomePage />
                </MemoryRouter>
            );
        });

        await waitFor(() => {
            expect(screen.getByText('Book One')).toBeInTheDocument();
            expect(screen.getByText('Mock book')).toBeInTheDocument();
        });
    });

    test('should navigate to the next page', async () => {
        mockApiBooks();

        await act(async () => {
            render(
                <MemoryRouter>
                    <HomePage />
                </MemoryRouter>
            );
        });

        await waitFor(() => {
            expect(screen.getByText('Book One')).toBeInTheDocument();
        });

        const nextButton = screen.getAllByText('Next')[0];

        await act(() => {
            fireEvent.click(nextButton);
        });

        expect(api.get).toHaveBeenCalledWith('/v1/books/?limit=30&offset=30&search=');
    });

    test('should navigate to the previous page', async () => {
        mockApiBooks();

        render(
            <MemoryRouter>
                <HomePage />
            </MemoryRouter>
        );

        await waitFor(() => {
            expect(screen.getByText('Book One')).toBeInTheDocument();
        });

        const prevButton = screen.getAllByText('Previous')[0];
        const nextButton = screen.getAllByText('Next')[0];

        expect(prevButton).toBeDisabled();

        await act(() => {
            fireEvent.click(nextButton);
        });

        expect(prevButton).toBeEnabled();

        await act(() => {
            fireEvent.click(prevButton);
        });

        expect(api.get).toHaveBeenCalledWith('/v1/books/?limit=30&offset=0&search=');
    });

    test('should toggle the advanced search', async () => {
        mockApiBooks();

        await act(() => {
            render(
                <MemoryRouter>
                    <HomePage />
                </MemoryRouter>
            );
        });

        const toggleButton = screen.getByText('Advanced');

        await act(() => {
            fireEvent.click(toggleButton);
        });

        expect(screen.getByPlaceholderText('Title')).toBeInTheDocument();
    });
});
