import { createAsyncThunk } from "@reduxjs/toolkit";

export const registerUser = createAsyncThunk(
    "users/registerUser",
    async (userData, { rejectWithValue }) => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/users/auth/register`,
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(userData),
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Registration failed.");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const loginUser = createAsyncThunk(
    "users/loginUser",
    async (userCredentials, { rejectWithValue }) => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/users/auth/login`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(userCredentials),
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Login failed.");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);
