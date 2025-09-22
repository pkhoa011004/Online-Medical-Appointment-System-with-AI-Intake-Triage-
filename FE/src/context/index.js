import React, { createContext, useContext, useState } from 'react';

// Create a Context for the global state
const AppContext = createContext();

// Create a provider component
export const AppProvider = ({ children }) => {
    const [authState, setAuthState] = useState(null); // Example state for authentication

    return (
        <AppContext.Provider value={{ authState, setAuthState }}>
            {children}
        </AppContext.Provider>
    );
};

// Custom hook to use the AppContext
export const useAppContext = () => {
    return useContext(AppContext);
};