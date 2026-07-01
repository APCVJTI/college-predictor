import {
  FaBell,
  FaSearch,
  FaChevronDown,
} from "react-icons/fa";

import "./Topbar.scss";

function Topbar() {

  // Temporary user object
  // Later this will come from AuthContext/API

  const user = {
    name: "Achyut Chaudhari",
    role: "Student",
    initials: "AC",
  };

  return (

    <header className="topbar">

      {/* ==========================================
          Search
      ========================================== */}

      <div className="topbar__search">

        <FaSearch className="topbar__search-icon" />

        <input
          type="text"
          placeholder="Search colleges..."
          aria-label="Search colleges"
        />

      </div>

      {/* ==========================================
          Right Section
      ========================================== */}

      <div className="topbar__actions">

        {/* Notifications */}

        <button
          className="topbar__notification"
          aria-label="Notifications"
        >

          <FaBell />

          <span className="topbar__badge"></span>

        </button>

        {/* User Profile */}

        <button
          className="topbar__profile"
          aria-label="User profile"
        >

          <div className="topbar__avatar">

            {user.initials}

          </div>

          <div className="topbar__user">

            <h4>

              {user.name}

            </h4>

            <p>

              {user.role}

            </p>

          </div>

          <FaChevronDown />

        </button>

      </div>

    </header>

  );

}

export default Topbar;