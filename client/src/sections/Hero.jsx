import { Link } from "react-router-dom";

export default function Hero() {
    return (
        <section
            id="hero"
            className="bg-purple-950 flex items-center min-h-[500px]"
        >
            <div className="w-full lg:w-1/2 lg:relative flex flex-col items-center lg:items-start lg:pl-[10%] gap-7 p-3">
                <h1 className="text-center lg:text-left text-white font-poppins font-bold text-2xl md:text-4xl lg:text-5xl">
                    Say Hello to the Testing Assistant You’ll Rely On: Test-It!
                </h1>
                <p className="text-justify lg:text-left text-slate-300 text-lg">
                    Test-It! simplifies your QA process with intuitive test case
                    generation, step-by-step instructions, and detailed results
                    tracking—all in one seamless, web-based tool designed to
                    make software testing faster and smarter.
                </p>
                <div className="flex gap-3">
                    <Link to="/sign-in">
                        <button type="button" className="btn btn-accent">
                            Sign In
                        </button>
                    </Link>
                    <Link to="/sign-up">
                        <button type="button" className="btn btn-primary">
                            Sign Up
                        </button>
                    </Link>
                </div>
            </div>
            <div className="hidden w-1/2 lg:flex items-center justify-center">
                <img src="/src/assets/images/hero.png"></img>
            </div>
        </section>
    );
}
