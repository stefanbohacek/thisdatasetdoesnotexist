export default async () => {
  const datasetOutput = document.getElementById("dataset");

  try {
    const resp = await fetch("/generate");
    const respJSON = await resp.json();

    if (respJSON && respJSON.dataset) {
      datasetOutput.innerHTML = respJSON.dataset;
    }
  } catch (error) {
    console.log(error);
    return {};
  }
};
