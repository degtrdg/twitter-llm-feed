import React from "react";

const viewButtons = ["unfiltered", "filtered"]
const filterButtons = ["yes", "no", "both"]
const buttonStyle = "hover:bg-slate-600 text-slate-100 rounded-md px-2 py-1";

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function Header({
  onSwitchView,
  onFilterChange,
  onToggleShowReason,
  currentView,
  showReason,
}) {
  return (
    <div className="flex flex-col my-6">
      <div className="flex gap-2 mx-auto">
        {
          viewButtons.map((buttonName) => (
            <button
              className={buttonStyle}
              onClick={() => onSwitchView(buttonName)}
            >
              {capitalize(buttonName)} View
            </button>
          ))
        }
      </div>

      <div className="flex gap-2 mx-auto">
        {currentView === "filtered" && (
          <>
            {
              filterButtons.map((buttonName) => (
                <button
                  className={buttonStyle}
                  onClick={() => onFilterChange(buttonName)}
                >
                  Filter {capitalize(buttonName)}
                </button>
              ))
            }
            <button className={buttonStyle} onClick={onToggleShowReason}>
              {showReason ? "Hide Reasons" : "Show Reasons"}
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default Header;
