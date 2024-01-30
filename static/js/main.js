import ready from "/static/js/modules/ready.js";
import showNewDataset from "/static/js/modules/showNewDataset.js";

ready(() => {
  showNewDataset();

  const refreshDatasetBtn = document.getElementById("refresh-dataset");
  refreshDatasetBtn.addEventListener("click", async () => {
    refreshDatasetBtn.classList.add("btn-clicked");
    setTimeout(() => {
      refreshDatasetBtn.classList.remove("btn-clicked");
    }, 300);
    showNewDataset();
  });
});
