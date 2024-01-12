const fakeTweets = [
  { id: 1, author: "User1", content: "This is a fake tweet #1" },
  { id: 2, author: "User2", content: "This is a fake tweet #2" },
  {
    id: 3,
    author: "User3",
    content: "Just had a great meal at a new restaurant!",
  },
  { id: 4, author: "User4", content: "Excited to start my new job tomorrow!" },
  { id: 5, author: "User5", content: "Watching my favorite TV show tonight!" },
  {
    id: 6,
    author: "User6",
    content: "Feeling grateful for all the love and support!",
  },
];
export function fetchTweetsMock() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(fakeTweets); // Always resolve with the full list of fake tweets
    }, 1000);
  });
}
