import Navbar from '../components/Navbar.jsx';
import Hero from '../sections/Hero.jsx';
import Features from '../sections/Features.jsx';
import FAQs from '../sections/FAQs.jsx';
import Footer from '../components/Footer.jsx';

export default function Home() {
    return (
        <div className='mx-auto'>
            <Navbar />
            
            <Hero />
        
            <Features />
        
            <FAQs />
        
            <Footer />
        </div>
    )
}