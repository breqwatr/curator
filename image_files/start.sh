echo "$(date) Applying environment variables"
/env_config.py

cron && tail -f /dev/null
