# OVHcloud Security Audit Tool

A Python tool that uses the OVHcloud API to detect firewall 
misconfigurations across your cloud infrastructure.

## What It Does
- Authenticates to the OVHcloud API
- Inventories all IP addresses on the account
- Checks each IP for missing or incomplete firewall rules
- Outputs a prioritized findings report with remediation steps

## Why This Matters
Misconfigured firewalls are one of the most common causes of 
cloud breaches. OVHcloud's Edge Network Firewall supports up to 
20 rules per IP but only if they are actually configured. 
This tool flags IPs where that protection is absent.

## Setup
1. Clone this repo
2. Install dependencies: pip install ovh
3. Create ovh.conf with your API credentials (see ovh.conf.example)
4. Run: py audit.py

## Example Output
<img width="787" height="490" alt="python script output" src="https://github.com/user-attachments/assets/35637319-2285-4b7a-94c1-11d087372595" />

## Troubleshooting — Errors I Hit as an Entry-Level Developer

These were all simple fixes in hindsight. I'm documenting them 
because they're common beginner roadblocks that are easy to 
overthink.

### 1. "python is not recognized as an internal or external command"
Python was installed but Windows was intercepting the command 
with a Microsoft Store shortcut instead of the real executable.

Fix: Go to Settings > Apps > Advanced app settings > 
App execution aliases and disable both python.exe and python3.exe. 
Close and reopen your terminal.

### 2. "No module named ovh"
The ovh module wasn't being found because the code was running 
in the wrong environment. I was also originally writing code in 
Thonny instead of saving it as a proper .py file.

Fix: Write the code in Notepad, save it as audit.py, navigate 
to the folder in Command Prompt, and run it with:
py audit.py (instead of python audit.py)

### 3. "KeyError: lastname"
The script crashed trying to read a lastname field that 
OVHcloud doesn't store for all account types. I overthought 
this one — the fix was one line.

Fix: Replace square bracket lookups with .get() which returns 
an empty string instead of crashing when a field is missing. 
Also replaced lastname with nichandle, which is OVHcloud's 
internal account ID field.

Before:
me['lastname']

After:
me.get('nichandle', '')

### 4. "git is not recognized as an internal or external command"
Git was installed but not added to the system PATH, so 
Windows couldn't find it. Same root cause as the Python issue.

Fix: Search "Edit the system environment variables" in the 
Start menu, open Environment Variables, find Path under User 
variables, click Edit, and add:
C:\Program Files\Git\bin

Close and reopen your terminal.

## Skills Demonstrated
- OVHcloud API authentication and usage
- Python scripting for security automation
- Cloud infrastructure auditing
- Remediation reporting
- Real-world debugging and documentation

## Author
[Your name] | [Your LinkedIn URL]
