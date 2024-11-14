import { Link } from 'react-router-dom';
import { IconContext } from "react-icons/lib";
import { BiSolidError } from "react-icons/bi";
import Navbar from "../components/Navbar.jsx";
import Footer from "../components/Footer.jsx";

export default function Error() {
    return (
        <div className='flex flex-col gap-5'>
            <Navbar />

            {/* Error Message */}
            <div className='flex flex-col lg:flex-row justify-center items-center'>
                <IconContext.Provider value={{ size: '300px', color: '#b91c1c', className: '' }}>
                    <BiSolidError />
                </IconContext.Provider>
                <div className='text-justify flex flex-col w-full lg:w-1/2 gap-4 justify-center items-center px-5 lg:px-0'>
                    <h1 className='text-3xl text-red-700 font-poppins font-bold'>Not Found!</h1>
                    <p className='text-lg lg:text-xl text-slate-600'>We couldn't find the page you are looking for. </p>
                    <ul className='flex flex-col list-disc text-slate-600'>
                        <li className='list-inside list-item text-lg lg:text-xl'>Check if the URL is correct.</li>
                        <li className='list-inside list-item text-lg lg:text-xl'>Ensure there are no typos or extra spaces.</li>
                        <li className='list-inside list-item text-lg lg:text-xl'>Go back to the <Link to='/' className='text-blue-500 hover:text-purple-700'>homepage.</Link></li>
                    </ul>
                </div>
            </div>

            <Footer />
        </div>
    )
}