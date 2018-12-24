# Youtube Video Loader

Django Website which can be used to download audio file (mp3) of Youtube videos. 

##### Make sure you have:
1. installed pip 
2. installed git
3. python3.5
4. enabled remote redis connection on port 6379
## Installation manual

1. Download the project
```
git clone https://github.com/iberdiev/asyncloader 
```
2. Open needed directory
```
cd asyncloader
```
3. Create a virtual environment with python3.5
```
virtualenv --python=/usr/bin/python3.5 myvenv
```
4. Activate virtual environment (for OS Linux)
```
. myvenv/bin/activate
```
5. Install all required components
```
pip3 install -r requirements.txt
```
6. Run celery task manager
```
celery -A videoloader worker -l info
```
7. Open a new terminal and activate the same venv (Step 4)
8. Create a folder asyncloader/media (needed for storing files)
```
~/asyncloader$ mkdir media
```
9. Run django server through manage.py on newly activated venv
```
python3 manage.py runserver
```
10. Browse http://127.0.0.1:8000/

### Run with python==3.5, due to compatibility issues with celery/redis
### add email credetials in settings.py
```
EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'email@email.example'
EMAIL_HOST_PASSWORD = 'example123'
```

## Usage manual

1. Click on "Download music"
2. Put the link of the video and your email --> Save
3. Click on "Send an email"
5. You can find downloaded media files in asyncloader/media
6. Get the download link sent on you email (available on the same computer)
7. Or download an mp3 manually by clicking "download" in history.
