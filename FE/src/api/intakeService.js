import axios from 'axios';

const API_URL = 'http://your-api-url.com/api/intake/'; // Replace with your actual API URL

export const submitSymptoms = async (symptomsData) => {
    try {
        const response = await axios.post(`${API_URL}submit/`, symptomsData);
        return response.data;
    } catch (error) {
        throw new Error('Error submitting symptoms: ' + error.message);
    }
};

export const fetchSymptoms = async (patientId) => {
    try {
        const response = await axios.get(`${API_URL}fetch/${patientId}/`);
        return response.data;
    } catch (error) {
        throw new Error('Error fetching symptoms: ' + error.message);
    }
};