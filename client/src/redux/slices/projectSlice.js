import { createSlice } from "@reduxjs/toolkit";
import {
    createProject,
    getAllProjects,
    updateProject,
    deleteProject,
} from "../thunks/projectThunks";

const initialProjectState = {
    projects: [],
    paginationLinks: {},
    status: "idle", // idle, pending, succeeded, failed
    error: null,
};

export const projectSlice = createSlice({
    name: "projects",
    initialState: initialProjectState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(createProject.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(createProject.fulfilled, (state, action) => {
                state.projects.push(action.payload.project);
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(createProject.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(getAllProjects.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(getAllProjects.fulfilled, (state, action) => {
                state.projects = action.payload.projects;
                state.paginationLinks = action.payload.links;
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(getAllProjects.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(updateProject.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(updateProject.fulfilled, (state, action) => {
                const updatedProject = action.payload.project;
                const index = state.projects.findIndex(
                    (proj) => proj.id === updatedProject.id
                );

                if (index !== -1) {
                    state.projects[index] = updatedProject;
                }
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(updateProject.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(deleteProject.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(deleteProject.fulfilled, (state, action) => {
                state.projects = state.projects.filter(
                    (proj) => proj.id !== action.payload.deleted_proj_id
                );
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(deleteProject.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            });
    },
});

export default projectSlice.reducer;
