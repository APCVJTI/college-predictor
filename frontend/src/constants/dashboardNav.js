import {
  FaHome,
  FaChartLine,
  FaBalanceScale,
  FaHeart,
  FaUser,
  FaSignOutAlt,
} from "react-icons/fa";

const dashboardNav = [

  {
    id: 1,
    title: "Dashboard",
    path: "/dashboard",
    icon: FaHome,
  },

  {
    id: 2,
    title: "Predictor",
    path: "/predictor",
    icon: FaChartLine,
  },

  {
    id: 3,
    title: "Compare",
    path: "/compare",
    icon: FaBalanceScale,
  },

  {
    id: 4,
    title: "Favorites",
    path: "/favorites",
    icon: FaHeart,
  },

  {
    id: 5,
    title: "Profile",
    path: "/profile",
    icon: FaUser,
  },

  {
    id: 6,
    title: "Logout",
    path: "/logout",
    icon: FaSignOutAlt,
  },

];

export default dashboardNav;