# Inventory_items
It is simple web to see,update,edit,delete inventory and you can also export data of a product to a csv file

First to get this project run--------

First of all download Zip file from github and then extract all files in a single folder

after that you should have python installed in your system to run this project so to install python----
Just Visit https://www.python.org/

after that select latest version according to your Operating system(Windows/Linux/Mac)
after downloading install it in your system after installing to check installation in your command prompt just write---

python --version

it will show version of installed python

after python you should have installed virtual envirnment if not then open cmd prompt and write command--

pip install virtualenv
or
pip install virtualenvwrapper-win

after intsalling virtualenv now create a virtual enviornment so write command in cmd--

mkvirtualenv yourchoice
 
Now open folder where project is there after that open your command prompt in that directory and then write command--

workon yourchoice

from this command now you will be in virtual enviornment after that write command--

pip install -r requirements.txt

it will install all required packages after installing packages now just to make database connect and work write command--

python manage.py migrate

and after that write command---

python manage.py makemigrations

and now there is just final step just write command--

python manage.py runserver

it will run your local server and you can view your website on http://127.0.0.1:8000/
