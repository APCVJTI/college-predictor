import Navbar from "./components/layouts/Navbar/Navbar";
import Hero from "./components/home/Hero/Hero";
import WhyUs from "./components/home/WhyUs/WhyUs";
import Features from "./components/home/Features/Features";
import HowItWorks from "./components/home/HowItWorks/HowItWorks";
import FAQ from "./components/home/FAQ/FAQ";
import Footer from "./components/layouts/Footer/Footer";

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <WhyUs />
      <Features />
      <HowItWorks />
      <FAQ />
      <Footer />
    </>
  );
}

export default App;