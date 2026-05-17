# SAIL Dashboard - Quick Setup Script for 11 AM Demo
# Run this at 9:30 AM tomorrow - takes 5 minutes total

import os
import subprocess

print("🚀 SAIL Dashboard Quick Deploy")
print("=" * 50)

# Step 1: Open Power BI Desktop with the PBIR
pbir_path = r"C:\Users\ashahwal\SAIL-Fabric\SAIL_CEO_Dashboard_Report\report.json"
print("\n1️⃣  Opening Power BI Desktop...")
print(f"   File: {pbir_path}")

try:
    # Try Windows Store version first
    subprocess.run([
        "powershell", 
        "-Command", 
        f"Start-Process 'shell:AppsFolder\\Microsoft.MicrosoftPowerBIDesktop_8wekyb3d8bbwe!Microsoft.MicrosoftPowerBIDesktop' -ArgumentList '{pbir_path}'"
    ])
    print("   ✅ Power BI Desktop launched")
except:
    print("   ⚠️  Manual step: Open Power BI Desktop and load the report")

print("\n" + "=" * 50)
print("📋 MANUAL STEPS (3 minutes):")
print("=" * 50)
print("""
Once Power BI Desktop opens:

🔧 Fix the Connection:
1. If you see data refresh error, click "Edit Queries"
2. In Power Query, right-click the query → "Advanced Editor"
3. Replace <LAKEHOUSE_SQL_ENDPOINT> with your actual Gold__lh SQL endpoint:
   - Get it from: Fabric portal → Gold__lh → Copy SQL endpoint
   
📊 Add Quick Visuals (drag & drop - 2 minutes):
1. Select "agg_plant_daily_summary" table
2. Drag these fields to canvas:
   - plant_name → Axis
   - Total Hot Metal → Values  
   → This creates a bar chart
   
3. Add 3 Cards (click Card icon):
   - Drag "Total Hot Metal" → Card 1
   - Drag "Total Crude Steel" → Card 2  
   - Drag "Achievement %" → Card 3

4. Arrange them nicely on the canvas

🚀 Publish:
1. File → Publish
2. Select "SAIL" workspace
3. Click "Select"
4. Wait 30 seconds → DONE!

Your demo is ready by 10:00 AM!
""")

print("=" * 50)
print("💤 NOW GO TO BED!")
print("Set alarm for 9:15 AM - you'll be ready by 10:00 AM")
print("=" * 50)
