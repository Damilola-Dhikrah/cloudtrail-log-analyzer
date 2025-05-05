import json

# Step 1: Load the CloudTrail log file
with open("cloudtrail_sample.json", "r") as file:
    logs = json.load(file)

print("✅ Log file loaded. Total events:", len(logs))

# Step 2: Analyze each event
for event in logs:
    event_name = event["eventName"]
    user = event["userIdentity"]["userName"]
    time = event["eventTime"]
    ip = event["sourceIPAddress"]

    # Detect failed logins
    if event_name == "ConsoleLogin":
        if event["responseElements"]["ConsoleLogin"] == "Failure":
            print("\n❌ Failed Login Detected!")
            print(f"User: {user}, IP: {ip}, Time: {time}")

    # Detect IAM changes
    if event_name == "CreateUser" or event_name == "AttachUserPolicy":
        print("\n🚨 IAM Change Detected!")
        print(f"Event: {event_name}, Performed by: {user}")
        print(f"Target User: {event['requestParameters']['userName']}")
        print(f"Time: {time}, IP: {ip}")
#Added CloudTrail analyzer script
