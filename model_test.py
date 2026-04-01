import pickle
import pandas as pd

def test_single_input():
    # load model
    with open("car_price_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("label_encoders.pkl", "rb") as f:
        label_encoders = pickle.load(f)

    with open("binary_encoders.pkl", "rb") as f:
        binary_encoders = pickle.load(f)

    with open("model_columns.pkl", "rb") as f:
        model_columns = pickle.load(f)

    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)


    sample_input = {
        'brand': 'BMW',
        'model': '3 Series',
        'year': 2019,
        'transmission': 'Semi-Auto',
        'km': 45000,
        'fuelType': 'Diesel',
        'engineSize': 2.0
    }

    # 3. PREPROCESSING
    df = pd.DataFrame([sample_input])

    # Model/Brand
    if df['model'].iloc[0] not in label_encoders['model'].classes_:
        df['model'] = 'Other'
    if df['brand'].iloc[0] not in label_encoders['brand'].classes_:
        df['brand'] = 'Other'

    # Label Encoding
    for col in ['brand', 'model']:
        df[col] = label_encoders[col].transform(df[col])

    # Binary Encoding
    for col in ['transmission', 'fuelType']:
        df = binary_encoders[col].transform(df)

    # Scaling
    scale_cols = ['km', 'engineSize', 'year']
    df[scale_cols] = scaler.transform(df[scale_cols])

    # Reindex
    df = df.reindex(columns=model_columns, fill_value=0)

    # 4. Predict
    prediction = model.predict(df)

    print("-" * 30)
    print(f"İnput: {sample_input['brand']} {sample_input['model']} ({sample_input['year']})")
    print(f"PyCharm Predict: {prediction[0]:,.2f} TL")
    print("-" * 30)


if __name__ == "__main__":
    test_single_input()

