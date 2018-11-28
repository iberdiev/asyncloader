# Youtube Video Loader

Django Website which can be used to download audio file (mp3) of Youtube videos. 


## Installation manual

1. Downloading the project
```
git clone https://github.com/iberdiev/asyncloader 
```
2. Referring needed directory
```
cd asyncloader
```
3. Creating a virtual environment with python3.5
```
virtualenv --python=/usr/bin/python3.5 myvenv
```
4. Activating virtual environment (for OS Linux)
```
. myvenv/bin/activate
```
5. Installing all required components
```
pip3 install -r requirements.txt
```
6. Running celery task manager
```
celery -A videoloader worker -l info
```
7. Open a new terminal and activate the same venv (Step 4)
10. Create a folder asyncloader/media (needed for storing files)
```
~/asyncloader$ mkdir media
```
8. Run django server through manage.py on newly activated venv
```
python3 manage.py runserver
```
9. Browse http://127.0.0.1:8000/

###Run with python==3.5, due to compatibility issues with celery/redis

## Usage manual

1. Click on "Download music"
2. Put the link of the video and your email --> Save
3. Click on "Send an email"
5. You can find downloaded media files in asyncloader/media
