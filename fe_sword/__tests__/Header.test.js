import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Header from '../src/components/Header';

describe('Header Component', () => {
    test('renders the header with titlee', () => {
        render(
            <MemoryRouter>
                <Header />
            </MemoryRouter>
        );

        expect(screen.getByText(/sword/i)).toBeInTheDocument();
        expect(screen.getByText(/frontend/i)).toBeInTheDocument();
        expect(screen.getByText(/Book/i)).toBeInTheDocument();
        expect(screen.getByText(/Book/i)).toHaveAttribute('href', '/');
    });
});
