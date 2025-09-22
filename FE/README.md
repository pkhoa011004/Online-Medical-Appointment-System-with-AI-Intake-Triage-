# Healthcare Frontend

This project is a ReactJS application for managing healthcare-related functionalities. It includes various components and pages for user authentication, patient and doctor dashboards, and more.

## Project Structure

```
healthcare-frontend
├── public
│   ├── index.html            # Main HTML file for the React application
│   └── favicon.ico           # Favicon for the application
├── src
│   ├── index.js              # Entry point of the React application
│   ├── App.js                # Main App component
│   ├── components            # Reusable components
│   │   ├── Navbar.js         # Navigation bar component
│   │   ├── Footer.js         # Footer component
│   │   └── FormInput.js      # Input field component
│   ├── pages                 # Application pages
│   │   ├── Login.js          # User login page
│   │   ├── Register.js       # User registration page
│   │   ├── PatientDashboard.js# Patient dashboard page
│   │   ├── DoctorDashboard.js # Doctor dashboard page
│   │   └── ClinicStaffDashboard.js # Clinic staff dashboard page
│   ├── api                   # API service functions
│   │   ├── authService.js    # Authentication-related API calls
│   │   ├── appointmentService.js # Appointment-related API calls
│   │   └── intakeService.js   # AI intake-related API calls
│   ├── hooks                 # Custom hooks
│   │   └── index.js          # Custom hooks implementation
│   ├── context               # Context API for global state management
│   │   └── index.js          # Context providers and consumers
│   └── styles                # CSS styles
│       └── index.css         # Main CSS file for the application
├── package.json              # npm configuration file
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd healthcare-frontend
   ```

3. Install the required packages:
   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

## Features

- User authentication (login and registration)
- Patient and doctor dashboards
- Appointment management
- AI intake for patient data collection

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.