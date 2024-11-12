# MLFlow Project for Absenteeism Analysis

This project is designed to analyze absenteeism data using a machine learning model with an MLflow setup to facilitate experiment tracking and reproducibility. The project includes Docker configurations for managing dependencies and infrastructure, and it leverages MLflow's tracking capabilities to log parameters, metrics, and artifacts.

## Project Structure

- **Fase_3_RefactoredV2_MLFLOW_Equipo4.ipynb**: The main notebook file containing the code for data analysis, model training, and evaluation.
- **MLProject**: The MLflow configuration file to define the execution environment and parameters.
- **docker-compose.yml**: Docker configuration to set up the MLflow server with PostgreSQL and MinIO for artifact storage.

## Requirements

- **Docker** and **Docker Compose**
- **MLflow** (if not running through Docker)
- **Python 3.8+**

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
    ```

2. **Set up environment variables**:
   Create a `.env` file in the project root directory with the following content, updating as needed:
   ```plaintext
   PG_USER=<your_postgres_user>
   PG_PASSWORD=<your_postgres_password>
   PG_DATABASE=<your_postgres_database>
   PG_PORT=5432

   MINIO_ROOT_USER=<your_minio_user>
   MINIO_ROOT_PASSWORD=<your_minio_password>
   MINIO_ADDRESS=localhost
   MINIO_PORT=9000
   MINIO_CONSOLE_PORT=9001
   MINIO_STORAGE_USE_HTTPS=0
   MLFLOW_BUCKET_NAME=mlflow-bucket

   MLFLOW_PORT=5000
    ```

3. **Start Docker containers**:
   ```bash
   docker-compose up -d
   ```

4. **Run MLflow server**:
   The `docker-compose` setup includes the MLflow server running on `http://localhost:5000`. You can access it in your browser to view and manage experiment logs.

## Running Notebook in VS Code using Jupyter Extension

To run the notebook directly in VS Code, you can use the Jupyter extension, which allows you to open and execute Jupyter notebooks within the editor.

### Steps:

1. **Install the Jupyter Extension for VS Code**:
   - Open VS Code.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
   - Search for **Jupyter** and install the extension provided by Microsoft.

2. **Open the Notebook**:
   - In VS Code, open your project folder containing the `Fase_3_RefactoredV2_MLFLOW_Equipo4.ipynb` file.
   - Locate the notebook file in the Explorer sidebar and click to open it. It will open in an interactive notebook editor.

3. **Select a Python Kernel**:
   - If prompted, select the Python environment or kernel you want to use for executing the notebook.
   - The Jupyter extension will automatically detect installed Python environments, including virtual environments.

4. **Run Cells**:
   - You can run individual cells by clicking the **Run** icon (▶️) next to each cell.
   - Alternatively, you can run all cells by selecting **Run All** from the toolbar at the top of the notebook interface.

5. **View Output**:
   - The output of each cell will be displayed directly below it, just like in a Jupyter Notebook.

6. **Save Changes**:
   - Any changes you make to the notebook will be saved automatically or can be saved manually by pressing `Ctrl+S`.

---

Using the Jupyter extension in VS Code is a convenient way to interactively develop and debug your notebook, with all the functionality available in Jupyter Notebook but integrated within the VS Code environment.


## Running the notebook with python

### Using `nbclient` to Execute the Notebook Directly

1. **Install `nbclient`:**

   ```bash
   pip install nbclient
   ```
   
2. **Create a Main Execution Script**:

   Create a `main.py` file with the following content:

   ```python
   from nbclient import NotebookClient
   from nbformat import read, write

   # Load the notebook
   with open("Fase_3_RefactoredV2_MLFLOW_Equipo4.ipynb") as f:
       notebook = read(f, as_version=4)

   # Run the notebook
   client = NotebookClient(notebook)
   client.execute()

   # Save the executed notebook (optional)
   with open("Fase_3_RefactoredV2_MLFLOW_Equipo4_executed.ipynb", "w") as f:
       write(notebook, f)
 
  
3. **Execute `main.py`:**

   Run the following command in your terminal:

   ```bash
   python main.py
   ```


## Running the Notebook with MLflow

To run the notebook using MLflow, an `MLProject` file is included. This enables you to run the notebook as an MLflow project, logging experiment results.

### Workflow Example

1. **Run the MLflow Project**:
   Use the following command to execute the notebook with MLflow, specifying parameters if needed:

   ```bash
   mlflow run . -P filepath=./Absenteeism_at_work.csv -P learning_rate=0.001 -P epochs=10
    ```

- `filepath`: Path to the absenteeism dataset (default: `./Absenteeism_at_work.csv`).
- `learning_rate`: Learning rate for model training (default: `0.001`).
- `epochs`: Number of training epochs (default: `10`).

- **Monitor the Run**: After running the project, go to the MLflow UI at `http://localhost:5000` to track the run’s parameters, metrics, and artifacts.

- **View Results**: Within the MLflow UI, you can explore detailed logs, compare runs, and visualize model performance.

## Additional Information

### Docker Services

The `docker-compose.yml` file defines the following services:

- **PostgreSQL**: Database for storing MLflow metadata.
- **MinIO**: Object storage for storing MLflow artifacts.
- **MLflow Tracking Server**: MLflow server for managing and visualizing experiment logs.

### Customizing the Project

You can modify parameters in the `MLProject` file or add new ones as needed to extend the project's functionality.
