import { createSlice } from "@reduxjs/toolkit";
import {
    createSession,
    getAllSessions,
    updateSession,
    deleteSession,
} from "../thunks/sessionThunks";

const initialSessionState = {
    sessions: {}, // keys are projects, values are arrays of session objects
    paginatedLinks: {},
    status: "idle", // idle, pending, succeeded, failed
    error: null,
};

export const sessionSlice = createSlice({
    name: "sessions",
    initialState: initialSessionState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(createSession.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(createSession.fulfilled, (state, action) => {
                const createdSession = action.payload.session;
                const projId = createdSession.proj_id;

                if (!state.sessions[projId]) {
                    state.sessions[projId] = [];
                }

                state.sessions[projId].push(createdSession);
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(createSession.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(getAllSessions.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(getAllSessions.fulfilled, (state, action) => {
                const sessions = action.payload.sessions || [];

                if (sessions.length > 0) {
                    const projId = sessions[0].proj_id;
                    state.sessions[projId] = sessions;
                    state.paginatedLinks[projId] = action.payload.links;
                }

                state.status = "succeeded";
                state.error = null;
            })

            .addCase(getAllSessions.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(updateSession.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(updateSession.fulfilled, (state, action) => {
                const updatedSession = action.payload.session;
                const projId = updatedSession.proj_id;
                const index = state.sessions[projId].findIndex(
                    (sess) => sess.id === updatedSession.id
                );

                if (index != -1) {
                    state.sessions[projId][index] = updatedSession;
                }
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(updateSession.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            })

            .addCase(deleteSession.pending, (state) => {
                state.status = "pending";
                state.error = null;
            })

            .addCase(deleteSession.fulfilled, (state, action) => {
                const projId = action.payload.deleted_session.proj_id;
                const sessId = action.payload.deleted_session.id;

                state.sessions[projId] = state.sessions[projId].filter(
                    (sess) => sess.id !== sessId
                );
                state.status = "succeeded";
                state.error = null;
            })

            .addCase(deleteSession.rejected, (state, action) => {
                state.error = action.payload;
                state.status = "failed";
            });
    },
});

export default sessionSlice.reducer;
