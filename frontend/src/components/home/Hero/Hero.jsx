import "./Hero.scss";

import HeroContent from "./HeroContent";
import PredictionDemo from "./PredictionDemo";

function Hero() {
  return (
    <section className="hero">
      <div className="hero__container">
        <HeroContent />

        <PredictionDemo />
      </div>
    </section>
  );
}

export default Hero;