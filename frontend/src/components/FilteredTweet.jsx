import React from "react";
import { Tweet } from "react-tweet";

function FilteredTweet({ tweet, showReason }) {
  return (
    <div>
      <Tweet id={tweet.Link.match(/\/(\d+)/)[1]} />
      {showReason && <div>Reason: {tweet.Reasoning}</div>}
    </div>
  );
}

export default FilteredTweet;
