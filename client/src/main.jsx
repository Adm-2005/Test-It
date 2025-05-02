import { StrictMode } from "react";
import { Provider } from "react-redux";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { routes } from "./utils/appConfig.jsx";
import { store } from "./redux/store.js";
import "./index.css";

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <Provider store={store}>
            <RouterProvider
                router={createBrowserRouter(routes)}
            ></RouterProvider>
        </Provider>
    </StrictMode>
);
