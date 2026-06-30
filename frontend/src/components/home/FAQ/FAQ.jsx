import { useState } from "react";

import "./FAQ.scss";

import faqData from "./faqData";
import FAQItem from "./FAQItem";

function FAQ() {

  const [openId, setOpenId] = useState(1);

  const handleToggle = (id) => {

    setOpenId(openId === id ? null : id);

  };

  return (

    <section className="faq">

      <div className="faq__container">

        {/* Header */}

        <div className="faq__header">

          <span className="faq__badge">
            Frequently Asked Questions
          </span>

          <h2>

            Everything You
            <br />

            <span>Need to Know</span>

          </h2>

          <p>

            Find answers to the most common questions about our
            Maharashtra Diploma College Predictor.

          </p>

        </div>

        {/* FAQ List */}

        <div className="faq__list">

          {faqData.map((faq) => (

            <FAQItem
              key={faq.id}
              faq={faq}
              isOpen={openId === faq.id}
              onClick={() => handleToggle(faq.id)}
            />

          ))}

        </div>

        {/* Bottom CTA */}

        <div className="faq__cta">

          <h3>
            Still have questions?
          </h3>

          <p>

            We're here to help you make the right admission decision.

          </p>

          <button className="faq__button">

            Contact Us

          </button>

        </div>

      </div>

    </section>

  );

}

export default FAQ;