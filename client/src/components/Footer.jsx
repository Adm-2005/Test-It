import { Link } from "react-router-dom";
import { IconContext } from "react-icons/lib";
import { DiTerminal } from "react-icons/di";
import { footerLinks } from "../utils/textConstants";

export default function Footer() {
    return (
        <div className="relative bottom-0 w-full  bg-purple-950">
            <footer className="flex flex-col items-center p-4 bg-black/20 gap-8">
                <Link to="/">
                    <div className="flex gap-2 items-center justify-center">
                        <h1 className="text-white font-semibold text-3xl">
                            Test-It!
                        </h1>
                        <IconContext.Provider
                            value={{
                                size: "40px",
                                color: "#FFB05A",
                                className: "",
                            }}
                        >
                            <DiTerminal />
                        </IconContext.Provider>
                    </div>
                </Link>
                <div>
                    <ul className="flex flex-col lg:flex-row gap-4 lg:gap-[200px]">
                        {footerLinks.map((item, index) => (
                            <li key={index} className="flex flex-col gap-3">
                                <span className="text-center text-xl text-accent font-semibold font-poppins">
                                    {item.name}
                                </span>
                                <ul className="flex flex-col gap-3">
                                    {item.links.map((subItem, index) => (
                                        <li
                                            key={index}
                                            className="text-center text-slate-300 hover:text-purple-400 text-lg font-light"
                                        >
                                            <Link to={subItem.href}>
                                                {subItem.name}
                                            </Link>
                                        </li>
                                    ))}
                                </ul>
                            </li>
                        ))}
                    </ul>
                </div>
                <p className="text-slate-300">
                    &copy; All Rights Reserved.
                    <Link
                        to="https://akshatmishra.onrender.com"
                        className="pl-2 text-accent hover:text-purple-400 underline underline-offset-2"
                    >
                        Akshat Mishra
                    </Link>
                </p>
            </footer>
        </div>
    );
}
