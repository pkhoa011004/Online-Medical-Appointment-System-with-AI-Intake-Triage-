import axios from 'axios';

const API_URL = 'http://localhost:8000/api/appointments/';

export const createAppointment = async (appointmentData) => {
    try {
        const response = await axios.post(API_URL, appointmentData);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const fetchAppointments = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const fetchAppointmentById = async (id) => {
    try {
        const response = await axios.get(`${API_URL}${id}/`);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const updateAppointment = async (id, appointmentData) => {
    try {
        const response = await axios.put(`${API_URL}${id}/`, appointmentData);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const deleteAppointment = async (id) => {
    try {
        await axios.delete(`${API_URL}${id}/`);
    } catch (error) {
        throw error.response.data;
    }
};