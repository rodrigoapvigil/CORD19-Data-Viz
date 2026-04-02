# **CORD-19 Co-authorship Network Visualization**

## **Description**
This project visualizes the scientific collaboration networks within the **CORD-19 dataset** using **Gephi**. It identifies research communities and key investigators (hubs) involved in COVID-19 research by analyzing large-scale metadata.

---

## **Methodology**

* **Data Collection**: The raw data was sourced from the **CORD-19 Kaggle dataset**.
* **Preprocessing**: A **Python** script was developed to filter a representative sample of **1,000 publications**. To ensure network readability, a limit of **10 authors per paper** was applied to prevent a combinatorial explosion of connections.
* **Visualization**: The network was processed in **Gephi** using the following technical configurations:
    * **Layout**: ForceAtlas 2 (Scaling: 50.0 / Gravity: 5.0).
    * **Statistics**: Modularity metrics (Result: 0.997) for community detection.
    * **Ranking**: Node size proportional to Degree (Range: 10-50).

---

## **Main Result**

![Final Graph](./results/final_graph.png)
> **Figure 1**: Co-authorship network visualization with modularity-based coloring and degree-based node scaling.

---

## **Project Structure**
The repository is organized as follows:

* **`/data`**: Contains the processed `nodos.csv` and `aristas.csv` files.
* **`/results`**: Includes the high-resolution graph and the final report in PDF.
* **`/scripts`**: Contains the Python preprocessing script.

---
