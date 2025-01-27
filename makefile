# Might be best to use command line for this

# python = conda activate myenv && python
# pip = conda install

# setup:
# 	conda create --name myenv python=3.9
# 	$(python) -m pip install --upgrade pip
# 	conda install --file requirements.txt

# run:
# 	$(python) main.py

# mlflow:
# 	conda activate myenv && mlflow ui

# test:
# 	$(python) -m pytest
		
# clean:
# 	rm -rf steps/__pycache__
# 	rm -rf __pycache__
# 	rm -rf .pytest_cache
# 	rm -rf tests/__pycache__

# remove:
# 	conda env remove --name myenv
# 	rm -rf mlruns