import axios from "axios";

const baseURL = process.env.VUE_APP_URL;

const apiService = axios.create({
  baseURL,
});

export default apiService;
