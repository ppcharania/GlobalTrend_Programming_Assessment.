import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def clean_and_preprocess(df):
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    df_preprocessed = preprocessor.fit_transform(df)

    num_features = numerical_cols.tolist()
    cat_features = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols).tolist()
    feature_names = num_features + cat_features

    df_cleaned = pd.DataFrame(df_preprocessed, columns=feature_names)

    return df_cleaned

data = pd.DataFrame({
    'age': [22, 27, 29, None],
    'income': [48000, None, 54000, 58000],
    'gender': ['male', 'female', 'male', None],
    'city': ['Boston', 'Seattle', 'Boston', 'Austin']
})

df_cleaned = clean_and_preprocess(data)
print(df_cleaned)
