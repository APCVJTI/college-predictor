import { Routes, Route } from "react-router-dom";

import Navbar from "../components/layouts/Navbar/Navbar";
import Hero from "../components/home/Hero/Hero";
import WhyUs from "../components/home/WhyUs/WhyUs";
import Features from "../components/home/Features/Features";
import HowItWorks from "../components/home/HowItWorks/HowItWorks";
import FAQ from "../components/home/FAQ/FAQ";
import Footer from "../components/layouts/Footer/Footer";

import DashboardLayout from "../layouts/DashboardLayout/DashboardLayout";

// Pages
import Dashboard from "../pages/Dashboard/Dashboard";
import Predictor from "../pages/Predictor/Predictor";
import Compare from "../pages/Compare/Compare";
import Favorites from "../pages/Favorites/Favorites";
import Profile from "../pages/Profile/Profile";
import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";

function Home() {

  return (

    <>

      <Navbar />

      <Hero />

      <WhyUs />

      <Features />

      <HowItWorks />

      <FAQ />

      <Footer />

    </>

  );

}

function AppRoutes() {

  return (

    <Routes>

      {/* ==========================
          Public Routes
      ========================== */}

      <Route
        path="/"
        element={<Home />}
      />

      <Route
        path="/login"
        element={<Login />}
      />

      <Route
        path="/register"
        element={<Register />}
      />

      {/* ==========================
          Dashboard Layout
      ========================== */}

      <Route element={<DashboardLayout />}>

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/predictor"
          element={<Predictor />}
        />

        <Route
          path="/compare"
          element={<Compare />}
        />

        <Route
          path="/favorites"
          element={<Favorites />}
        />

        <Route
          path="/profile"
          element={<Profile />}
        />

      </Route>

      {/* ==========================
          404
      ========================== */}

      <Route
        path="*"
        element={<h1>404 Page Not Found</h1>}
      />

    </Routes>

  );

}

export default AppRoutes;