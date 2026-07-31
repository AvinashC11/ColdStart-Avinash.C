import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from backend.config import DATA_FILE, TARGET_COLUMN, TEST_SIZE, RANDOM_STATE


def load_data():
    """
    Load the dataset from the CSV file.
    """

    df = pd.read_csv(DATA_FILE)

    if TARGET_COLUMN not in df.columns:
        raise ValueError(
            f"Target column '{TARGET_COLUMN}' not found.\n"
            f"Available columns: {list(df.columns)}"
        )

    return df


def get_feature_lists(df):
    """
    Separate numerical and categorical columns.
    """

    numeric_features = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    if TARGET_COLUMN in numeric_features:
        numeric_features.remove(TARGET_COLUMN)

    if TARGET_COLUMN in categorical_features:
        categorical_features.remove(TARGET_COLUMN)

    return numeric_features, categorical_features


def build_preprocessor(df):
    """
    Create preprocessing pipeline.
    """

    numeric_features, categorical_features = get_feature_lists(df)

    numeric_transformer = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            )
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                numeric_transformer,
                numeric_features
            ),
            (
                "cat",
                categorical_transformer,
                categorical_features
            ),
        ]
    )

    return preprocessor


def split_data(df):
    """
    Split features and labels.
    """

    if TARGET_COLUMN not in df.columns:
        raise ValueError(
            f"Target column '{TARGET_COLUMN}' is missing."
        )

    X = df.drop(columns=[TARGET_COLUMN])

    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    return X_train, X_test, y_train, y_test