import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Login from './pages/Login';
import Register from './pages/Register';
import PatientDashboard from './pages/PatientDashboard';
import DoctorDashboard from './pages/DoctorDashboard';
import ClinicStaffDashboard from './pages/ClinicStaffDashboard';
import './styles/index.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Switch>
                    <Route path="/" exact component={Login} />
                    <Route path="/register" component={Register} />
                    <Route path="/patient-dashboard" component={PatientDashboard} />
                    <Route path="/doctor-dashboard" component={DoctorDashboard} />
                    <Route path="/clinic-staff-dashboard" component={ClinicStaffDashboard} />
                </Switch>
                <Footer />
            </div>
        </Router>
    );
}

export default App;