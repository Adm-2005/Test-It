import Home from "../pages/Home.jsx";
import Error from "../pages/Error.jsx";
import Input from "../pages/Input.jsx";
import SignUp from "../pages/SignUp.jsx";
import SignIn from "../pages/SignIn.jsx";
import Dashboard from "../pages/Dashboard.jsx";
import Profile from "../pages/Profile.jsx";

export const routes = [
    {
        path: "/",
        element: <Home />,
        errorElement: <Error />,
    },
    {
        path: "/sign-in",
        element: <SignIn />,
    },
    {
        path: "/sign-up",
        element: <SignUp />,
    },
    {
        path: "/test-studio",
        element: <Input />,
    },
    {
        path: "/dashboard/:id",
        element: <Dashboard />,
    },
    {
        path: "/profile/:id",
        element: <Profile />,
    },
];
