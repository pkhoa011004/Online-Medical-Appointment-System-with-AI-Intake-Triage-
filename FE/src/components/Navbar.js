import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Optional: Import a CSS file for styling

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <Link to="/">Healthcare System</Link>
            </div>
            <ul className="navbar-links">
                <li>
                    <Link to="/login">Login</Link>
                </li>
                <li>
                    <Link to="/register">Register</Link>
                </li>
                <li>
                    <Link to="/patient-dashboard">Patient Dashboard</Link>
                </li>
                <li>
                    <Link to="/doctor-dashboard">Doctor Dashboard</Link>
                </li>
                <li>
                    <Link to="/clinic-staff-dashboard">Clinic Staff Dashboard</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;