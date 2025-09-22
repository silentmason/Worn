import React from 'react';

function PostList() {
  // Implement logic to fetch and display posts here (e.g., API call)
  const posts = [
    { id: 1, username: 'user1', text: 'This is the first post.' },
    { id: 2, username: 'user2', text: 'This is another post.' },
  ];

  return (
    <div>
      <h2>Posts</h2>
      {posts.map((post) => (
        <div key={post.id}>
          <strong>{post.username}:</strong> {post.text}
        </div>
      ))}
    </div>
  );
}

export default PostList;