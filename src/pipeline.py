from prefect import flow, task

from train import train_model


@task
def run_training():
    train_model()


@flow(name="used-car-price-training-pipeline")
def training_pipeline():
    run_training()


if __name__ == "__main__":
    training_pipeline()
