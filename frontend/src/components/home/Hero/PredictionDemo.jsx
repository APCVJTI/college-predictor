import "./PredictionDemo.scss";
import { FaUniversity, FaCheckCircle } from "react-icons/fa";

function PredictionDemo() {
  return (
    <div className="prediction-card">

      <div className="prediction-card__header">
        <span className="live-dot"></span>
        <p>Live Prediction</p>
      </div>

      <div className="prediction-card__percentage">
        95.63%
      </div>

      <div className="prediction-card__divider"></div>

      <div className="prediction-section">
        <h3>Dream Colleges</h3>

        <div className="college">
          <FaUniversity />
          <span>VJTI</span>
        </div>

        <div className="college">
          <FaUniversity />
          <span>COEP</span>
        </div>

        <div className="college">
          <FaUniversity />
          <span>PICT</span>
        </div>
      </div>

      <div className="prediction-card__divider"></div>

      <div className="prediction-section">
        <h3>Target Colleges</h3>

        <div className="college">
          <FaUniversity />
          <span>DJ Sanghvi</span>
        </div>

        <div className="college">
          <FaUniversity />
          <span>PCCOE</span>
        </div>
      </div>

      <div className="prediction-card__divider"></div>

      <div className="prediction-section">
        <h3>Safe Colleges</h3>

        <div className="college">
          <FaUniversity />
          <span>AISSMS</span>
        </div>

        <div className="college">
          <FaUniversity />
          <span>RCOEM</span>
        </div>
      </div>

      <div className="prediction-card__footer">
        <FaCheckCircle />
        <span>Updated just now</span>
      </div>

    </div>
  );
}

export default PredictionDemo;