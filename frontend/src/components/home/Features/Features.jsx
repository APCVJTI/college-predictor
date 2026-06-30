import { useState } from "react";

import "./Features.scss";

import featuresData from "./featuresData";
import FeatureTabs from "./FeatureTabs";
import FeaturePreview from "./FeaturePreview";

function Features() {
  const [activeFeature, setActiveFeature] = useState(featuresData[0]);

  return (
    <section className="features">

      <div className="features__container">

        <div className="features__left">

          <FeatureTabs
            features={featuresData}
            activeFeature={activeFeature}
            setActiveFeature={setActiveFeature}
          />

        </div>

        <div className="features__right">

          <FeaturePreview
            activeFeature={activeFeature}
          />

        </div>

      </div>

    </section>
  );
}

export default Features;