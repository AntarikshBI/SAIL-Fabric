# 🚨 DEMO DAY - SIMPLE 30-MIN WORKFLOW

## Forget the broken PBIP files. Here's what actually works:

---

## **Step 1: Open Power BI Desktop** (1 min)

1. Windows Key → Type "Power BI" → Open Power BI Desktop
2. Click **"Blank report"** if welcome screen appears

---

## **Step 2: Connect to Gold Lakehouse** (5 min)

1. **Home ribbon** → **Get Data** → **OneLake data hub**

2. Browse to: **SAIL** workspace → **Gold__lh** lakehouse

3. Click **Connect**

4. **Select tables** (checkboxes):
   - ✅ agg_plant_daily_summary
   - ✅ dim_plant  
   - ✅ fact_production

5. Click **"Load"** (NOT Transform)

6. Wait 30 seconds for data to load

---

## **Step 3: Apply Dark Theme** (1 min)

1. **View** ribbon → **Themes** → **Browse for themes**

2. Navigate to: `C:\Users\ashahwal\SAIL-Fabric\SAIL_CEO_Dashboard_Report\StaticResources\RegisteredResources`

3. Select **`SAIL-Dark-Theme.json`** → Click **Open**

4. Report now has SAIL colors

---

## **Step 4: Build 5 Visuals** (15 min)

### **Card 1: Total Hot Metal**
- Click blank canvas → Click **Card** icon in Visualizations pane
- From Data pane → drag `agg_plant_daily_summary[total_hot_metal]` to Fields
- Resize small, place top-left

### **Card 2: Total Crude Steel**
- Click blank → Card icon
- Drag `total_crude_steel` → Fields
- Place next to Card 1

### **Card 3: Achievement %**
- Click blank → Card icon
- Drag `overall_achievement_pct` → Fields
- Right-click field → change to **Average**

### **Bar Chart: Production by Plant**
- Click blank → **Clustered Bar Chart** icon
- Drag `plant_name` → **Y-axis**
- Drag `total_hot_metal` → **X-axis**
- Make it big (middle of canvas)

### **Table: Plant Performance**
- Click blank → **Table** icon
- Drag these to Columns:
  - `plant_name`
  - `total_hot_metal`
  - `target_hot_metal`
  - `overall_achievement_pct`

---

## **Step 5: Add Title** (1 min)

- **Insert** ribbon → **Text box**
- Click top of canvas
- Type: **"SAIL Daily Operations Dashboard"**
- Font size 28, Bold, Orange color

---

## **Step 6: Publish** (3 min)

1. **Home** ribbon → **Publish** button (top right)

2. **Save first** - it asks to save:
   - Location: `C:\Users\ashahwal\SAIL-Fabric\`
   - File name: `SAIL_Dashboard.pbix`
   - Save

3. Sign in if prompted

4. Select destination: **SAIL** workspace

5. Click **Select**

6. Wait 30 sec → "Success!" 

7. Click link → opens in browser

---

## ✅ **DONE - Ready for 11 AM Demo**

---

## 🎬 **Demo Script (5 min):**

**Opening:**
"This is SAIL's daily operations dashboard - real-time view across all 5 plants."

**KPI Cards:**
"At a glance: total hot metal, crude steel output, and overall target achievement."

**Bar Chart:**
"Production breakdown by plant - Bhilai is performing best."

**Table:**
"Detailed actuals vs targets - this drives daily review meetings."

**Data Pipeline:**
"Data flows: Bronze (raw Excel from plants) → Silver (cleaned) → Gold (aggregated). Dashboard auto-refreshes."

**If asked about .jsx app:**
"That's our prototype for plant-level file uploads. This Power BI is production."

---

## 🆘 **Emergency Plan B:**

If Power BI Desktop has issues, just show the **Fabric workspace** directly:
1. Open: https://app.fabric.microsoft.com/groups/5964ac59-2715-4b7a-910e-c5d2dcb82a77
2. Show **Gold__lh** with the tables
3. Click `agg_plant_daily_summary` → show data preview
4. "Our data warehouse is consolidating production data from all plants"

Still demonstrates value.

---

## 💤 **GO SLEEP. Alarm 9:15 AM.**

Trust the process. This will work tomorrow.
