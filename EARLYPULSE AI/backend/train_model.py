import json
import joblib

from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from backend.config import MODEL_PATH
from backend.config import METRICS_PATH

from backend.preprocessing import (
    load_data,
    build_preprocessor,
    split_data,
)


def main():

    # Load dataset
    df = load_data()

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(df)

    # Build preprocessing pipeline
    preprocessor = build_preprocessor(df)

    models = {
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42,
        ),

        "xgboost": XGBClassifier(
            n_estimators=200,
            max_depth=4,
            learning_rate=0.05,
            random_state=42,
            eval_metric="logloss",
        ),
    }

    best_model = None
    best_score = -1

    metrics = {}

    for name, model in models.items():

        pipeline = Pipeline(
            [
                ("preprocessor", preprocessor),
                ("classifier", model),
            ]
        )

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        f1 = f1_score(y_test, predictions)

        metrics[name] = {
            "accuracy": float(accuracy),
            "f1_score": float(f1),
        }

        if f1 > best_score:

            best_score = f1
            best_model = pipeline

    joblib.dump(best_model, MODEL_PATH)

    with open(METRICS_PATH, "w") as file:

        json.dump(metrics, file, indent=4)

    print("\nTraining complete.\n")
    print(metrics)


if __name__ == "__main__":
    main()