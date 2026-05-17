# SAIL Dashboard - Demo Day Workflow
## ⏰ Start at 9:30 AM - Done by 10:30 AM

---

## 🎯 Goal
Create a professional Power BI dashboard matching your .jsx design:
- Dark theme with orange/green colors
- Overview page with KPI cards
- Production metrics by plant
- All connected to Gold lakehouse data

---

## 📋 STEP-BY-STEP (Follow blindly)

### **STEP 1: Get SQL Endpoint (2 minutes)**

1. Open browser: https://app.fabric.microsoft.com/groups/5964ac59-2715-4b7a-910e-c5d2dcb82a77

2. Click on **Gold__lh** lakehouse

3. Top-right corner → Click **"SQL analytics endpoint"** icon

4. You'll see a connection string like:
   ```
   xlrbqbpfn7tejbhb2miqpci-s4e2b3yl2brejd7rjb4gkpq5zy.datawarehouse.fabric.microsoft.com
   ```

5. **COPY THIS** - you need it for next step

---

### **STEP 2: Update Semantic Model (3 minutes)**

1. Open file: `C:\Users\ashahwal\SAIL-Fabric\SAIL_CEO_Dashboard_Report\definition\model.bim`

2. Press `Ctrl+F` → Search for: `<LAKEHOUSE_SQL_ENDPOINT>`

3. Replace with the SQL endpoint you copied (WITHOUT any protocol like https://)

4. Save the file (`Ctrl+S`)

---

### **STEP 3: Open in Power BI Desktop (5 minutes)**

1. **Launch Power BI Desktop:**
   - Press Windows Key
   - Type "Power BI"
   - Open "Power BI Desktop"

2. **Open the report:**
   - File → Open Report → Browse
   - Navigate to: `C:\Users\ashahwal\SAIL-Fabric\SAIL_CEO_Dashboard_Report`
   - Select: `report.json`
   - Click Open

3. **If you see connection errors:**
   - Click "Edit Queries"
   - Click "Advanced Editor"
   - Verify the SQL endpoint is correct
   - Click "Close & Apply"

---

### **STEP 4: Create Overview Page (20 minutes)**

#### **A. Add KPI Cards (5 min)**

1. Select **"Visualizations" pane** (right side)
2. Click **"Card"** icon (looks like a card with number)
3. From **"Data" pane**, expand `agg_plant_daily_summary`
4. Drag **"Total Hot Metal"** measure to the card
5. Resize and position in top-left

**Repeat 3 more times for:**
- Total Crude Steel
- Total Saleable Steel  
- Achievement %

**Arrange cards horizontally across the top**

#### **B. Add Bar Chart (8 min)**

1. Click blank area on canvas
2. Select **"Clustered Bar Chart"** from Visualizations
3. Drag fields:
   - **plant_name** → Axis
   - **Total Hot Metal** → Values
   - **Target Hot Metal** → Values (adds comparison)

4. **Style it:**
   - Format pane → Data colors → Pick orange (#e87a20) for actual
   - Data labels → On
   - Title → "Hot Metal Production by Plant"

#### **C. Add Table (7 min)**

1. Click blank area
2. Select **"Table"** visualization
3. Drag these columns:
   - plant_name
   - Total Hot Metal
   - Target Hot Metal  
   - Hot Metal Achievement %

4. **Format:**
   - Format pane → Grid → Alternate row colors
   - Text size → 11

---

### **STEP 5: Apply Dark Theme (5 minutes)**

1. **View** ribbon → **Themes** → **Browse for themes**

2. Navigate to: `C:\Users\ashahwal\SAIL-Fabric\SAIL_CEO_Dashboard_Report\StaticResources\RegisteredResources`

3. Select: `SAIL-Dark-Theme.json`

4. Click **Open**

✅ Your entire report now has the dark theme with orange/green colors!

---

### **STEP 6: Add More Pages (Optional - 10 min)**

**If you have time, duplicate the page:**

1. Right-click on "Overview" page tab (bottom)
2. Select "Duplicate Page"
3. Rename to "Production Details"
4. Change the chart to show different metrics (crude steel, saleable steel)

---

### **STEP 7: Publish to Fabric (3 minutes)**

1. **File** → **Publish** → **Publish to Power BI**

2. Sign in (if prompted)

3. Select destination: **SAIL** workspace

4. Click **"Select"**

5. Wait for upload (~30 seconds)

6. ✅ **"Success!"** dialog appears

7. Click **"Open 'SAIL_CEO_Dashboard' in Power BI"** → Opens in browser

---

## ✅ YOU'RE DONE!

**Your dashboard is now live in Fabric workspace.**

Share link with customer:
```
https://app.fabric.microsoft.com/groups/5964ac59-2715-4b7a-910e-c5d2dcb82a77/reports/<report-id>
```

---

## 🎬 Demo Tips (11 AM)

### **What to show:**

1. **"This is our real-time steel plant operations dashboard"**
   - Show the Overview page
   - Point out the KPI cards (Total Hot Metal, Crude Steel, etc.)

2. **"It's connected directly to our Gold lakehouse"**
   - Open Fabric in another tab
   - Show Gold__lh with the tables
   - "All this data flows automatically through our data pipeline"

3. **"We can filter by any plant"**
   - Use the plant_name slicer (if you added one)
   - Or just click on bars in the chart to filter

4. **"The dark theme matches our company branding"**
   - Show the professional SAIL styling

### **If customer asks about the .jsx web app:**
- "That's our proof-of-concept for Excel file uploads"
- "This Power BI version is the production system connected to live data"
- "We can deploy the web version too if they prefer file-based reporting"

---

## 🆘 Emergency Fallback

**If something breaks:**

1. **Open this URL:** https://app.fabric.microsoft.com/groups/5964ac59-2715-4b7a-910e-c5d2dcb82a77

2. Click **"+ New"** → **"Report"**

3. Select **Gold__lh** as data source

4. Drag fields to create ONE simple visual (bar chart with plant_name and Total Hot Metal)

5. Show this - it proves the data pipeline works

Better to have ONE working visual than a broken complex report.

---

## 💤 NOW GO TO SLEEP

Set alarm: **9:15 AM**

You have everything you need. Tomorrow morning, follow this doc step by step.

**You've got this.** 🚀
