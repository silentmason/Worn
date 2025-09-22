import React from 'react';
import Register from './components/Register';
import Login from './components/Login';
import PostForm from './components/PostForm';
import PostList from './components/PostList';

function App() {
  return (
    <div className="App">
      <h1>Social Media App</h1>
      <Register />
      <Login />
      <PostForm />
      <PostList />
    </div>
  );
}

export default App;