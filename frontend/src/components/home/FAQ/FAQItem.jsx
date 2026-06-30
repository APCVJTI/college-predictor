import { FaPlus, FaMinus } from "react-icons/fa";
import "./FAQItem.scss";

function FAQItem({ faq, isOpen, onClick }) {
  return (
    <div className={`faq-item ${isOpen ? "active" : ""}`}>

      <button
        className="faq-item__header"
        onClick={onClick}
      >
        <h3>{faq.question}</h3>

        <span className="faq-item__icon">
          {isOpen ? <FaMinus /> : <FaPlus />}
        </span>
      </button>

      <div className={`faq-item__content ${isOpen ? "show" : ""}`}>
        <p>{faq.answer}</p>
      </div>

    </div>
  );
}

export default FAQItem;