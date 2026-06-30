import "./HowItWorks.scss";

import stepsData from "./stepsData";
import StepCard from "./StepCard";

function HowItWorks() {
  return (
    <section className="how-it-works">

      <div className="how-it-works__container">

        <div className="how-it-works__header">

          <span className="how-it-works__badge">
            How It Works
          </span>

          <h2>
            From Percentage to
            <br />
            <span>Your Dream College</span>
          </h2>

          <p>
            Finding the right engineering college shouldn't be confusing.
            Follow these four simple steps to discover your best options.
          </p>

        </div>

        <div className="how-it-works__grid">

          {stepsData.map((step) => (
            <StepCard
              key={step.id}
              step={step}
            />
          ))}

        </div>

      </div>

    </section>
  );
}

export default HowItWorks;