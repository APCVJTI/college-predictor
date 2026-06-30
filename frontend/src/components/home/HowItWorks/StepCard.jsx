import "./StepCard.scss";

function StepCard({ step }) {
  const Icon = step.icon;

  return (
    <div className="step-card">

      <div className="step-card__number">
        {step.id}
      </div>

      <div className="step-card__icon">
        <Icon />
      </div>

      <h3>
        {step.title}
      </h3>

      <p>
        {step.description}
      </p>

    </div>
  );
}

export default StepCard;