import { createAsyncThunk } from "@reduxjs/toolkit";
import { validateToken } from "../../utils/helpers";

export const createProject = createAsyncThunk(
    "projects/createProject",
    async (projectData, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/projects/create`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`,
                    },
                    body: JSON.stringify(projectData),
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Project creation failed");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const getProject = createAsyncThunk(
    "projects/getProject",
    async (projId, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/projects/${projId}`,
                {
                    method: "GET",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to fetch project.");
            }

            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const getAllProjects = createAsyncThunk(
    "projects/getAllProjects",
    async (userId, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/projects/user/${userId}`,
                {
                    method: "GET",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to fetch projects.");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const updateProject = createAsyncThunk(
    "projects/updateProject",
    async ({ projId, updateData }, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/projects/${projId}`,
                {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`,
                    },
                    body: JSON.stringify(updateData),
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to update project.");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const deleteProject = createAsyncThunk(
    "projects/deleteProject",
    async (projId, { rejectWithValue }) => {
        try {
            const token = validateToken(rejectWithValue);

            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/projects/${projId}`,
                {
                    method: "DELETE",
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            const json = await response.json();

            if (!response.ok) {
                throw new Error(json.message || "Failed to delete project.");
            }

            return json.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);
