import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { IconContext } from 'react-icons/lib';
import { DiTerminal } from "react-icons/di";
import { PiUserListFill } from "react-icons/pi";
import { GiHamburgerMenu } from "react-icons/gi";
import { LiaTimesCircleSolid } from "react-icons/lia";
import { navLinks } from '../utils.jsx';

export default function Navbar({ isLoggedIn }) {
    const [ nav, setNav ] = useState(false); 

    const location = useLocation();
    const isHomePage = location.pathname === '/';

    const onHamClick = () => {
        setNav(!nav);
    }

    return (
        <div className={ isHomePage 
        ? 'bg-purple-950 sticky top-0 z-10' 

        : 'lg:relative lg:left-[20%] bg-purple-950 sticky top-0 w-full rounded-b-0 lg:rounded-b-xl lg:w-3/5 z-10'
        }>
            <nav className={isHomePage 
                ? 'lg:absolute lg:left-[20%] w-full lg:w-3/5 flex items-center justify-between lg:justify-between bg-black/20 h-[60px] lg:h-[100px] lg:rounded-b-xl p-3 lg:p-4' 

                : 'flex items-center justify-between lg:justify-between bg-black/20 h-[60px] lg:h-[100px] lg:rounded-b-xl p-3 lg:p-4'
            }>
                <Link to='/'>
                    <div className='flex gap-2 items-center justify-center'>
                        <h1 className='text-white font-semibold text-3xl leading-none'>
                            Test-It!
                        </h1>
                        <IconContext.Provider value={{ size: '40px', color: '#FFB05A', className: ''}}>
                            <DiTerminal />
                        </IconContext.Provider>
                    </div>
                </Link>
                <div className='flex items-center'>
                    <ul className={nav ? 'flex flex-col lg:flex-row gap-6 absolute lg:static top-[60px] left-0 right-0 bg-white lg:bg-transparent p-4' : 'hidden lg:flex gap-6 items-center justify-center'}>
                        {navLinks.map((navLink, index) => (
                            <li key={index} className='text-black hover:text-purple-400 lg:text-white text-md lg:text-lg font-semibold border-b lg:border-0'>
                                <Link to={navLink.href} className=''>
                                    { navLink.name }
                                </Link>
                            </li>
                        ))}
                        <li>
                            <Link to='/test-studio'>
                                <button type='button' className='btn btn-accent w-full'>
                                    Test Studio
                                </button>
                            </Link>
                        </li>
                    </ul>
                </div>

                {isLoggedIn && (<IconContext.Provider value={{ size:'45px', color: '#ffffff', className: ''}}>
                    <PiUserListFill />
                </IconContext.Provider>)}



                {!(isLoggedIn) && (<IconContext.Provider value={{ size:'35px', color: '#ffffff', className: 'lg:hidden' }}>
                    { nav
                        ? <LiaTimesCircleSolid onClick={onHamClick} />
                        : <GiHamburgerMenu onClick={onHamClick} />
                    }
                </IconContext.Provider>)}
            </nav>
        </div>
    )
}