import { createSlice } from "@reduxjs/toolkit";
import { registerUser, loginUser } from "../thunks/userThunks";

const initialUserState = {
    user: {},
    status: "idle", // idle, pending, succeeded, failed
    error: null,
    authenticated: false,
};

export const userSlice = createSlice({
    name: "users",
    initialState: initialUserState,
    reducers: {
        logoutUser: (state) => {
            if (!state.authenticated) {
                return;
            }

            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");
            state.user = {};
            state.authenticated = false;
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(registerUser.pending, (state) => {
                state.status = "pending";
            })

            .addCase(registerUser.fulfilled, (state, action) => {
                state.user = { ...action.payload.user };
                state.authenticated = true;

                localStorage.setItem(
                    "accessToken",
                    action.payload.access_token
                );
                localStorage.setItem(
                    "refreshToken",
                    action.payload.refresh_token
                );

                state.status = "succeeded";
            })

            .addCase(registerUser.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(loginUser.pending, (state) => {
                state.status = "pending";
            })

            .addCase(loginUser.fulfilled, (state, action) => {
                state.user = { ...action.payload.user };
                state.authenticated = true;

                localStorage.setItem(
                    "accessToken",
                    action.payload.access_token
                );
                localStorage.setItem(
                    "refreshToken",
                    action.payload.refresh_token
                );

                state.status = "succeeded";
            })

            .addCase(loginUser.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            });
    },
});

export const { logoutUser } = userSlice.actions;
export default userSlice.reducer;
