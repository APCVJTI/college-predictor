import {
  FaArrowUp,
} from "react-icons/fa";

import Logo from "../../common/Logo/Logo";
import FooterColumn from "./FooterColumn";
import footerData from "./footerData";

import "./Footer.scss";

function Footer() {

  const scrollToTop = () => {

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });

  };

  return (

    <footer className="footer">

      <div className="footer__container">

        {/* ===========================
            Left
        =========================== */}

        <div className="footer__brand">

          <Logo />

          <p className="footer__description">

            Helping Maharashtra Diploma students make smarter
            engineering admission decisions using previous
            CAP cutoff analysis.

          </p>

          <div className="footer__socials">

            {footerData.socials.map((social, index) => {

              const Icon = social.icon;

              return (

                <a
                  key={index}
                  href={social.link}
                  className="footer__social"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={`Social Link ${index + 1}`}
                >

                  <Icon />

                </a>

              );

            })}

          </div>

        </div>

        {/* ===========================
            Right
        =========================== */}

        <div className="footer__links">

          <FooterColumn
            title="Quick Links"
            items={footerData.quickLinks}
          />

          <FooterColumn
            title="Features"
            items={footerData.features}
          />

          <FooterColumn
            title="Contact"
            items={footerData.contact}
          />

        </div>

      </div>

      {/* ===========================
          Bottom
      =========================== */}

      <div className="footer__bottom">

        <div className="footer__credit">

          <p className="footer__copyright">

            © {new Date().getFullYear()} DSE College Predictor •
            All Rights Reserved.

          </p>

          <p className="footer__developer">

            Crafted with ❤️ by{" "}

            <a
              href="https://www.linkedin.com/in/achyut-chaudhari-8b5880356/"
              target="_blank"
              rel="noopener noreferrer"
              className="footer__developer-link"
            >

              Achyut Chaudhari

            </a>

          </p>

        </div>

        <button
          className="footer__top"
          onClick={scrollToTop}
          aria-label="Scroll to top"
        >

          <FaArrowUp />

        </button>

      </div>

    </footer>

  );

}

export default Footer;