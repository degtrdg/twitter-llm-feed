import React, { useState, useEffect } from "react";
import Error from "./Error";
import { fetchTweetsMock } from "../fetchTweetsMock";
import Tweet from "./Tweet";
import Loader from "./Loader";
import axios from "axios";

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

// function TweetList() {
//   const [tweets, setTweets] = useState([]);
//   const [loading, setLoading] = useState(true);
//   //   const [tweets, setTweets] = useState(fakeTweets);
//   //   const [loading, setLoading] = useState(false); // Set to false since we're using fake data

//   useEffect(() => {
//     axios
//       .get("/get-tweets")
//       .then((response) => {
//         setTweets(response.data);
//         setLoading(false);
//       })
//       .catch((error) => console.error("Error fetching tweets:", error));
//   }, []);

//   if (loading) return <Loader />;

//   return (
//     <div className="tweet-list">
//       {console.log(tweets)}
//       {tweets.map((tweet) => (
//         <Tweet key={tweet.id} data={tweet} />
//       ))}
//     </div>
//   );
// }

function TweetList() {
  // const [tweets, setTweets] = useState([]);
  const [tweets, setTweets] = useState(fakeTweets);
  // const [loading, setLoading] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Rest of the code...

  useEffect(() => {
    fetchTweetsMock()
      .then((data) => {
        setTweets(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <Loader />;
  if (error)
    return <Error message={error} retry={() => window.location.reload()} />;

  return (
    <div className="tweet-list">
      {tweets.length > 0
        ? tweets.map((tweet) => <Tweet key={tweet.id} data={tweet} />)
        : "No tweets to display"}
    </div>
  );
}

export default TweetList;
