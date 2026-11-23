import re
from datetime import datetime
from collections import Counter, defaultdict

# STEP 1: Read the log file
log_entries = []

with open("application.log", "r") as file:
    for line in file:
        line = line.strip()

        if line:
            log_entries.append(line)

print("Total log lines:", len(log_entries))


# STEP 2: Create regex pattern
pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARN|ERROR) (.+)$"


# STEP 3: Create counters and defaultdict
level_count = Counter()
hour_count = Counter()
error_count = Counter()
logs_by_level = defaultdict(list)

parsed_entries = []


# STEP 4: Parse every log entry
for line in log_entries:

    match = re.match(pattern, line)

    if match:
        timestamp_str, level, message = match.groups()

        # Convert string into datetime object
        timestamp = datetime.strptime(
            timestamp_str, "%Y-%m-%d %H:%M:%S"
        )

        # Store parsed information
        record = {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }

        parsed_entries.append(record)

        # STEP 5: Count log levels
        level_count[level] += 1

        # STEP 6: Count entries per hour
        hour_count[timestamp.hour] += 1

        # STEP 7: Count repeated ERROR messages
        if level == "ERROR":
            error_count[message] += 1

        # STEP 8: Group logs by level
        logs_by_level[level].append(record)


# STEP 9: Display total entries per level
print("\n--- LOG LEVEL SUMMARY ---")

for level, count in level_count.items():
    print(level, ":", count)


# STEP 10: Find busiest hour
print("\n--- BUSIEST HOUR ---")

if hour_count:
    busiest_hour, busiest_count = hour_count.most_common(1)[0]

    print(f"Busiest hour: {busiest_hour:02d}:00")
    print("Total entries:", busiest_count)


# STEP 11: Find most repeated ERROR message
print("\n--- MOST REPEATED ERROR ---")

if error_count:
    message, count = error_count.most_common(1)[0]

    print("Error message:", message)
    print("Occurrences:", count)
else:
    print("No ERROR entries found.")


# STEP 12: Display logs grouped by level
print("\n--- LOGS GROUPED BY LEVEL ---")

for level, records in logs_by_level.items():

    print(f"\n{level}:")

    for record in records:
        print(record["timestamp"], "-", record["message"])


# STEP 13: Validate parsing
print("\n--- VALIDATION ---")

print("Total lines:", len(log_entries))
print("Successfully parsed:", len(parsed_entries))
print("Unparsed lines:", len(log_entries) - len(parsed_entries))
