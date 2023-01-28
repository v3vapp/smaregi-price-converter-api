```
# Run API server
python -m uvicorn python.main:app --reload    
python -m uvicorn tests.beta:app --reload    
```
```
# Local venv
poetry config --local virtualenvs.in-project true
```
```
poetry export -f requirements.txt --output requirements.txt
```