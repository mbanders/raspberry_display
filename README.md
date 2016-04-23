# raspberry_display
Simple Flask App for Rasbperry PI. Based off Raspbian operating system.

Quick Use
---------
From `/home/pi`:
```sh
sudo apt-get install git python-pip
sudo pip install Flask
git clone git@github.com:mbanders/raspberry_display.git
cd raspberry_display
python mysite.py
```

Open a web browser and visit your raspberry PI.  Mine is at http://raspberrypi:5000/

Use with Apache Webserver
-------------------------
Setup:
```sh
sudo apt-get install -y apache2 libapache2-mod-wsgi
sudo mv raspberry_display.conf /etc/apache2/sites-available/
sudo a2ensite raspberry_display
sudo service apache2 reload
```

Then you should be able to visit http://raspberrypi/mysite
