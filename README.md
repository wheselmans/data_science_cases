# data_science_cases
Fictitious data science cases (educational purposes)

In this repository, you can add interesting data science cases found on the internet and adjusted to your own needs.
Make sure you add a README.md file with description of the case, source of the case,..

Structure:\
cases/ \
├── case_x/ \
│ ├── data/ \
│ │ ├── file1.csv \
│ │ ├── file2.json \
│ ├── notebook1.ipynb \
│ ├── notebook2.py \
│ ├── README.md \
├── case_y/ \
│ ├── data/ \
│ │ ├── file3.csv \
│ │ ├── file4.parquet \
│ ├── notebook3.py \
│ ├── README.md \
├── README.md\

### How to start?

Create a virtual environment and install the requirements.txt file so all necessary packages are in your venv:
python -m venv myenv
Activate the venv called 'myenv': myenv\Scripts\activate
pip install -r requirements.txt

### To use kaggle

Make sure you have the .kaggle/kaggle.json file with your API credentials in your main working directory.
You can download the kaggle.json file from your kaggle account on the website.