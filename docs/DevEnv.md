#Development Environment
The installation process takes 3 steps: Downloading the directory, Setting up settings and downloading required libraries, Setting up your database. For the development we prefer using Linux based systems. So I would strongly suggest using either MacOS or Linux machine, e.g. Ubuntu.

##Install Xcode and Homebrew
We will use the package manager Homebrew to install Python 3. Homebrew depends on Apple’s Xcode package, so run the following command to install it:
```
xcode-select --install
```
Click through all the confirmation commands (Xcode is a large program so this might take a while to install depending on your internet connection).

Next, install Homebrew:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Note: You can also find this command on the homepage of the Homebrew website. It’s easiest to copy and paste since it’s a long command.

To confirm Homebrew installed correctly, run this command:
```
$ brew doctor
```
Your system is ready to brew.
Install Python 3
To install the latest version of Python, run the following command:
```
$ brew install python3
```
Now let’s confirm which version was installed:
```
$ python3 --version
Python 3.7.0
```

##Download git repository and change settings
First, let’s clone the repository with our code:
```
git clone https://github.com/nurpeiis/RED.git
```
For the next steps you have to be in the repository itself.
```
cd RED
```
Install all requrired libraries
```
pip install -r RED/requirements/base.txt
```
##Database
For the production we are using PosgreSQL 9.6.11. Install same version using brew and following command:
Remove previous versions of PostgreSQL
```
https://www.openscg.com/bigsql/postgresql/installers.jsp/
```
