import React from "react";

function Error({ message, retry }) {
  return (
    <div className="p-4 text-center error">
      <p>Error: {message}</p>
      <button
        className="px-4 py-2 font-bold text-white bg-blue-500 rounded hover:bg-blue-700"
        onClick={retry}
      >
        Retry
      </button>
    </div>
  );
}

export default Error;
