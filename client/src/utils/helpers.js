export const validateToken = (rejectWithValue) => {
    const token = localStorage.getItem("accessToken");
    if (!token) throw rejectWithValue("User not authenticated");
    return token;
};
