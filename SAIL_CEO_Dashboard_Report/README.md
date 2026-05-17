# SAIL CEO Dashboard Power BI Report

## 📊 Overview
Comprehensive daily operations dashboard for Steel Authority of India steel plants matching the React JSX design.

## 🎯 Features
- **7 Dashboard Pages:**
  - Overview: KPI cards, production vs target charts, achievement metrics
  - Production: Blast furnaces, SMS, sinter plants, coke ovens tables
  - Mills: Rolling mill performance table
  - Raw Materials: Stock position cards
  - Despatch: Loading KPIs and product-wise table
  - Energy: Power generation KPIs and sources table
  - Delays: Delay cards and detailed issue tracking

- **Data Model:**
  - Connected to Gold lakehouse tables (fact_production, dim_plant, dim_date, fact_delays)
  - 15+ DAX measures for KPIs
  - Relationships configured
  - Filters and slicers for plant/date selection

- **Dark Theme:**
  - SAIL corporate colors (#e87a20 orange, #1db954 green, #e84040 red)
  - Dark background (#080c14)
  - Professional typography (DM Sans, JetBrains Mono)

## 📦 Report Structure
```
SAIL_CEO_Dashboard_Report/
├── .pbi/
│   └── localSettings.json          # Report metadata
├── definition/
│   ├── model.tmdl                  # Data model + DAX measures
│   └── pages/
│       ├── overview.json           # Overview page visuals
│       ├── production.json         # Production units page
│       ├── mills.json              # Rolling mills page
│       ├── rawmaterials.json       # Raw materials page
│       ├── despatch.json           # Despatch & loading page
│       ├── energy.json             # Energy & utilities page
│       └── delays.json             # Delays & issues page
├── StaticResources/
│   └── RegisteredResources/
│       └── SAIL-Dark-Theme.json    # Custom theme
└── report.json                     # Main report configuration
```

## 🚀 Deployment to Microsoft Fabric

### Method 1: Upload to Fabric Workspace (Recommended)

1. **Package the report:**
   ```powershell
   # Zip the entire report folder
   Compress-Archive -Path "C:\Users\ashahwal\SAIL_CEO_Dashboard_Report\*" `
                    -DestinationPath "C:\Users\ashahwal\SAIL_CEO_Dashboard.zip" -Force
   ```

2. **Upload to Fabric:**
   - Open https://msit.powerbi.com
   - Navigate to SAIL workspace
   - Click **+ New** → **Upload** → **Upload .pbip folder**
   - Select the `SAIL_CEO_Dashboard_Report` folder
   - Wait for upload to complete

3. **Connect to Gold Lakehouse:**
   - Open the report in Fabric
   - Go to **Transform data** → **Data source settings**
   - Update connection to point to `Gold__lh` in SAIL workspace
   - Refresh the dataset

### Method 2: Open in Power BI Desktop

1. **Install Power BI Desktop** (if not already installed):
   - Download from https://powerbi.microsoft.com/desktop/

2. **Open the PBIR folder:**
   - File → Open → Browse
   - Navigate to `C:\Users\ashahwal\SAIL_CEO_Dashboard_Report`
   - Select the folder (not individual files)

3. **Configure data source:**
   - Transform data → Advanced Editor
   - Update lakehouse connection:
     ```m
     let
       Source = Lakehouse.Contents(null),
       Workspace = Source{[workspaceId="5964ac59-2715-4b7a-910e-c5d2dcb82a77"]}[Data],
       Lakehouse = Workspace{[Name="Gold__lh"]}[Data],
       Table = Lakehouse{[Name="fact_production"]}[Data]
     in
       Table
     ```

4. **Publish to Fabric:**
   - Home → Publish → Select SAIL workspace
   - Click Publish

## 🔧 Configuration

### Data Connections
The report expects these tables in `Gold__lh`:
- `fact_production` (actual/target/variance for all KPIs)
- `dim_plant` (5 plants: BSP, DSP, RSP, BSL, ISP)
- `dim_date` (date dimension)
- `fact_delays` (delay tracking)
- `agg_plant_daily_summary` (daily aggregates)

### DAX Measures
Pre-configured measures:
- `[Total Actual]`, `[Total Target]`, `[Total Variance]`
- `[Achievement %]`
- `[Hot Metal Actual]`, `[Hot Metal Target]`
- `[Crude Steel Actual]`, `[Crude Steel Target]`
- `[Saleable Steel Actual]`, `[Saleable Steel Target]`
- `[KPI Status]`, `[Status Color]`
- `[Total Delay Hours]`, `[Critical Delays]`

### Visual Formatting
All visuals use SAIL Dark Theme with:
- Background: #080c14
- Text: #e8ecf4 (primary), #8899b0 (secondary), #566880 (muted)
- KPI colors: #e87a20 (orange), #1db954 (green), #e84040 (red), #d4a017 (amber)

## 📊 Usage

### Page Navigation
- Use tabs at bottom to switch between 7 pages
- Overview: Quick KPI snapshot with achievement metrics
- Production: Detailed unit-wise production tables
- Mills: Mill performance and utilization
- Raw Materials: Stock position monitoring
- Despatch: Loading and product-wise tracking
- Energy: Power generation and consumption
- Delays: Issue tracking and downtime analysis

### Filters
- **Plant Slicer** (Overview page): Select plant (BSP/DSP/RSP/BSL/ISP)
- **Date Slicer** (Overview page): Select reporting date
- Filters apply across all pages

### KPI Cards
- Display actual values with large numbers
- Show target comparison when available
- Color-coded: Green (on target), Amber (warning), Red (below target)

### Tables
- Sortable by clicking column headers
- Total rows show aggregated values
- Color-coded status indicators

## 🎨 Customization

### Change Theme Colors
Edit `StaticResources/RegisteredResources/SAIL-Dark-Theme.json`:
```json
{
  "dataColors": ["#your-color-1", "#your-color-2", ...],
  "background": "#your-bg-color",
  "foreground": "#your-text-color"
}
```

### Add New Measures
Edit `definition/model.tmdl` in fact_production table:
```dax
measure [Your Measure Name] = 
  CALCULATE(SUM(fact_production[actual]), <filter>)
  formatString: #,##0
```

### Add Visuals
Edit page JSON files in `definition/pages/`:
- Add new visual container with x/y/z/width/height
- Configure visualType (card/tableEx/clusteredBarChart/etc.)
- Set projections to bind data fields

## ✅ Validation Checklist

After deployment:
- [ ] All 7 pages load without errors
- [ ] Plant slicer filters all visuals
- [ ] Date slicer works correctly
- [ ] KPI cards show actual numbers from fact_production
- [ ] Tables display data from Gold lakehouse
- [ ] Theme colors match SAIL branding
- [ ] Total rows calculate correctly
- [ ] Achievement % displays with correct formatting

## 🐛 Troubleshooting

**Issue: "Can't connect to data source"**
- Solution: Update lakehouse connection in data source settings
- Verify SAIL workspace ID: `5964ac59-2715-4b7a-910e-c5d2dcb82a77`
- Confirm Gold__lh exists in workspace

**Issue: "Table not found"**
- Solution: Verify table names match Gold lakehouse
- Run pipeline to populate Gold tables if empty

**Issue: "Visuals not displaying"**
- Solution: Check data model relationships
- Refresh dataset
- Verify measures calculate without errors

**Issue: "Theme not applied"**
- Solution: Re-import theme from StaticResources
- Apply theme manually: View → Themes → Browse for theme

## 📝 Notes

- Report uses PBIR format (Power BI Report Item) - native Fabric format
- Compatible with Power BI Desktop (Jan 2024+) and Fabric
- Auto-refresh on data pipeline completion (configure in Fabric settings)
- Supports drill-through from summary to detail pages (configure per need)

## 🔗 Related Resources
- Pipeline: `SAIL_Production_Pipeline` (orchestrates data ETL)
- Lakehouses: Bronze__lh, Silver__lh, Gold__lh
- Notebooks: 01_Configuration through 07_Semantic_Model

---

**Report Version:** 1.0  
**Last Updated:** May 18, 2026  
**Data Source:** SAIL Gold Lakehouse (fact_production, dim_plant, dim_date, fact_delays)
