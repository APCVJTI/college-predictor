import "./FeaturePreview.scss";

import Button from "../../common/Button/Button";

function FeaturePreview({ activeFeature }) {
  return (
    <div className="feature-preview">

      <div className="feature-preview__window">

        <div className="feature-preview__topbar">

          <div className="dots">
            <span></span>
            <span></span>
            <span></span>
          </div>

          <p>DSE College Predictor</p>

        </div>

        <div className="feature-preview__content">

          <span className="preview-tag">
            {activeFeature.subtitle}
          </span>

          <h2>
            {activeFeature.title}
          </h2>

          <p>
            {activeFeature.description}
          </p>

          <div className="preview-info">

            <div className="preview-box">

              <h4>{activeFeature.stats}</h4>

              <span>Powered by Previous CAP Analysis</span>

            </div>

            <div className="preview-box">

              <h4>Instant</h4>

              <span>Result Generation</span>

            </div>

          </div>

          <Button>
            {activeFeature.button}
          </Button>

        </div>

      </div>

    </div>
  );
}

export default FeaturePreview;