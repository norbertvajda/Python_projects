#!/usr/bin/python3

# Basic concept for WordPress automatic installation on Ubuntu 18.04 - GUI, OOP coming soon ;)

import os
import random
import string
import tempfile
import zipfile

def input_lang():
    languages = ['de', 'en', 'hr', 'hu']
    while True:
        lang = input("Choose a language (de, en, hr, hu): ").lower()        
        try:
            if lang in languages:
                return lang
            else:
                print("Choose between de, en, hr and hu")
        except ValueError:
            print("Choose between de, en, hr and hu")

lang = input_lang()

local_host_name = input("Choose a name for the website (e.g. test.localhost): ").lower()
db_name = input("Choose a database name: ").lower()
db_user = input("Enter database user's name: ")
db_pass = input("enter database user's password: ")
table_prefix = input("Choose a prefix for the WordPress DB tables: ")

wp_zip_de = "https://de.wordpress.org/latest-de_DE.zip"
wp_zip_en = "https://wordpress.org/latest.zip"
wp_zip_hr = "https://hr.wordpress.org/latest-hr.zip"
wp_zip_hu = "https://hu.wordpress.org/latest-hu_HU.zip"

temp_dir = tempfile.gettempdir() + "/my_temp"
location_of_host = "/var/www"

# salt generating
def generate_salt(str_length=64):
    pass_chars = string.ascii_letters + string.digits + "!#$%&()*+,-./:;<=>?@[]^_{|}~"
    return ''.join(random.choice(pass_chars) for i in range(str_length))

# block - make temp directory and download wordpress zip
temp_lang = ""
if lang == "de":
    temp_lang = wp_zip_de
elif lang == "en":
    temp_lang = wp_zip_en
elif lang == "hr":
    temp_lang = wp_zip_hr
else:
    temp_lang = wp_zip_hu
    
os.system("mkdir " + temp_dir)
os.system("wget -O " + temp_dir + "/my_downloaded_wp.zip " + temp_lang)
# end block - make temp directory and download wordpress zip

# block - extract wordpress.zip to /var/www with the localhost name local_host_name and delete tmp
zip_ref = zipfile.ZipFile(temp_dir + "/my_downloaded_wp.zip", 'r')
zip_ref.extractall(temp_dir)
zip_ref.close()
os.system("mv " + temp_dir + "/wordpress " + temp_dir + "/" + local_host_name)
os.system("sudo cp -a " + temp_dir + "/" + local_host_name + "/. " + location_of_host + "/" + local_host_name + "/")

os.system("rm -rf " + temp_dir)
# end block - extract wordpress.zip to /var/www with the localhost name local_host_name and delete tmp

# block - Apache configuration
os.system("sudo mkdir " + location_of_host + "/" + local_host_name + "/logs")
host_first_part = local_host_name.split(".")
conf_file = open("/etc/apache2/sites-available/" + host_first_part[0] + ".conf", "x")
conf_file.write("<VirtualHost *:80>\n")
conf_file.write("   ServerAdmin webmaster@localhost\n")
conf_file.write("   ServerName " + local_host_name + "\n")
conf_file.write("   ServerAlias www." + local_host_name + "\n")
conf_file.write("\n")
conf_file.write("   DocumentRoot " + location_of_host + "/" + local_host_name + "/\n")
conf_file.write("\n")
conf_file.write("   <Directory  " + location_of_host + "/" + local_host_name + "/>\n")
conf_file.write("      AllowOverride All\n")
conf_file.write("   </Directory>\n")
conf_file.write("\n")
conf_file.write("   ErrorLog " + location_of_host + "/" + local_host_name + "/logs/error.log\n")
conf_file.write("   CustomLog " + location_of_host + "/" + local_host_name + "/logs/access.log combined\n")
conf_file.write("</VirtualHost>\n")
conf_file.close()

os.system("sudo ln -s /etc/apache2/sites-available/" + host_first_part[0] + ".conf /etc/apache2/sites-enabled/" + host_first_part[0] + ".conf")

os.system("sudo a2enmod rewrite")
os.system("sudo apache2ctl configtest")
os.system("sudo systemctl restart apache2")
# end block - Apache configuration

# block - create DB
os.system('mysql -u ' + db_user + ' -p -e "CREATE DATABASE ' + db_name + ' DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"')
# end block - create DB

# block - create wp-config.php and .htaccess
os.system("sudo touch " + location_of_host + "/" + local_host_name + "/.htaccess")

wp_config = open(location_of_host + "/" + local_host_name + "/wp-config.php", "x")
wp_config.write("<?php\n")
wp_config.write("define('DB_NAME', '" + db_name + "');\n")
wp_config.write("define('DB_USER', '" + db_user + "');\n")
wp_config.write("define('DB_PASSWORD', '" + db_pass + "');\n")
wp_config.write("define('DB_HOST', '" + local_host_name + "');\n")
wp_config.write("define('DB_CHARSET', 'utf8mb4');\n")
wp_config.write("define('DB_COLLATE', '');\n")
wp_config.write("define('FS_METHOD', 'direct');\n")
wp_config.write("\n")
wp_config.write("define('AUTH_KEY',         '" + generate_salt() + "');\n")
wp_config.write("define('SECURE_AUTH_KEY',  '" + generate_salt() + "');\n")
wp_config.write("define('LOGGED_IN_KEY',    '" + generate_salt() + "');\n")
wp_config.write("define('NONCE_KEY',        '" + generate_salt() + "');\n")
wp_config.write("define('AUTH_SALT',        '" + generate_salt() + "');\n")
wp_config.write("define('SECURE_AUTH_SALT', '" + generate_salt() + "');\n")
wp_config.write("define('LOGGED_IN_SALT',   '" + generate_salt() + "');\n")
wp_config.write("define('NONCE_SALT',       '" + generate_salt() + "');\n")
wp_config.write("\n")
wp_config.write("$table_prefix = '" + table_prefix + "';\n")
wp_config.write("\n")
wp_config.write("define('WP_DEBUG', false);\n")
wp_config.write("\n")
wp_config.write("if ( !defined('ABSPATH') )\n")
wp_config.write("	define('ABSPATH', dirname(__FILE__) . '/');\n")
wp_config.write("require_once(ABSPATH . 'wp-settings.php');\n")

wp_config.close()
# end block - create wp-config.php and .htaccess

# block - adjusting the ownership and permissions
os.system("sudo chown -R www-data:www-data " + location_of_host + "/" + local_host_name)
os.system("sudo find " + location_of_host + "/" + local_host_name + "/ -type d -exec chmod 750 {} \;")
os.system("sudo find " + location_of_host + "/" + local_host_name + "/ -type f -exec chmod 640 {} \;")
# end block - adjusting the ownership and permissions
