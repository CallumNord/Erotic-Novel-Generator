import os

# Create directories
os.makedirs('static')
os.makedirs('templates')

# Create files
open('app.py', 'a').close()
open('config.py', 'a').close()
open('README.md', 'a').close()
open('requirements.txt', 'a').close()
open('templates/index.html', 'a').close()
