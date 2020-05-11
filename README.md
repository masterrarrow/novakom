# novakom

Automatically checking utility bills on [novakom](https://www.novakom.com.ua/, "www.novakom.com.ua")

The script will open www.novakom.com.ua navigate through the site and open page with utility bills information. You need just to click print if you want. 


### Setup process
1. Install `python 3.7+` and if you want to create a virtual environment - `pipenv --python 3.7`
2. Inside the root directory run `pipenv shell` and `pip install requirements.txt`
3. Download [geckodriver](https://github.com/mozilla/geckodriver/releases "geckodriver") for your operating system
4. Create `.env` file with the next data:

````
STREET="your_street_name"
HOUSE="your_house_number"
CODE="your_communal_code"
FLAT="your_flat_number"
````

5. Create create shell script with the next data:

````
python /path/novakom/novakom.py
````

Where `path` - path to novakom folder.

### Run

After setting up your `.env` file and shell script you can run the application by executing the script.
