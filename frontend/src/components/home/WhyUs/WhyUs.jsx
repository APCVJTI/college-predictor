import "./WhyUs.scss";
import whyUsData from "./whyUsData";

function WhyUs() {
  return (
    <section className="why-us">

      <div className="why-us__container">

        <div className="why-us__header">

          <span className="why-us__badge">
            Why Choose Us
          </span>

        <h2>
            Why Students Choose
            <br />
            <span>DSE College Predictor</span>
        </h2>

          <p>
            Built specifically for Maharashtra Diploma students,
            helping you make confident admission decisions using
            previous CAP cutoff trends.
          </p>

        </div>

        <div className="why-us__grid">

          {whyUsData.map((item, index) => {

            const Icon = item.icon;

            return (

              <div className="why-card" key={index}>

                <div className="why-card__icon">
                  <Icon />
                </div>

                <h3>{item.title}</h3>

                <p>{item.description}</p>

              </div>

            );

          })}

        </div>

      </div>

    </section>
  );
}

export default WhyUs;