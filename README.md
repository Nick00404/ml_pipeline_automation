# ML Pipeline Automation Project

This project is a comprehensive, **production-ready machine learning pipeline** designed for flexibility and scalability across many industries. It integrates **state-of-the-art MLOps tools** and provides a modular, configurable structure for data ingestion, preprocessing, training, deployment, monitoring, and auto-retraining.


## 🚀 What You'll Get

✅ How to structure a real-world ML pipeline  
✅ How to modularize and reuse your code  
✅ How to automate training workflows  
✅ How to deploy models using FastAPI and Docker  
✅ How to monitor production ML systems  
✅ How to configure pipelines without changing code  

## Project Structure

```
ml_pipeline_automation/
├── .gitignore
├── .env
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── requirements.txt
├── .dockerignore
├── .github/
│   └── workflows/
│       └── deploy.yml
├── autoretrain/
│   ├── auto_retrain.py
│   └── schedule.sh
├── configs/
│   ├── model_config.yaml
│   └── training_config.yaml
├── data/
│   ├── raw/ (.gitkeep)
│   └── processed/ (.gitkeep)
├── frontend/
│   ├── package.json
│   └── src/
│       ├── App.js
│       ├── index.html
│       └── index.js
├── logs/ (.gitkeep)
├── models/ (.gitkeep)
├── monitoring/
│   ├── prometheus.yml
│   └── dashboards/
│       └── fastapi_dashboard.json
├── notebooks/
│   └── sample_notebook.ipynb
├── scripts/
│   ├── deploy_aws.sh
│   ├── run_training.sh
│   └── start_server.sh
├── src/
│   ├── data.py
│   ├── data_cleaning.py
│   ├── data_ingestion.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── model_evaluation.py
│   ├── model_server.py
│   ├── model_training.py
│   ├── train.py
│   ├── utils.py
│   └── __init__.py
├── terraform/
│   ├── main.tf
│   └── variables.tf
└── tests/
    ├── test_api.py
    └── test_model.py
```


## 🧰 Tech Stack

- **Python 3.10**  
- **FastAPI** for serving ML models  
- **scikit-learn** for model training  
- **Docker** for containerization  
- **GitHub Actions** for CI/CD  
- **Prometheus & Grafana** for monitoring  
- **Terraform** for cloud infrastructure  
- **YAML** for configuration  
- **React** for minimal dashboard  

---

## 🔧 How It Works (Step-by-Step)

### 1. Add Your Dataset

Place your `.csv` file inside:

```
data/raw/
```

Make sure your dataset includes a `target` column. If not, update `train.py` and `configs/training_config.yaml` accordingly.

---

### 2. Install Dependencies

- Update `.env` File with your configuration.

```bash
pip install -r requirements.txt
```

---

### 3. Configure the Pipeline

Edit `configs/training_config.yaml` and `configs/model_config.yaml` to customize model type, parameters, train-test split, etc.

```yaml
model:
  type: "RandomForest"
  params:
    n_estimators: 100
    max_depth: 5

train_test_split:
  test_size: 0.2
  random_state: 42
```

---

### 4. Run the Pipeline

Run all steps — ingestion, preprocessing, training, evaluation — using:

```bash
python train.py
```

✔️ The trained model will be saved in `models/`  
✔️ Metrics and reports will be printed to the terminal  

---

## 📂 Key Modules in `src/`

| File | Purpose |
|------|---------|
| `data_ingestion.py` | Load raw data |
| `data_cleaning.py` | Handle nulls, fix types |
| `feature_engineering.py` | Scale and encode features |
| `model_training.py` | Train model using YAML config |
| `model_evaluation.py` | Print accuracy, classification report |
| `utils.py` | Helper functions (e.g., load YAML) |
| `api/` | FastAPI server for inference |

---

## 🖥️ Serving the Model (API)

Once a model is trained, start the API server:

```bash
bash scripts/start_server.sh
```

Access it via:  
`http://localhost:8000/docs`  
You’ll see an interactive Swagger UI to test your ML model.

---

## ☁️ Deploy to Cloud

Using **Terraform**, you can deploy the whole stack (Docker, FastAPI, Prometheus, Grafana) on an AWS EC2 instance.

```bash
cd terraform/
terraform init
terraform apply
```

Make sure your AWS credentials are set.

---

## 📊 Monitoring

- **Prometheus** scrapes metrics from your API.
- **Grafana** provides real-time dashboards.

Access Grafana via the browser (default port 3000). Dashboards are located in:

```
monitoring/dashboards/
```

---

## 🔄 Auto-Retraining

Automatically retrain models on a schedule (e.g., every week):

- Edit `autoretrain/schedule.sh` and configure a cron job.
- The script will re-run `train.py` and log results.

---

## 🧪 Testing

Unit tests are located in `tests/`. Run them using:

```bash
pytest tests/
```

---

## 💡 Advanced Extensions (Ideas)

- Add MLflow for experiment tracking  
- Integrate Optuna for hyperparameter tuning  
- Add XGBoost or LightGBM as options in the config  
- Deploy the API with Kubernetes  
- Extend pipeline to handle regression problems  

---

## 🙌 Contribution

Found a bug? Have a feature idea? Want to improve docs?

Feel free to fork this repo, submit a pull request, or open an issue.  
This project is made to grow with your learning 📈

---

## 📜 License

MIT License © 2025


