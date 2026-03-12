import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from src.utils import save_object
import logging
from src.exception import TransformationException

class DataTransformation:

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            target = "Exited"
            X_train = train_df.drop(columns=[target])
            y_train = train_df[target]
            X_test = test_df.drop(columns=[target])
            y_test = test_df[target]

            num_cols = ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"]
            cat_cols = ["Geography", "Gender"]

            num_pipeline = Pipeline(steps=[("scaler", StandardScaler())])
            cat_pipeline = Pipeline(steps=[("encoder", OneHotEncoder())])

            preprocessor = ColumnTransformer(
                [("num", num_pipeline, num_cols),
                 ("cat", cat_pipeline, cat_cols)]
            )

            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

            save_object("artifacts/preprocessor.pkl", preprocessor)
            logging.info("Data transformation completed successfully")
            return X_train, X_test, y_train, y_test

        except Exception as e:
            raise TransformationException(f"Data transformation failed: {e}", sys)