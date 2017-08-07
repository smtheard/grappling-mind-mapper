# Grappling Mind Mapper

### Getting Started:

Webpack (Bundles NPM Dependencies only):
```
sudo npm install webpack -g
```

NPM Dependencies:
```
npm install
webpack
```

This app is a little different, you only need to re-run webpack if you include another NPM dependency, so no reason to run with the --watch arg.

Make sure apt (or apt-get) is up to date:
```bash
sudo apt update
```

Install / Configure Postgres and add development database:
```bash
sudo apt-get install postgresql postgresql-contrib
sudo -i -u postgres
createuser --interactive 
Enter name of role to add: <whatever_username_you_want_for_db_access>
Shall the new role be a superuser? (y/n) y
createdb mindmapper_development
```

Install Redis (used for storing sessions) and Python deps:
```bash
sudo apt-install redis-server
sudo pip install -r requirements.txt
```
Run the app:
```bash
python server.py
```
