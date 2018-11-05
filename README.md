# guild-website

Website for my guild in World of Warcraft based off Pyramid web development framework.

## Development

Once you install Python 3.6.5, follow next steps. 

Make sure pip is up to date.
```
pip install -U pip
```

Create fork to clone into local.

```
git clone $FORK_URL
git remote -v
```

Create python virtual environment outside local repo directory to install packages into. 

```
python3 -m venv $VENV_NAME
```

Once the virtual environment is established, activate it and install guild-web package in development mode.

```
source $VENV_PATH/bin/activate
cd $REPO_PATH
pip install -e .
```

Now you're ready to push local changes to your fork!

## Deployment

Follow these steps to deploy the application locally!

Make sure you've completed the steps above on how to start development.

Serve the application on localhost with the following, where $CONFIG_NAME is development.ini or production.ini.

```
$REPO_PATH/pserve $CONFIG_NAME --reload
```

Then go to the localhost port that the application is bound to in order to see the site.

Changes made to the repo should reload on page refresh.


## Merge Strategy (Needs to be discussed)

1. Fork repo
2. Clone to local 
3. Create Branch from develop
    * feature-$name
    * hotfix-$name
    * ISSUE-$number
4. Commit local changes to branch
5. Push changes to remote branch
6. Make PR to develop

