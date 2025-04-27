import axios from "axios";

const baseURL = process.env.apiUrl;

const apiService = axios.create({
  baseURL,
  // You can add additional configurations here
});

export default apiService;
