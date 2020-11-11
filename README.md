# Skynet_Pizza

**In order to start the virtual environment:**

```pipenv shell```

**To run Django on the localhost:**

```python manage.py runserver```

**Build from the container locally:**

```docker build -t docker_container -f Dockerfile .```

**Push and Build on the Heroku server: **

```heroku container:push web --app blooming-beyond-76863 ```

**To release the image pushed to the Heroku App:**

```heroku container:release web -a blooming-beyond-76863```

**To open the web app being run on Heroku server:**

```heroku open --app blooming-beyond-76863```     
