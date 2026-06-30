import { useEffect, useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { HiOutlineMenuAlt3, HiOutlineX } from "react-icons/hi";

import Logo from "../../common/Logo/Logo";
import Button from "../../common/Button/Button";

import navLinks from "./navLinks";

import "./Navbar.scss";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  // Temporary authentication state
  // Later replace with JWT auth
  const isAuthenticated = false;

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 40);
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <header className={`navbar ${scrolled ? "navbar--scrolled" : ""}`}>
      <div className="container navbar__container">

        {/* Logo */}

        <Logo />

        {/* Desktop Navigation */}

        <nav className="navbar__links">

          {navLinks.map((link) => (
            <NavLink
              key={link.name}
              to={link.path}
              className="navbar__link"
            >
              {link.name}
            </NavLink>
          ))}

        </nav>

        {/* Right Side */}

        <div className="navbar__actions">

          {!isAuthenticated ? (
            <>
              <Link
                to="/login"
                className="navbar__login"
              >
                Login
              </Link>

              <Button>
                Start Prediction
              </Button>
            </>
          ) : (
            <>
              <Link
                to="/workspace"
                className="navbar__login"
              >
                Workspace
              </Link>

              <Button variant="secondary">
                Profile
              </Button>
            </>
          )}

        </div>

        {/* Mobile Button */}

        <button
          className="navbar__toggle"
          onClick={() => setMenuOpen(!menuOpen)}
        >
          {menuOpen ? (
            <HiOutlineX />
          ) : (
            <HiOutlineMenuAlt3 />
          )}
        </button>

      </div>

      {/* Mobile Menu */}

      {menuOpen && (

        <div className="navbar__mobile">

          {navLinks.map((link) => (

            <NavLink
              key={link.name}
              to={link.path}
              className="navbar__mobile-link"
              onClick={() => setMenuOpen(false)}
            >
              {link.name}
            </NavLink>

          ))}

          {!isAuthenticated ? (

            <>
              <Link
                to="/login"
                className="navbar__mobile-login"
              >
                Login
              </Link>

              <Button fullWidth>
                Start Prediction
              </Button>
            </>

          ) : (

            <>
              <Link
                to="/workspace"
                className="navbar__mobile-login"
              >
                Workspace
              </Link>

              <Button
                variant="secondary"
                fullWidth
              >
                Profile
              </Button>
            </>

          )}

        </div>

      )}

    </header>
  );
}

export default Navbar;