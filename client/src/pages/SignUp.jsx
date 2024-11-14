import { Link } from "react-router-dom";
import { MdError } from "react-icons/md";
import { IconContext } from "react-icons/lib";
import Navbar from "../components/Navbar.jsx";
import Footer from "../components/Footer.jsx";

export default function SignUp() {
    return (
        <div className='bg-purple-950 min-h-screen flex flex-col gap-5 lg:gap-10'>
            <Navbar />
            
            <section className='flex flex-grow justify-center items-center'>
                <form action='' method='post' className='bg-black/20 max-w-md w-[90%] flex flex-col gap-4 p-12 rounded-xl' noValidate>
                    <h1 className='text-accent text-center text-xl font-bold font-josefin'>Join Test-It!</h1>
                    <div className='flex flex-col gap-2'>
                        <label className='font-poppins text-lg text-white'>Full Name</label>
                        <input type='text' className='p-1 rounded-sm focus:outline-accent'></input>
                        <span id='error-cont' className='hidden text-red-600 text-xs'>
                            <div className='flex gap-2 items-center'>
                                <IconContext.Provider value={{ size: '20px' }}>
                                    <MdError />
                                </IconContext.Provider>
                                <p id='error-message'></p>
                            </div>
                        </span>
                    </div>

                    <div className='flex flex-col gap-2'>
                        <label className='font-poppins text-lg text-white'>Email</label>
                        <input type='email' className='p-1 rounded-sm focus:outline-accent'></input>
                        <span id='error-cont' className='hidden text-red-600 text-xs'>
                            <div className='flex gap-2 items-center'>
                                <IconContext.Provider value={{ size: '20px' }}>
                                    <MdError />
                                </IconContext.Provider>
                                <p id='error-message'></p>
                            </div>
                        </span>
                    </div>

                    <div className='flex flex-col gap-2'>
                        <label className='font-poppins text-lg text-white'>Password</label>
                        <input type='password' className='p-1 rounded-sm focus:outline-accent'></input>
                        <span id='error-cont' className='hidden text-red-600 text-xs'>
                            <div className='flex gap-2 items-center'>
                                <IconContext.Provider value={{ size: '20px' }}>
                                    <MdError />
                                </IconContext.Provider>
                                <p id='error-message'></p>
                            </div>
                        </span>
                    </div>

                    <div className='flex flex-col gap-2'>
                        <label className='font-poppins text-lg text-white'>Confirm Password</label>
                        <input type='password' className='p-1 rounded-sm focus:outline-accent'></input>
                        <span id='error-cont' className='hidden text-red-600 text-xs'>
                            <div className='flex gap-2 items-center'>
                                <IconContext.Provider value={{ size: '20px' }}>
                                    <MdError />
                                </IconContext.Provider>
                                <p id='error-message'></p>
                            </div>
                        </span>
                    </div>

                    <Link to='/sign-in'>
                        <p className='text-slate-300'>
                            Already an user? <span className='text-accent'>Sign In.</span>
                        </p>
                    </Link>

                    <button type='submit' className='btn btn-accent'>
                        Sign Up
                    </button>

                </form>
            </section>

            <Footer />
        </div>
    )
}