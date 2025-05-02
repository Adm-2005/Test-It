import {configureStore} from "@reduxjs/toolkit";
import userReducer from "./slices/userSlice";
import projectReducer from "./slices/projectSlice";
import sessionReducer from "./slices/sessionSlice";

export const store = configureStore({
    reducer: {
        users: userReducer,
        projects: projectReducer,
        sessions: sessionReducer
    }
});