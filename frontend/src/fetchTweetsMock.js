export function fetchTweetsMock() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Randomly resolve or reject to simulate success/failure
      if (Math.random() > 0.5) {
        resolve([
          { id: 1, author: "User1", content: "Mock tweet #1" },
          { id: 2, author: "User2", content: "Mock tweet #2" },
          // Add more mock tweets as needed
        ]);
      } else {
        reject(new Error("Failed to fetch tweets"));
      }
    }, 1000); // Simulate network delay
  });
}
