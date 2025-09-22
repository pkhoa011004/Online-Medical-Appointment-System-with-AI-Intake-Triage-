import axios from 'axios';

const API_URL = 'http://localhost:8000/api/auth/'; // Update with your API URL

// Register user
const register = async (userData) => {
    const response = await axios.post(`${API_URL}register/`, userData);
    return response.data;
};

// Login user
const login = async (userData) => {
    const response = await axios.post(`${API_URL}login/`, userData);
    return response.data;
};

// Logout user
const logout = () => {
    localStorage.removeItem('user');
};

// Get current user
const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem('user'));
};

export default {
    register,
    login,
    logout,
    getCurrentUser,
};