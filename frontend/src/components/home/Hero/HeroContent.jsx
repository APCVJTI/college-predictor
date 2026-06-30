import "./HeroContent.scss";

import { FaArrowRight, FaCheckCircle } from "react-icons/fa";

import Button from "../../common/Button/Button";

function HeroContent() {
  return (
    <div className="hero-content">
      <span className="hero-content__badge">
        Maharashtra DSE Admissions
      </span>

    <h1 className="hero-content__title">
        Your Diploma.
        <br />

        <span className="hero-content__highlight">
            Your Future.
        </span>

        <br />

        One Smart Decision.
    </h1>

      <p className="hero-content__description">
            Predict your Dream, Target and Safe engineering colleges using previous Maharashtra DSE CAP cutoff analysis.
            Built exclusively for Diploma students.
      </p>

      <div className="hero-content__features">

        <div className="feature">
          <FaCheckCircle />
          <span>Previous CAP Cutoff Analysis</span>
        </div>

        <div className="feature">
          <FaCheckCircle />
          <span>Dream • Target • Safe Prediction</span>
        </div>

        <div className="feature">
          <FaCheckCircle />
          <span>Instant Results</span>
        </div>

      </div>

      <div className="hero-content__buttons">

        <Button size="lg">
          Start Prediction
          <FaArrowRight />
        </Button>

        <Button
          variant="secondary"
          size="lg"
        >
          Explore Colleges
        </Button>

      </div>

      <div className="hero-content__stats">

        <div className="stat">

          <h2>300+</h2>

          <p>Engineering Colleges</p>

        </div>

        <div className="stat">

          <h2>CAP</h2>

          <p>Cutoff Analysis</p>

        </div>

        <div className="stat">

          <h2>Dream</h2>

          <p>Target • Safe</p>

        </div>

      </div>

    </div>
  );
}

export default HeroContent;