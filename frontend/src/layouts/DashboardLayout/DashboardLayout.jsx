import { Outlet } from "react-router-dom";

import Sidebar from "../../components/dashboard/Sidebar/Sidebar";
import Topbar from "../../components/dashboard/Topbar/Topbar";

import "./DashboardLayout.scss";

function DashboardLayout() {

  return (

    <div className="dashboard-layout">

      {/* ==========================================
          Sidebar
      ========================================== */}

      <Sidebar />

      {/* ==========================================
          Main Section
      ========================================== */}

      <div className="dashboard-layout__main">

        {/* Top Navigation */}

        <Topbar />

        {/* Dynamic Page Content */}

        <main className="dashboard-layout__content">

          <Outlet />

        </main>

      </div>

    </div>

  );

}

export default DashboardLayout;