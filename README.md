# 🎯 Student Performance Predictor System

An **end-to-end Machine Learning** project that predicts a student's **Math score** using features like gender, race/ethnicity, parental education, lunch type, test preparation course, and reading/writing scores.  
Built with **Python, Scikit-learn, Flask, Pandas**, and a clean, responsive HTML/CSS UI.

---

## ✨ What’s inside

- **Full ML pipeline**  
  - Data ingestion → train/test split  
  - Data transformation (encoding, scaling)  
  - Model training & evaluation  
  - Persisted artifacts (`preprocessor.pkl`, `model.pkl`)
- **Web app (Flask)** to submit features via form and get a predicted Math score
- **Clear project structure**, logging, and custom exceptions
- **Reproducible environment** via `requirements.txt`

---

## 🧱 Project Structure

```
.
├── app.py                        # Flask entrypoint (run the app)
├── requirements.txt
├── artifacts/                    # Saved artifacts (created after training)
│   ├── preprocessor.pkl
│   └── model.pkl
├── notebook/                     # EDA / exploration notebooks
├── templates/
│   ├── index.html                # Landing page
│   └── home.html                 # Prediction form + result
└── src/
    ├── components/               # Pipeline building blocks
    │   ├── data_Ingestion.py
    │   ├── data_transformation.py
    │   └── model_trainer.py
    ├── piplines/                 # (spelling as used in repo) runtime pipelines
    │   └── predict_pipeline.py
    ├── utils.py                  # save/load helpers, etc.
    ├── logger.py                 # logging config
    └── exception.py              # CustomException
```
> **Note:** Your repo uses the folder name `piplines` (without “e”). The README uses that exact spelling to match your code.

---

## 🚀 Quickstart

### 1) Clone & create a virtual environment
```bash
git clone https://github.com/<your-username>/student-performance-predictor-system.git
cd student-performance-predictor-system

# Windows (PowerShell)
python -m venv venv
.env\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2) Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3) (First time) Train the model & create artifacts
This generates `artifacts/preprocessor.pkl` and `artifacts/model.pkl`.

If you have a training script (recommended):
```bash
# adjust if your training script/module differs
python -m src.components.data_Ingestion
python -m src.components.data_transformation
python -m src.components.model_trainer
```

> If you created a single training entrypoint (e.g., `src/piplines/train_pipeline.py`), run:
> ```bash
> python -m src.piplines.train_pipeline
> ```

Confirm:
```bash
dir artifacts       # Windows
# or
ls artifacts        # macOS/Linux
```

You should see:
```
preprocessor.pkl  model.pkl  train.csv  test.csv
```

### 4) Run the web app
```bash
python app.py
```
Open: **http://127.0.0.1:5000/**

---

## 🧠 How it works

1. **Data Ingestion** (`src/components/data_Ingestion.py`)  
   - Reads raw CSV (e.g., `notebook/data/stud.csv`)  
   - Splits into train/test  
   - Writes `artifacts/train.csv` and `artifacts/test.csv`

2. **Data Transformation** (`src/components/data_transformation.py`)  
   - Builds a **preprocessing pipeline** (encodes categoricals, scales numerics)  
   - Saves `artifacts/preprocessor.pkl`

3. **Model Training** (`src/components/model_trainer.py`)  
   - Trains candidate models (e.g., Linear Regression, RandomForest, XGBoost/CatBoost if enabled)  
   - Selects best model via metrics (e.g., R² / RMSE)  
   - Saves `artifacts/model.pkl`

4. **Prediction** (`src/piplines/predict_pipeline.py`)  
   - Loads `preprocessor.pkl` and `model.pkl`  
   - Transforms incoming form data and returns **predicted Math score**

---

## 🧪 Example: Prediction Flow (UI)

1. Go to **Home** (`/`) → Click to open the prediction form.  
2. Select:
   - Gender, Race/Ethnicity, Parental Education  
   - Lunch type, Test preparation  
   - Reading score, Writing score  
3. Submit → The app returns the **predicted Math score**.

---

## 🧰 Utilities & Conventions

- **Artifacts directory**:  
  All persisted files are in `artifacts/`.  
  Flask loads them using **paths relative to the project root** (avoid CWD issues).

- **Custom exceptions / logging**:  
  Consistent error traces with file & line number via `CustomException` and `logger`.

- **Requirements**:  
  Ensure your `requirements.txt` uses the correct names (e.g., `scikit-learn`, not `sklearn`).

---

## ⚙️ Configuration tips

- VS Code: tell the Python analyzer where `src` lives (optional but helps linting):
  ```json
  // .vscode/settings.json
  {
    "python.analysis.extraPaths": ["./src"],
    "python.defaultInterpreterPath": "venv\Scripts\python.exe"
  }
  ```
- Always run the app from **project root**:
  ```bash
  python app.py
  ```

---

## 🐞 Troubleshooting

**Q: Flask error — `No such file or directory: 'artifacts\preprocessor.pkl'`**  
A: Train first (create artifacts) **and** ensure filenames match exactly:
```bash
python -m src.components.data_Ingestion
python -m src.components.data_transformation
python -m src.components.model_trainer
```
Also check spelling (e.g., not `proprocessor.pkl`).

**Q: Import errors like `cannot import name DataTransformation`**  
A:
- Confirm the class name matches exactly in `data_transformation.py`  
- Avoid circular imports; move heavy imports into the `if __name__ == "__main__":` block  
- Run from project root so package imports resolve

**Q: VS Code shows yellow underline on `from src....`**  
A: Set:
```json
"python.analysis.extraPaths": ["./src"]
```
(or use module runs: `python -m src.components.data_Ingestion`)

**Q: PowerShell won’t activate venv**  
A:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
.env\Scripts\Activate.ps1
```

---

## 📈 Possible Enhancements

- Add a unified training script (e.g., `src/piplines/train_pipeline.py`)
- Export metrics/plots to `artifacts/metrics.json`
- Containerize with Docker
- CI (GitHub Actions) to lint/test on push
- Cloud deployment (Render/Heroku/AWS) with persistent storage

---

## 📜 License

This project is licensed under the **MIT License**.  
See `LICENSE` for details.

---

## 🙌 Acknowledgements

- Dataset structure inspired by classic **Students Performance** dataset variants  
- Thanks to the **Scikit-learn** and **Flask** communities