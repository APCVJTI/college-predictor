import { NavLink } from "react-router-dom";

import dashboardNav from "../../../constants/dashboardNav";

import Logo from "../../common/Logo/Logo";

import "./Sidebar.scss";

function Sidebar() {

  return (

    <aside className="sidebar">

      {/* ==========================
          Logo
      ========================== */}

      <div className="sidebar__logo">

        <Logo />

      </div>

      {/* ==========================
          Navigation
      ========================== */}

      <nav className="sidebar__nav">

        {

          dashboardNav.map((item) => {

            const Icon = item.icon;

            return (

              <NavLink
                key={item.id}
                to={item.path}
                className={({ isActive }) =>
                  isActive
                    ? "sidebar__link active"
                    : "sidebar__link"
                }
              >

                <Icon className="sidebar__icon" />

                <span>

                  {item.title}

                </span>

              </NavLink>

            );

          })

        }

      </nav>

    </aside>

  );

}

export default Sidebar;