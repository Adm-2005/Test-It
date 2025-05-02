const navLinks = [
    {
        name: "Home",
        href: "/",
    },
    {
        name: "Features",
        href: "/#features",
    },
    {
        name: "FAQs",
        href: "/#faqs",
    },
];

const featureGroups = [
    {
        name: "Effortless Testing",
        text: "Automatically generate detailed test instructions from images or code snippets, streamlining your QA process and saving valuable time.",
        icon: "",
    },
    {
        name: "Multi-format Input",
        text: "Upload images or input code snippets with ease, enabling seamless test instruction generation for both visual and code-based content.",
        icon: "",
    },
    {
        name: "Customizable Test Scope",
        text: "Choose from a range of predefined test scopes like Functional, UI/UX, Security, and more, or create a custom scope tailored to your needs.",
        icon: "",
    },
    {
        name: "Intuitive Design",
        text: "Experience a clean, user-friendly interface that makes it simple and quick to generate, view, and manage your test instructions without any hassle.",
        icon: "",
    },
    {
        name: "Project Organization",
        text: "Easily organize and manage your test instructions across multiple projects, ensuring quick access and seamless tracking of all your testing activities.",
        icon: "",
    },
    {
        name: "Collaborate with Others",
        text: "Effortlessly share test instructions with team members or clients, enabling smooth collaboration and streamlined review processes for your projects.",
        icon: "",
    },
];

const faqs = [
    {
        q: "What is Test-It?",
        a: " Test-It! is a web-based application that generates detailed, AI-driven testing instructions for software products based on user-uploaded images or code snippets. It streamlines the testing process by analyzing your inputs and generating customized instructions.",
    },
    {
        q: "How does Test-It! generate testing instructions?",
        a: "Test-It! uses state-of-the-art AI models, to analyze uploaded images or code snippets. Based on these inputs, it generates accurate and detailed testing instructions to assist in software QA.",
    },
    {
        q: "What types of inputs can I upload to Test-It?",
        a: "Test-It! currently supports two types of inputs: Images & Code Snippets.",
    },
    {
        q: "What kind of test scopes can I select in Test-It!?",
        a: 'Test-It! offers a variety of test scope options, such as Functional, UI/UX, Security, Performance, and Accessibility. You can also choose the "Other" option to define a custom test scope if your requirements differ from these categories.',
    },
    {
        q: "Can I create multiple projects in Test-It?",
        a: "Yes! Test-It allows users to create individual projects or collections. Each project can contain multiple testing instructions organized based on your inputs, making it easy to track and manage test cases for different software features.",
    },
    {
        q: "Can I customize the generated test instructions?",
        a: "Currently, Test-It! provides test instructions based on the analysis of your input and selected scope. While there is no direct edit feature, you can provide more details or select different test scopes to influence the depth and type of instructions generated.",
    },
];

const footerLinks = [
    {
        name: "Pages",
        links: [
            {
                name: "Home",
                href: "/",
            },
            {
                name: "Sign In",
                href: "/sign-in",
            },
            {
                name: "Sign Up",
                href: "/sign-up",
            },
            {
                name: "Test Studio",
                href: "/test-studio",
            },
        ],
    },
    {
        name: "Sections",
        links: [
            {
                name: "Features",
                href: "/#features",
            },
            {
                name: "FAQs",
                href: "/#faqs",
            },
        ],
    },
    {
        name: "Contact",
        links: [
            {
                name: "Twitter",
                href: "",
            },
            {
                name: "Facebook",
                href: "",
            },
            {
                name: "Instagram",
                href: "",
            },
        ],
    },
];

export { routes, navLinks, featureGroups, faqs, footerLinks };
