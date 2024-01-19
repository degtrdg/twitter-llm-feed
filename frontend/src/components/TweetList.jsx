import React from "react";
import { Tweet } from "react-tweet";
import FilteredTweet from "./FilteredTweet";

function TweetList({ tweets, currentView, showReason, filterAnswer }) {
  return (
    <div>
      {currentView === "unfiltered"
        ? tweets.map((tweet, index) => (
            <Tweet key={index} id={tweet["Link"].match(/\/(\d+)/)[1]} />
          ))
        : tweets
            .filter(
              (tweet) =>
                filterAnswer === "both" ||
                tweet.Answer.toLowerCase() === filterAnswer
            )
            .map((tweet, index) => (
              <FilteredTweet
                key={index}
                tweet={tweet}
                showReason={showReason}
                answer={tweet.Answer.toLowerCase()}
              />
            ))}
    </div>
  );
}

export default TweetList;
