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
This tool flags IPs where that protection is absent. This also works for other CSP’s. 

## Setup
1. Clone this repo
2. Install dependencies: pip install ovh
3. Create ovh.conf with your API credentials (see ovh.conf.example)
4. Run: python audit.py

## Example Output
[paste a screenshot of your terminal output here]

## Skills Demonstrated
- OVHcloud API authentication and usage
- Python scripting for security automation
- Cloud infrastructure auditing
- Remediation reporting

## Author
Aubree Herron | https://www.linkedin.com/in/aherronprofie3/
