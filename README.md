# videoloader
1. git clone https://github.com/iberdiev/asyncloader     ## Downloading the project
2. cd asyncloader     ## Referring needed directory
3. virtualenv myenv     ## Creating a virtual environment
4. . myenv/bin/activate     ## Activating virtual environment (for OS Linux)
5. pip install -r requirements.txt     ## Installing all required components
6. celery -A videoloader worker -l info     ## Running celery task manager
7. python3.5 manage.py runserver     ## Run django server through manage.py
8. http://127.0.0.1:8000/     ## Go to the given address from browser and enjoy
<h4>Run with python==3.5, due to compatibility issues with celery/redis</h4>

