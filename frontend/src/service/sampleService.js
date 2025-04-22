import api from "./api";

export const fetchSamples = async () => {
  const response = await api.get("/samples");
  return response.data;
};

export const addSample = async (sample) => {
  const response = await api.post("/samples", sample);
  return response.data;
};

export const evaluateSamples = async () => {
  const response = await api.get("/evaluate");
  return response.data;
};