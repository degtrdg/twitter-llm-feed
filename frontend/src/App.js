import React from "react";
import "./App.css";
import TweetList from "./components/TweetList";

function App() {
  return (
    <div className="App">
      <header className="App-header bg-blue-500">
        <h1 className="text-white">Tweet Filter</h1>
      </header>
      <TweetList />
    </div>
  );
}

export default App;
