import React from "react";

function Header({
  onSwitchView,
  onFilterChange,
  onToggleShowReason,
  currentView,
  showReason,
}) {
  return (
    <div>
      <button onClick={() => onSwitchView("unfiltered")}>
        Unfiltered View
      </button>
      <button onClick={() => onSwitchView("filtered")}>Filtered View</button>

      {currentView === "filtered" && (
        <>
          <button onClick={() => onFilterChange("yes")}>Filter Yes</button>
          <button onClick={() => onFilterChange("no")}>Filter No</button>
          <button onClick={() => onFilterChange("both")}>Show Both</button>
          <button onClick={onToggleShowReason}>
            {showReason ? "Hide Reasons" : "Show Reasons"}
          </button>
        </>
      )}
    </div>
  );
}

export default Header;
