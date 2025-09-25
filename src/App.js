import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Import CSS file

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data from backend (replace with actual Discord login logic)
    axios.get('http://localhost:5000/user') // Replace with your backend URL
      .then(response => {
        setUser(response.data);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }, []);

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="user-profile">
          {user && (
            <>
              <span className="username">{user.username}</span>
              <img src={user.profile_picture} alt="Profile" className="profile-picture" />
            </>
          )}
        </div>
      </header>
      <main className="app-main">
        <h1>Welcome to the Cool Text Page!</h1>
        <p>This is a placeholder for your awesome content.</p>
      </main>
    </div>
  );
}

export default App;