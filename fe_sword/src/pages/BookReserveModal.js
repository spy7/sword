import React, { useEffect, useRef, useState } from 'react';
import './BookReserveModal.css';

const BookReserveModal = ({ isOpen, onClose, onReserve }) => {
    const [formData, setFormData] = useState({
        customer_name: '',
        customer_email: '',
    });

    const modalRef = useRef(null);
    const customerNameRef = useRef(null);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleReserve = (e) => {
        e.preventDefault();
        onReserve(formData);
        handleClose();
    };

    const handleClose = () => {
        setFormData({ customer_name: '', customer_email: '' });
        onClose();
    }

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (modalRef.current && !modalRef.current.contains(event.target)) {
                handleClose();
            }
        };

        if (isOpen) {
            document.addEventListener('mousedown', handleClickOutside);
            customerNameRef.current.focus();
        } else {
            document.removeEventListener('mousedown', handleClickOutside);
        }

        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, [isOpen, onClose]);

    if (!isOpen) return null;

    return (
        <div className="modal">
            <div className="modal-content" ref={modalRef}>
                <div className="modal-header">
                    <h2 className="modal-title">Reserve Book</h2>
                    <button className="close-button" onClick={handleClose}>&times;</button>
                </div>
                <div className="modal-body">
                    <form onSubmit={handleReserve}>
                        <div>
                            <input
                                type="text"
                                name="customer_name"
                                placeholder="Your name"
                                className="input-field"
                                value={formData.customer_name}
                                onChange={handleInputChange}
                                ref={customerNameRef}
                                required
                            />
                        </div>
                        <div>
                            <input
                                type="email"
                                name="customer_email"
                                placeholder="Your e-mail"
                                className="input-field"
                                value={formData.customer_email}
                                onChange={handleInputChange}
                                required
                            />
                        </div>
                        <button type="submit" className='submit-button'>Reserve</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default BookReserveModal;
