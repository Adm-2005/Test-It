import { useState } from "react";
import { faqs } from "../utils/textConstants";

export default function FAQs() {
    const [open, setOpen] = useState(null);

    const handleOpen = (value) => setOpen(open === value ? null : value);

    return (
        <section
            id="faqs"
            className="w-full flex flex-col gap-[30px] p-3 justify-center items-center py-[40px]"
        >
            <div className="flex flex-col gap-2">
                <h1 className="font-josefin font-bold text-center text-purple-950 text-4xl md:text-5xl">
                    FAQs
                </h1>
                <p className="text-center text-slate-500 font-poppins italic">
                    Your questions about us, answered.
                </p>
            </div>
            <div className="max-w-md md:max-w-xl lg:max-w-3xl w-full flex flex-col gap-2">
                {faqs.map((faq, index) => (
                    <details
                        key={index}
                        className="p-2 md:p-4 shadow-lg rounded-lg border-purple-950"
                        open={open === index}
                    >
                        <summary
                            onClick={() => handleOpen(index)}
                            className="font-poppins font-medium text-purple-950 md:text-xl"
                        >
                            {faq.q}
                        </summary>
                        <p className="font-poppins font-medium m-3 text-slate-700">
                            {faq.a}
                        </p>
                    </details>
                ))}
            </div>
        </section>
    );
}
