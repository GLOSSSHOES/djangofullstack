# Set Heroku app name (replace with your actual app name)
```
HEROKU_APP_NAME="glossshoes"
DATBASE_TYPE="mini"
```

# Filter Postgres add-ons (using grep)
```
heroku apps:destroy --app $HEROKU_APP_NAME
echo "All Postgres add-ons removed (if successful)"
```

# Set the commands (modify if needed)
```
heroku create $HEROKU_APP_NAME
heroku config:set DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY -a $HEROKU_APP_NAME
heroku config:set DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE -a $HEROKU_APP_NAME
heroku config:set AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -a $HEROKU_APP_NAME
heroku config:set AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -a $HEROKU_APP_NAME
heroku config:set AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME -a $HEROKU_APP_NAME
heroku stack:set container -a $HEROKU_APP_NAME
heroku addons:create heroku-postgresql:mini -a $HEROKU_APP_NAME
heroku git:remote -a $HEROKU_APP_NAME
git push heroku master:main
```