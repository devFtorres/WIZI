git clone https://github.com/devFtorres/WIZI.git

create a virtualenv like :
opem a prompt in the wiz directory
run the command: 
pip install virtualenv
virtualenv myenv(you can name it whatever you want)
.\myenv\Scripts\activate

After this your virtual env should be activate and your console should have something like this:

(myenv)C:\Users\urpath....: (on windows)

After you have to navigate to the folder where manage.py is located

Now, you need to run the following commands 1 by 1:(assuming you have python installed)

pip install django
pip install -r requirements.txt

in some  cases not all the requirements will install automatically and you should need to update the following libraries:
pip install django-crispy-forms
pip install django-allauth
pip install Pillow