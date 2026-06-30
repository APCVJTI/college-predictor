import {
  FaKeyboard,
  FaChartLine,
  FaUniversity,
  FaCheckCircle,
} from "react-icons/fa";

const stepsData = [
  {
    id: "01",
    icon: FaKeyboard,
    title: "Enter Percentage",
    description:
      "Enter your Diploma aggregate percentage to begin the prediction.",
  },
  {
    id: "02",
    icon: FaChartLine,
    title: "Analyze CAP Data",
    description:
      "Our system compares your percentage with previous Maharashtra DSE CAP cutoff trends.",
  },
  {
    id: "03",
    icon: FaUniversity,
    title: "Explore Colleges",
    description:
      "View Dream, Target and Safe colleges along with important admission insights.",
  },
  {
    id: "04",
    icon: FaCheckCircle,
    title: "Make Your Decision",
    description:
      "Compare colleges and confidently choose the best option for your future.",
  },
];

export default stepsData;