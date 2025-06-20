Last login: Wed Jun 18 13:22:31 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Lukass-MacBook-Air:~ lukaseideloth$ cd /pycharm
-bash: cd: /pycharm: No such file or directory
Lukass-MacBook-Air:~ lukaseideloth$ ls
Applications
Desktop
Documents
Downloads
file
get-pip.py
Library
Movies
Music
OneDrive - BildungsCentrum der Wirtschaft gemeinnützige Gesellschaft mbH
package-lock.json
Pictures
Public
PycharmProjects
scriptSE
shared Folder
VirtualBox VMs
Zotero
Lukass-MacBook-Air:~ lukaseideloth$ cd /
Lukass-MacBook-Air:/ lukaseideloth$ ls
Applications	etc		private		Users
bin		home		sbin		usr
cores		Library		System		var
dev		opt		tmp		Volumes
Lukass-MacBook-Air:/ lukaseideloth$ cd home
Lukass-MacBook-Air:home lukaseideloth$ ls
Lukass-MacBook-Air:home lukaseideloth$ ls
Lukass-MacBook-Air:home lukaseideloth$ ls -la
total 2
dr-xr-xr-x   2 root  wheel    1 18 Jun 13:22 .
drwxr-xr-x@ 20 root  wheel  640 10 Jun 08:34 ..
Lukass-MacBook-Air:home lukaseideloth$ cd ..
Lukass-MacBook-Air:/ lukaseideloth$ cd Users/PycharmProjects
-bash: cd: Users/PycharmProjects: No such file or directory
Lukass-MacBook-Air:/ lukaseideloth$ ls
Applications	etc		private		Users
bin		home		sbin		usr
cores		Library		System		var
dev		opt		tmp		Volumes
Lukass-MacBook-Air:/ lukaseideloth$ cd Users
Lukass-MacBook-Air:Users lukaseideloth$ ls
lukaseideloth	Shared
Lukass-MacBook-Air:Users lukaseideloth$ cd lukaseideloth
Lukass-MacBook-Air:~ lukaseideloth$ ls
Applications
Desktop
Documents
Downloads
file
get-pip.py
Library
Movies
Music
OneDrive - BildungsCentrum der Wirtschaft gemeinnützige Gesellschaft mbH
package-lock.json
Pictures
Public
PycharmProjects
scriptSE
shared Folder
VirtualBox VMs
Zotero
Lukass-MacBook-Air:~ lukaseideloth$ cd PycharmProjects
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ ls
coffeeMachine			LicensePlateRecognitionSystem
customerBitwarden		PythonProject
customerBW			PythonProject1
customerBW1			PythonProject2
customerBW2			scheresteinpapier
Dynamische Programmierung	Skyjo
Gefahren_generativer_KI		weatherStation
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf PythonProject/
Password:
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf PythonProject1/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf PythonProject2/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf Gefahren_generativer_KI/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf customerBW/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf customerBW1/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf customerBW2/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf customerBitwarden/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ ls
coffeeMachine			scheresteinpapier
customerBitwarden		Skyjo
Dynamische Programmierung	weatherStation
LicensePlateRecognitionSystem
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf Dynamische\ Programmierung/
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ sudo rm -rf weatherStation
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ ls
coffeeMachine			scheresteinpapier
customerBitwarden		Skyjo
LicensePlateRecognitionSystem
Lukass-MacBook-Air:PycharmProjects lukaseideloth$ ssh weatherfrog@10.12.12.101
weatherfrog@10.12.12.101's password:
Linux raspberrypi-weather 6.12.25+rpt-rpi-v7 #1 SMP Raspbian 1:6.12.25-1+rpt1 (2025-04-30) armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jun 11 18:07:05 2025 from 10.12.12.56
weatherfrog@raspberrypi-weather:~ $ cd
weatherfrog@raspberrypi-weather:~ $ ls
displayWeatherDB.py  log  README.txt  venv  weatherstation.py  web
weatherfrog@raspberrypi-weather:~ $ sudo nano displayWeatherDB.py
weatherfrog@raspberrypi-weather:~ $ touch we
weatherstation.py  web/
weatherfrog@raspberrypi-weather:~ $ touch weatherstation.py
touch: cannot touch 'weatherstation.py': Permission denied
weatherfrog@raspberrypi-weather:~ $ sudo touch weatherstation.py
weatherfrog@raspberrypi-weather:~ $ nano weatherstation.py
weatherfrog@raspberrypi-weather:~ $ cd web
weatherfrog@raspberrypi-weather:~/web $ ls
weatherWeb.py
weatherfrog@raspberrypi-weather:~/web $ nano weatherWeb.py

  GNU nano 7.2                                                weatherWeb.py
for entry in last24hours:
        print(entry)
print(len(last24hours))

dateX = []
for date in last24hours:
        dateX.append(date[1].strftime("%m-%d %H:%M"))

dateY = []
for date in last24hours:
        dateY.append(date[2])

x = dateX
y = dateY

# Checking and if so, deleting, old file

path = "/var/www/html/img/"
file = "plotTemp.png"

if os.path.exists(os.path.join(path, file)):
        os.system(f"rm {file}")
else:
        print("False")

# Create a line plot
plt.figure(figsize=(7.5,5))
plt.scatter(x, y, marker='o')
plt.tight_layout()
plt.xticks(rotation=45)
plt.title("temperature")
plt.xlabel("time")
plt.ylabel("temp")
plt.grid(True)
plt.savefig("/var/www/html/img/plotTemp.png")

dateY = []
for date in last24hours:
        dateY.append(date[4])

x = dateX
y = dateY

# Checking and if so, deleting, old file

path = "/var/www/html/img/"
file = "plotHumi.png"

if os.path.exists(os.path.join(path, file)):
        os.system(f"rm {file}")
else:
        print("False")

# Create a line plot
plt.figure(figsize=(7.5,5))
plt.scatter(x, y, marker='o')
plt.tight_layout()
plt.xticks(rotation=45)
plt.title("humidity")
plt.xlabel("time")
plt.ylabel("humid.")
plt.grid(True)
plt.savefig("/var/www/html/img/plotHumi.png")