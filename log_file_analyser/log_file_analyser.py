import re
from collections import Counter
from datetime import datetime

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()

        # Extract timestamps, IPs, and errors
        timestamps = []
        ip_addresses = []
        error_messages = []

        for line in logs:
            # Match common log timestamp formats
            timestamp_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
            if timestamp_match:
                timestamps.append(datetime.strptime(timestamp_match.group(), '%Y-%m-%d %H:%M:%S'))

            # Match IPv4 addresses
            ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if ip_match:
                ip_addresses.append(ip_match.group())

            # Match error keywords
            if "ERROR" in line or "FAIL" in line or "CRITICAL" in line:
                error_messages.append(line.strip())

        # Summarize data
        print("\n--- Log Analysis Report ---")
        print(f"Total Lines: {len(logs)}")
        print(f"Total Timestamps Found: {len(timestamps)}")
        print(f"Total Unique IPs: {len(set(ip_addresses))}")
        print(f"Total Errors Found: {len(error_messages)}")

        print("\nMost Common IPs:")
        for ip, count in Counter(ip_addresses).most_common(5):
            print(f"{ip}: {count} occurrences")

        print("\nError Messages:")
        for error in error_messages[:10]:
            print(f"- {error}")

        # Save summary to a report file
        with open("log_analysis_report.txt", "w") as report:
            report.write("--- Log Analysis Report ---\n")
            report.write(f"Total Lines: {len(logs)}\n")
            report.write(f"Total Timestamps Found: {len(timestamps)}\n")
            report.write(f"Total Unique IPs: {len(set(ip_addresses))}\n")
            report.write(f"Total Errors Found: {len(error_messages)}\n\n")
            report.write("Most Common IPs:\n")
            for ip, count in Counter(ip_addresses).most_common(5):
                report.write(f"{ip}: {count} occurrences\n")
            report.write("\nError Messages:\n")
            for error in error_messages:
                report.write(f"- {error}\n")

        print("\nLog analysis complete! Report saved to 'log_analysis_report.txt'.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Log File Analyzer!")
    log_file = input("Enter the path to your log file: ")
    analyze_log(log_file)
