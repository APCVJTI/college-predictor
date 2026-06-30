import "./FooterColumn.scss";

function FooterColumn({ title, items }) {
  return (
    <div className="footer-column">

      <h3 className="footer-column__title">
        {title}
      </h3>

      <ul className="footer-column__list">

        {items.map((item, index) => (

          <li
            key={index}
            className="footer-column__item"
          >
            {item}
          </li>

        ))}

      </ul>

    </div>
  );
}

export default FooterColumn;