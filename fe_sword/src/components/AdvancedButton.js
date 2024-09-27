import React from 'react';
import './AdvancedButton.css';

const AdvancedButton = ({ advanced, toggleAdvancedSearch }) => {
  return (
    <div className="search-toggle">
        <button className={`toggle-button ${advanced ? 'active' : ''}`} onClick={toggleAdvancedSearch}>
            {advanced ? "Basic" : "Advanced"}
        </button>
    </div>
  );
};

export default AdvancedButton;
