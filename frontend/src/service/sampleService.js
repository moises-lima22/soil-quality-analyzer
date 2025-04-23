import api from "./api";

export const fetchSamples = async () => {
  const response = await api.get("/samples");
  return response.data;
};

export const addSample = async (sample) => {
  const response = await api.post("/samples", sample);
  return response.data;
};

export const updateSample = async (id, sample) => {
  const response = await api.put(`/samples/${id}`, sample);
  return response.data;
};

export const deleteSample = async (id) => {
  const response = await api.delete(`/samples/${id}`);
  return response.data;
};

export const evaluateSamples = async () => {
  const response = await api.get("/evaluate");
  return response.data;
};

export const downloadReport = async () => {
  const response = await api.get("/samples/report", {
    responseType: "blob",
  });

  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement("a");
  link.href = url;
  link.setAttribute("download", "report.txt");
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};