import React, { useState, useEffect } from "react";
import Header from "./components/Header";
import TweetList from "./components/TweetList";
import axios from "axios";

const serverUrl = "http://127.0.0.1:5000";

function App() {
  const [currentView, setCurrentView] = useState("unfiltered");
  const [unfilteredTweets, setUnfilteredTweets] = useState([]);
  const [filteredTweets, setFilteredTweets] = useState([]);
  const [showReason, setShowReason] = useState(false);
  const [filterAnswer, setFilterAnswer] = useState("both"); // 'yes', 'no', 'both'

  useEffect(() => {
    // Fetch unfiltered tweets
    axios
      .get(`${serverUrl}/unanalyzed-tweets`)
      .then((response) => setUnfilteredTweets(response.data))
      .catch((error) =>
        console.error("Error fetching unfiltered tweets:", error)
      );

    // Fetch filtered tweets
    axios
      .get(`${serverUrl}/evaluate-tweets`)
      .then((response) => setFilteredTweets(response.data))
      .catch((error) =>
        console.error("Error fetching filtered tweets:", error)
      );
  }, []);

  const handleViewChange = (view) => {
    setCurrentView(view);
  };

  const handleFilterChange = (answer) => {
    setFilterAnswer(answer);
  };

  const toggleShowReason = () => {
    setShowReason(!showReason);
  };

  return (
    <div>
      <Header
        onSwitchView={handleViewChange}
        onFilterChange={handleFilterChange}
        onToggleShowReason={toggleShowReason}
        currentView={currentView}
        showReason={showReason}
      />
      <TweetList
        tweets={
          currentView === "unfiltered" ? unfilteredTweets : filteredTweets
        }
        currentView={currentView}
        showReason={showReason}
        filterAnswer={filterAnswer}
      />
    </div>
  );
}

export default App;
