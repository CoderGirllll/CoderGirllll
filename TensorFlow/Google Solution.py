#Checking the virtual environment
python -m venv myenv
myenv\Scripts\activate.bat

pip freeze > requirements.txt
pip install -r requirements.txt

