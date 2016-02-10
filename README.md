#http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x

sudo easy_install pip

#https://docs.djangoproject.com/en/1.9/topics/install/#installing-development-version

git clone git@github.com:naofumi-npd/hybrid-api.git

go to project root
cd hybrid-api


git clone git://github.com/django/django.git

pip install -e django/

if you need to change mysql credentials
vim hybrid/settings.py


you need to install some pip modules
pip install MySQL-python


http://www.django-rest-framework.org/
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

go to project directory 

python manage.py migrate

CREATE TABLE `menu` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=geostd8;


npm instlal


python manage.py runserver

go to nodeapp directory
run node app.js