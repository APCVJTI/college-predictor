import "./Logo.scss";
import { Link } from "react-router-dom";

function Logo() {
  return (
    <Link to="/" className="logo">
      <div className="logo__icon">
        DSE
      </div>

      <div className="logo__content">
        <h1 className="logo__title">
          College Predictor
        </h1>

        <p className="logo__subtitle">
          Maharashtra DSE Admissions
        </p>
      </div>
    </Link>
  );
}

export default Logo;