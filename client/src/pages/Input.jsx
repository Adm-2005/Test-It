import { useState, Suspense } from 'react';
import Navbar from '../components/Navbar.jsx';
import FileUpload from '../components/FileUpload.jsx';
import Footer from '../components/Footer.jsx';
import CodeEditor from '../components/CodeEditor.jsx';
import Loading from '../components/Loading.jsx';

export default function Input() {
    const [activeButton, setActiveButton] = useState('image');
    const [images, setImages] = useState([]);
    const [code, setCode] = useState("# add your code...");
    const [selectedScope, setSelectedScope] = useState("");
    const [customScope, setCustomScope] = useState("");

    const testScopes = [
        'Functional', 'UI/UX', 'Security', 'Performance', 'Accessibility', 'Other'
    ];

    const imageButtonHandler = () => {
        setActiveButton('image');
    };

    const codeButtonHandler = () => {
        setActiveButton('code');
    };

    const scopeChangeHandler = (event) => {
        setSelectedScope(event.target.value);
        if (selectedScope !== 'Other') {
            setCustomScope("");
        }
    };

    const customScopeHandler = (event) => {
        setCustomScope(event.target.value);
    }

    return (
        <div className='flex flex-col gap-5'>
            <Navbar />

            <section className='flex flex-col gap-6 lg:gap-[50px] items-center justify-center'>
                <div className='flex'>
                    <button
                        type='button'
                        onClick={imageButtonHandler}
                        className={
                            activeButton === 'image'
                                ? 'bg-accent text-lg font-poppins p-3 w-[125px] md:w-[150px] text-purple-950 border border-accent rounded-l-xl'
                                : 'bg-white text-lg font-poppins p-3 w-[125px] md:w-[150px] text-purple-950 border border-accent rounded-l-xl'
                        }
                    >
                        Images
                    </button>
                    <button
                        type='button'
                        onClick={codeButtonHandler}
                        className={
                            activeButton === 'code'
                                ? 'bg-accent text-lg font-poppins p-3 w-[125px] md:w-[150px] text-purple-950 border border-accent rounded-r-xl'
                                : 'bg-white text-lg font-poppins p-3 w-[125px] md:w-[150px] text-purple-950 border border-accent rounded-r-xl'
                        }
                    >
                        Code
                    </button>
                </div>

                <form
                    action=''
                    method='post'
                    className='w-full flex flex-col justify-center items-center gap-5 lg:gap-[50px]'
                    noValidate
                >
                    <div className='flex flex-col lg:flex-row gap-5 lg:gap-[80px] items-center justify-center'>
                        <Suspense fallback={<Loading />}>
                            {activeButton === 'image' && (<FileUpload images={images} setImages={setImages} />)}
                            {activeButton === 'code' && (<CodeEditor code={code} setCode={setCode} />)}
                        </Suspense>

                        <div className='flex flex-col gap-3'>
                            <div className='flex flex-col gap-2 w-[250px] md:w-[400px] lg:w-[500px]'>
                                <label className='font-poppins text-purple-950'>Feature/Component Name</label>
                                <input type='text' className='p-2 border rounded-md outline outline-1 outline-purple-950' placeholder='Enter Feature Name'></input>
                            </div>

                            <div className='flex flex-col gap-2 w-[250px] md:w-[400px] lg:w-[500px]'>
                                <label className='font-poppins text-purple-950'>Test Scope</label>
                                <select value={selectedScope} onChange={scopeChangeHandler} className='p-2 border rounded-md outline outline-1 outline-purple-950'>
                                    <option className=''>--Select Scope--</option>
                                    {
                                        testScopes.map((scope) => (
                                            <option key={scope} value={scope}>{scope}</option>
                                        ))
                                    }
                                </select>
                            </div>

                            {
                                selectedScope === 'Other' && (
                                    <div className='flex flex-col gap-2 w-[250px] md:w-[400px] lg:w-[500px]'>
                                        <label className='font-poppins text-purple-950'>Custom Scope</label>
                                        <input type='text' className='p-2 border rounded-md outline outline-1 outline-purple-950' placeholder='Enter Custom Scope'></input>
                                    </div>
                                )
                            }

                            <div className='flex flex-col gap-2 w-[250px] md:w-[400px] lg:w-[500px]'>
                                <label className='font-poppins text-purple-950'>Expected Outcome</label>
                                <textarea rows='4' className='p-2 border rounded-md resize-none outline outline-1 outline-purple-950' placeholder='Describe the Feature'></textarea>
                            </div>
                        </div>
                    </div>

                    <button className='btn btn-accent w-[180px] md:w-[250px] md:py-[10px] mx-auto'>Generate</button>
                </form>
            </section>

            <Footer />
        </div>
    )
}
