# config_template.py is a template for passing credentials in noc_monitor.py
# A new config file will need to be saved locally as noc_local_config.py with the actual credentials as it will be ignored in .gitignore
# This way when pushing the changes to Git the credentials should not be saved there for security reasons.
# The script should only pull the credentials locally.

metricly_username = "your-email"
metricly_password = "email-pass"

alertsite_username = "your-email"
alertsite_password = "email-pass"

slack_username = "your-email"
slack_password = "email-pass"