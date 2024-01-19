import React from "react";
import { Tweet } from "react-tweet";

function FilteredTweet({ tweet, showReason, answer }) {
  return (
    <div className="flex items-start justify-center my-8 space-x-4">
      <div className="flex-initial max-w-md">
        <Tweet id={tweet.Link.match(/\/(\d+)/)[1]} />
      </div>
      {showReason && (
        <div
          className={`flex-initial max-w-md p-4 border-2 rounded shadow-lg ${
            answer === "yes" ? "border-green-200" : "border-red-900"
          }`}
          style={{ margin: "1.6rem" }}
        >
          <p className="text-sm font-medium">Reason:</p>
          <p>{tweet.Reasoning}</p>
        </div>
      )}
    </div>
  );
}

export default FilteredTweet;
