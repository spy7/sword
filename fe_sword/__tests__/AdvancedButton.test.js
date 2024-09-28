import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import AdvancedButton from '../src/components/AdvancedButton';

describe('AdvancedButton Component', () => {
  const mockToggleAdvancedSearch = jest.fn();

  test('renders button with "Advanced" label when advanced is false', () => {
    render(<AdvancedButton advanced={false} toggleAdvancedSearch={mockToggleAdvancedSearch} />);

    const button = screen.getByRole('button', { name: /advanced/i });
    expect(button).toBeInTheDocument();
    expect(button).toHaveTextContent('Advanced');
  });

  test('renders button with "Basic" label when advanced is true', () => {
    render(<AdvancedButton advanced={true} toggleAdvancedSearch={mockToggleAdvancedSearch} />);

    const button = screen.getByRole('button', { name: /basic/i });
    expect(button).toBeInTheDocument();
    expect(button).toHaveTextContent('Basic');
  });

  test('calls toggleAdvancedSearch function when clicked', () => {
    render(<AdvancedButton advanced={false} toggleAdvancedSearch={mockToggleAdvancedSearch} />);

    const button = screen.getByRole('button', { name: /advanced/i });
    fireEvent.click(button);

    expect(mockToggleAdvancedSearch).toHaveBeenCalledTimes(1);
  });

  test('applies "active" class when advanced is true', () => {
    render(<AdvancedButton advanced={true} toggleAdvancedSearch={mockToggleAdvancedSearch} />);

    const button = screen.getByRole('button', { name: /basic/i });
    expect(button).toHaveClass('active');
  });

  test('does not apply "active" class when advanced is false', () => {
    render(<AdvancedButton advanced={false} toggleAdvancedSearch={mockToggleAdvancedSearch} />);

    const button = screen.getByRole('button', { name: /advanced/i });
    expect(button).not.toHaveClass('active');
  });
});
