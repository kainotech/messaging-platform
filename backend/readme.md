## Env 
  python -m virtualenv .venv --clear
  
  pip install -r requirements.txt
 
 ## Service
  uvicorn main:app --reload

## Streamlit Ui
  streamlit run app.py
