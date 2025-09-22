import React, { useState } from 'react';

function PostForm() {
  const [text, setText] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Implement post creation logic here (e.g., API call)
    console.log('Creating post', text);
    setText(''); // Clear the input after submitting
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Post</h2>
      <label>
        Text:
        <textarea value={text} onChange={(e) => setText(e.target.value)} />
      </label>
      <br />
      <button type="submit">Post</button>
    </form>
  );
}

export default PostForm;