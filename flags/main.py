import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if "critical" in line:
            line = f"🟣 CRITICAL: {line}"
        if "high" in line:
            line = f"🔴 HIGH: {line}"
        if "medium" in line:
            line = f"🟠 MEDIUM: {line}"
        if "low" in line:
            line = f"🟢 LOW: {line}"
        if "info" in line:
            line = f"🔵 INFO: {line}"
        if "unknown" in line:
            line = f"⚪ UNKNOWN: {line}"
        
        print(line)

if __name__ == '__main__':
    main()
