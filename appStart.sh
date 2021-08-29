source config.env
#cd $APP_PATH; 

# Run in background
#flask run --cert=adhoc --host=$LOCAL_IP >/dev/null &
#flask run --cert=adhoc --host=$REMOTE_IP >/dev/null &

# Show output
flask run --cert=adhoc --host=$LOCAL_IP