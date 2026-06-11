from datetime import datetime
import os

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    
    if not data:
        print("Warning: Empty data list provided")
        return None
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    test_logs = [
        "User logged in",
        "User updated profile", 
        "Report exported",
        "Session ended"
    ]
    
    print("Testing generate_log function...")
    result = generate_log(test_logs)
    print(f"File created: {result}")