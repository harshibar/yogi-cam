#!/usr/bin/env python3
import subprocess
import time

print("Testing camera access...")

try:
    # Simple photo test
    result = subprocess.run([
        "libcamera-jpeg",
        "--camera", "0",
        "--width", "640",
        "--height", "480",
        "--timeout", "2000",
        "--output", "test_photo.jpg"
    ], capture_output=True, text=True, timeout=10)
    
    if result.returncode == 0:
        print("✅ SUCCESS: Photo taken!")
        print("✅ File: test_photo.jpg created")
    else:
        print("❌ FAILED to take photo")
        print("Error:", result.stderr)
        
except subprocess.TimeoutExpired:
    print("❌ TIMEOUT: Camera took too long")
except Exception as e:
    print(f"❌ ERROR: {e}")

print("\nTest complete.")
