# Youtube Video Loader

Django Website which can be used to download audio file (mp3) of Youtube videos. 


## Installation manual

1. Downloading the project
```
git clone https://github.com/iberdiev/asyncloader 
```
2. cd asyncloader     ## Referring needed directory
3. virtualenv --python=/usr/bin/python3.5 myvenv     ## Creating a virtual environment with python3.5
4. . myvenv/bin/activate     ## Activating virtual environment (for OS Linux)
5. pip3 install -r requirements.txt     ## Installing all required components
6. celery -A videoloader worker -l info     ## Running celery task manager
7. Open a new terminal and activate the same venv (Step 4)
8. python3 manage.py runserver     ## Run django server through manage.py
9. http://127.0.0.1:8000/     ## Go to the given address from browser and enjoy
10. Create a folder asyncloader/media     ## Creating a folder where will be the video and audio 
<h4>Run with python==3.5, due to compatibility issues with celery/redis</h4>

## Usage manual

1. Click on "Download music"
2. Put the link of the video and your email --> Save
3. Click on "Send an email"
4. New folder will be created asyncloader/media
5. There will be video and audio file generated from the link
6. You can go to "History" and watch inputted links
