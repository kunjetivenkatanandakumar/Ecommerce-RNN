# E-Commerce Sales Forecasting using Simple RNN

## Project Overview

This project uses a Simple Recurrent Neural Network (RNN) to forecast the next day's sales for an e-commerce business based on historical sales data.

The model is trained using TensorFlow/Keras and deployed using Streamlit.

---

## Business Problem

E-commerce companies need accurate sales forecasting to:

- Manage inventory
- Reduce stock shortages
- Improve supply chain planning
- Estimate future revenue
- Support business decision-making

This project predicts the next day's sales using the previous three days' sales data.

---

## Dataset

The dataset contains:

| Column | Description |
|----------|-------------|
| Date | Sales Date |
| Sales | Daily Sales Value |

Example:

| Date | Sales |
|---------|---------|
| 2024-01-01 | 120 |
| 2024-01-02 | 125 |
| 2024-01-03 | 130 |

File:

```
ecom_sales_data.csv
```

---

## Project Workflow

```
Dataset
   ↓
Preprocessing
   ↓
Normalization
   ↓
Sequence Creation
   ↓
Simple RNN Model
   ↓
Training
   ↓
Model Saving (.keras)
   ↓
Streamlit Deployment
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-Learn
- Streamlit

---

## Model Architecture

```
Input Layer
      ↓
SimpleRNN (32 Units)
      ↓
Dense Layer (1 Unit)
      ↓
Sales Prediction
```

---

## Features

- Predict next-day sales
- Interactive Streamlit UI
- Trained RNN model
- Easy deployment
- Beginner-friendly deep learning project

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Ecommerce-RNN.git
```

### Navigate to Project Folder

```bash
cd Ecommerce-RNN
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Application will start at:

```
http://localhost:8501
```

---

## Project Structure

```
Ecommerce-RNN/
│
├── app.py
├── e-com_sales.ipynb
├── ecom_sales_data.csv
├── sales_rnn_model.keras
├── requirements.txt
└── README.md
```

---

## Sample Input

```
Day 1 Sales = 180
Day 2 Sales = 185
Day 3 Sales = 190
```

## Output

```
Predicted Next Day Sales = 194.8
```

---

## Future Improvements

- LSTM Implementation
- GRU Implementation
- Real E-commerce Dataset
- Multi-feature Forecasting
- Hyperparameter Tuning
- Cloud Deployment

---

## Author

Kunjeti Venkata Nanda Kumar

MCA Fresher | Data Science & AI Enthusiast

Skills:
- Python
- Machine Learning
- Deep Learning
- TensorFlow
- Streamlit
- Data Analytics

---

## License

This project is developed for educational and learning purposes.
