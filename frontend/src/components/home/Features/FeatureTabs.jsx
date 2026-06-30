import "./FeatureTabs.scss";

function FeatureTabs({ features, activeFeature, setActiveFeature }) {
  return (
    <div className="feature-tabs">

      <div className="feature-tabs__header">

        <span>Explore Features</span>

        <h3>
          Everything you need for
          <br />
          smarter college decisions.
        </h3>

      </div>

      <div className="feature-tabs__list">

        {features.map((feature) => (

          <button
            key={feature.id}
            className={`feature-tab ${
              activeFeature.id === feature.id ? "active" : ""
            }`}
            onClick={() => setActiveFeature(feature)}
          >

            <div className="feature-tab__number">

              {String(feature.id).padStart(2, "0")}

            </div>

            <div className="feature-tab__content">

              <h4>{feature.title}</h4>

              <p>{feature.subtitle}</p>

            </div>

          </button>

        ))}

      </div>

    </div>
  );
}

export default FeatureTabs;