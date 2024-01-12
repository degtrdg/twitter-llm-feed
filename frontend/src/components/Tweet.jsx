import React from "react";

function Tweet({ data }) {
  return (
    <div className="p-4 border-b border-gray-200 tweet">
      <h3 className="font-bold">{data.author}</h3>
      <p>{data.content}</p>
    </div>
  );
}

export default Tweet;
