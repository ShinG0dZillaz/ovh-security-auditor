import ovh
import json

client = ovh.Client()

print("*" * 50)
print("OVHcloud Security Audit Tool")
print("*" * 50)

# Get account info
me = client.get('/me')
print(f"\nAccount: {me.get('firstname', '')} {me.get('nichandle', '')} ({me.get('email', '')})")

# Get all IPs
print("\n[*] Fetching IP addresses...")
ips = client.get('/ip')

findings = []

for ip_block in ips:
    print(f"\n  Checking: {ip_block}")
    
    try:
        # Check firewall status
        firewall = client.get(f'/ip/{ip_block.replace("/", "%2F")}/firewall')
        
        if not firewall:
            findings.append({
                "ip": ip_block,
                "issue": "No firewall rules configured",
                "severity": "HIGH",
                "recommendation": "Configure at least one firewall rule to restrict unauthorized access"
            })
            print(f"    [HIGH] No firewall rules found")
        else:
            print(f"    [OK] {len(firewall)} firewall rule(s) found")
            
    except Exception as e:
        print(f"    [INFO] Could not check firewall: {e}")

# Print findings
print("\n" + "=" * 50)
print("FINDINGS REPORT")
print("=" * 50)

if findings:
    for f in findings:
        print(f"\n  IP: {f['ip']}")
        print(f"  Severity: {f['severity']}")
        print(f"  Issue: {f['issue']}")
        print(f"  Fix: {f['recommendation']}")
else:
    print("\n  No critical misconfigurations found.")

print("\nAudit complete.")
