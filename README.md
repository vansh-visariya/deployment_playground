in this i am try different different tools and library used in the mlops

## continuous X
Continuous Integration (CI) extends the testing and validating code and components by adding testing and validating data and models.

Continuous Delivery (CD) concerns with delivery of an ML training pipeline that automatically deploys another the ML model prediction service.

Continuous Training (CT) is unique to ML systems property, which automatically retrains ML models for re-deployment.

Continuous Monitoring (CM) concerns with monitoring production data and model performance metrics, which are bound to business metrics.

## how the MLops works actually and what can we use for it
    -Data versioning - DVC (helps to version the data) , dagshub
    -Code versioning - git (helps to version the code) , dagshub
    -ETL pipeline - Airflow (helps to create the pipeline)
    -model tracking, monitoring, versioning - MLflow (helps to track the model) , dagshub , prometheus
    -CI/CD - GitHub Actions (helps to deploy the model)
    -containerization - Docker (helps to containerize the model)
    -Container Orchestration - Kubernetes (helps to orchestrate the container)

## There are some tools i am exploring and learning
kserve, kubernetes, Prometheus, kubeflow

can you CML for CI/CD also

## airflow
for airflow, use astronomer.io(astro)

    1. winget install -e --id Astronomer.Astro # install astro

    2. astro dev init

    3. astro dev start # start the astro/airflow in the docker