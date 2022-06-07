### Purpose
This script is originally meant for 8 TV Screens in a NOC (around 75" in size w/ 4k resolution).
When ran it will open 8 Chrome Windows and 2 VLC players. Then one-by-one go to the site, authenticate, then resize and reposition itself.
Monitor 3 is Slack which you would need to download the Desktop app. You just need to manually open the desktop app and leave it there.
Also please note for Slack it was made with Okta SSO in mind and required a DUO push notification.
Most of the monitors have element checks and if they fail the script will try again 3 more times.

In order for this script to work you would need to fulfill the following prerequisites.

#### Prerequisites:
1. Need to have python 3.7 or higher installed
2. Chrome browser installed
3. Need to have the chromedriver (mac or windows). It's included here anyways.
4. Need PyCharm CE to test/run the script.
5. Need to have pip, selenium, PyAutoIT, tryagain packages installed in PyCharm CE.
6. Please create a noc_local_config.py file with the appropriate credentials as this is being called in the script. You can use config.py as a template.

#### To Run:
1. Run the noc_monitor.py script in PyCharm CE.
2. Keep an eye on the console to see which monitor it is opening next and if there are any errors.
3. If the screens fail to launch properly, please rerun the script again and it will automatically kill all existing Windows.

#### Setting up as a task in Windows
1. In task scheduler create a task call "noc_monitor_script" and in the command you would have to have powershell invoke the noc_monitor.py script.
2. If the screens fail to launch properly (like if you get an error like this: c:\users\micnguyen\appdata\local\temp\scoped_dir9136_14191374\internal 
Manifest file is missing or unreadable, please rerun the task again and it will close all existing Chrome and VLC windows and re-open again.
3. If there's still issues like windows are not loading correctly, etc..maybe there are Windows Updates that need to be applied and the machine 
needs to be restarted. Alternatively you can open up PyCharm CE and run the noc_monitor.py script or make changes and test there.
4. Sometimes the chromedriver may not work because it's an older version. Please download the latest chromedriver here: https://chromedriver.chromium.org/downloads

### Author
Michael Nguyen 

https://github.com/micnguyen266


