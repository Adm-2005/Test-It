import { createAsyncThunk } from "@reduxjs/toolkit";
import { validateToken } from "../../utils/helpers";

export const createSession = createAsyncThunk(
    "sessions/createSession",
    async ({ projId, sessionData }, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/sessions/create/${projId}`,
                {
                    method: "POST",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                    body: sessionData,
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to create session");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const getSession = createAsyncThunk(
    "sessions/getSession",
    async (sessId, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/sessions/${sessId}`,
                {
                    method: "GET",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to get session");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const getAllSessions = createAsyncThunk(
    "sessions/getAllSessions",
    async (projId, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/sessions/project/${projId}`,
                {
                    method: "GET",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to get sessions.");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const updateSession = createAsyncThunk(
    "sessions/updateSession",
    async ({ sessId, updateData }, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/sessions/${sessId}`,
                {
                    method: "PUT",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                    body: updateData,
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to update session");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const deleteSession = createAsyncThunk(
    "sessions/deleteSession",
    async (sessId, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/sessions/${sessId}`,
                {
                    method: "DELETE",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to delete session");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);
