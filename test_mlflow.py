import mlflow

mlflow.set_experiment("Heart Disease Project")

with mlflow.start_run(run_name="Random Forest"):
    mlflow.log_param("model", "Random Forest")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", 0.83)

print("MLflow run created successfully")