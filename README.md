# Intelbot: Discord.py based bot
Hello, im intel28 (the real one, trust) and i made IntelBot, maybe the worst discord bot in history (being honest).

# How to install the dependencies

very easy to do, here is a quick tutorial for Windows, MacOS, Linux with PEP 668 and Linux without PEP 668:

## Windows
### Step 1: Installing Python
go to https://python.org/downloads and download the latest version for Windows.
Follow the installation wizard, and before installing make sure you add Python to the PATH, to do that so, check the checkmark related to adding python to the PATH; After that, install Python.

> To make sure you installed python correctly, execute in Windows Powershell or CMD:
>
> `python --version` and `pip --version`
>
> if you get an error, it means you didn't add it to the PATH.

### Step 2: Installing discord.py
Open your cmd or Powershell and execute:
`python -m pip install -U discord.py`
this will install the discord.py library.

## MacOS
### Step 1: Installing python

Go to https://www.python.org/downloads/macos/ and click on `'Latest Python 3 Release'` as seen below.
![Image.jpeg](https://github.com/IntelMint28/Intelbot/blob/c22e1e1274ecac3cc4162f9964b245254c8e54c1/pictures/Look.jpg)

### Step 2: Check for the PATH
Go to your terminal and execute:
`python --version` and `pip --version`.
if the output of at least one contains:
`zsh: command not found:`, it means python or pip are not in the PATH. If all is good and shows the python and pip version.

To fix this, execute:
`export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"`, then `source ~/.zshrc`.

if the problem persists, watch a youtube video ig

### Step 3: Installing discord.py
just execute `python3 -m pip install -U discord.py` and that's all.

## Linux
In linux systems there are two methods, but the methods may vary for your distribution.

### What is PEP 668?
PEP 668 is a way to block library instalation via pip, These come ussually with Debian-based systems, and helps the system to not break.
### Installing discord.py with PEP 668
execute the following in your distro's terminal, in order:
`sudo apt update`
`sudo apt install python3-venv`
`python3 -m venv bot-env`
`source bot-env/bin/activate`
`python -m pip install -U pip`
`python -m pip install -U discord.py`
> make sure that in the terminal's directory is your .py file.

### Installing discord.py without PEP 668
This part works with old Debian-based systems and other distros like Arch Linux, Manjaro, etc.
#### Old Debian-based systems:
`sudo apt update`
`sudo apt install python3 python3-pip`
`python3 -m pip install -U discord.py`

#### Arch/Manjaro
`sudo pacman -S python python-pip`
`python3 -m pip install -U discord.py`

## [OPTIONAL]
if you want, instead of normally installing discord.py, you can install it with voice channel focusement too.
to do that, instead of installing '`discord.py`', install '`"discord.py[voice]"`'.
