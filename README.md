# Mlor-ranch
KALRO have no research centers in Siaya county nor do they have any contact centers in the county. Farmers who need beef cattle production have to travel all the way to Kisumu County to a private ranch where they can be trained on beef cattle raring and buy heifers and bulls.. 


### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/JamesMusembi/Mlor-ranch.git

```

--> Move into the directory where we have the project files :
```bash
cd Mlor- ranch

```

--> Create a virtual environment :
```bash
# Create our virtual environment
python -m venv venv

```

--> Activate the virtual environment : <br><br>
windows
```bash
venv\scripts\activate

```
linux
```bash
source venv/bin/activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Migrate Database
```bash
python manage.py migrate

```

--> Create Super User
```bash
python manage.py createsuperuser

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/
