import React from "react";

function Tweet({ data }) {
  return (
    <div className="tweet">
      <h3>{data.author}</h3>
      <p>{data.content}</p>
    </div>
  );
}

export default Tweet;
