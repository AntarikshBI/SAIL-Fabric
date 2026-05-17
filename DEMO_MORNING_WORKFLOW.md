# SAIL Demo - Morning Workflow (May 18, 2026)

## Status: PBIP file is properly built and ready to open

Your repo now has a clean PBIP project that matches Microsoft's official sample format. All 8 metadata JSON files validate correctly.

```
SAIL-Fabric/
├── SAIL_Dashboard.pbip                    <-- Double-click to open in Power BI Desktop
├── SAIL_Dashboard.Report/
│   ├── definition.pbir                    (points to semantic model)
│   ├── .platform                          (Fabric Git metadata)
│   ├── report.json                        (empty page + SAIL dark theme)
│   └── StaticResources/RegisteredResources/SAIL-Dark-Theme.json
└── SAIL_Dashboard.SemanticModel/
    ├── definition.pbism
    ├── .platform
    └── model.bim                          (10 measures pre-built, needs SQL endpoint)
```

---

## STEP 1: Get the Gold Lakehouse SQL Endpoint (2 min)

1. Open: https://app.fabric.microsoft.com/groups/5964ac59-2715-4b7a-910e-c5d2dcb82a77
2. Click **Gold__lh** lakehouse
3. Top-right corner: dropdown next to "Lakehouse" -> Click **SQL analytics endpoint**
4. Click **Settings** (gear icon) at top -> **SQL endpoint**
5. Copy the value labeled **SQL connection string** (looks like `abc123xyz.datawarehouse.fabric.microsoft.com`)

---

## STEP 2: Open the PBIP in Power BI Desktop (1 min)

1. In File Explorer, navigate to `C:\Users\ashahwal\SAIL-Fabric\`
2. **Double-click `SAIL_Dashboard.pbip`**
3. Power BI Desktop opens. If it shows a preview-feature prompt, enable it.

---

## STEP 3: Set the SQL Endpoint Parameter (2 min)

1. **Home ribbon** -> **Transform data** -> **Edit parameters**
2. Find parameter **SQLEndpoint**
3. Replace placeholder text with the SQL connection string you copied
4. Click **OK**
5. **Home ribbon** -> **Refresh** (or "Apply changes" yellow banner if shown)
6. Data loads from Gold__lh - `agg_plant_daily_summary` table appears in Data pane (right side)

---

## STEP 4: Build the Overview Page (15 min)

The page is empty with the SAIL dark theme already applied. You will see all 10 pre-built measures in the Data pane under `agg_plant_daily_summary` -> fx Measures:
- Total Hot Metal, Target Hot Metal
- Total Crude Steel, Target Crude Steel
- Total Saleable Steel, Target Saleable Steel
- Achievement %
- Hot Metal Achievement %
- Crude Steel Achievement %
- Saleable Steel Achievement %

### Visual 1: KPI Card - Total Hot Metal
- Click blank canvas -> click **Card** icon in Visualizations pane
- Drag measure **Total Hot Metal** to Fields
- Resize small, place top-left

### Visual 2: KPI Card - Total Crude Steel
- Click blank -> Card icon
- Drag measure **Total Crude Steel** to Fields
- Place next to Card 1

### Visual 3: KPI Card - Achievement %
- Click blank -> Card icon
- Drag measure **Achievement %** to Fields
- Place next to Card 2

### Visual 4: Bar Chart - Hot Metal by Plant
- Click blank -> **Clustered Bar Chart** icon
- Y-axis: drag column `plant_name`
- X-axis: drag measure `Total Hot Metal`
- Resize big, place middle of canvas

### Visual 5: Table - Plant Performance
- Click blank -> **Table** icon
- Columns (in order): `plant_name`, `Total Hot Metal`, `Target Hot Metal`, `Achievement %`
- Place at bottom

### Visual 6 (optional): Title text box
- **Insert** ribbon -> **Text box**
- Type: `SAIL Daily Operations Dashboard`
- Font 28, Bold, color orange (#e87a20)

---

## STEP 5: Publish to Fabric (3 min)

1. **Home ribbon** -> **Publish**
2. Save prompts: keep defaults, save under `C:\Users\ashahwal\SAIL-Fabric\`
3. Sign in if prompted
4. Choose **SAIL** workspace -> Click **Select**
5. Wait 30 sec for "Success" dialog
6. Click the URL link to open in browser

---

## Demo Script (5 min for customer)

**Opening:** "This is SAIL's daily operations dashboard, connected directly to our Gold lakehouse in Microsoft Fabric. The data flows from raw plant Excel uploads through Bronze and Silver layers into Gold, where it's aggregated for executive reporting."

**KPI Cards:** "At a glance we see total hot metal, crude steel output, and overall achievement against daily targets across all 5 plants."

**Bar Chart:** "Production breakdown by plant - we can see which plants are performing well and which need attention today."

**Table:** "Detailed actuals vs targets per plant. This drives the daily review meeting."

**Pipeline talking point:** "Reports auto-refresh as new plant data lands. The same Fabric workspace also hosts the lakehouse, notebooks for ETL, and Git integration for CI/CD - everything in one platform."

**If asked about the .jsx prototype:** "That was our self-service file-upload prototype for plants without direct system integration. This Power BI report is the production reporting layer."

---

## Emergency Plan B (if PBIP still has issues)

1. Open Power BI Desktop normally (don't open the .pbip)
2. **Home -> Get Data -> OneLake data hub**
3. Browse SAIL workspace -> Gold__lh -> Connect
4. Select tables -> Load
5. **View -> Themes -> Browse for themes ->** select `C:\Users\ashahwal\SAIL-Fabric\SAIL_Dashboard.Report\StaticResources\RegisteredResources\SAIL-Dark-Theme.json`
6. Build the 5 visuals as above (no measures pre-built, so use SUM directly on `total_hot_metal` etc.)
7. Publish to SAIL workspace

---

## Why This Time Works (vs. last night's attempts)

The previous PBIP files were missing the required `definition.pbir` file and used a non-standard folder name (`SAIL_CEO_Dashboard_Report` instead of `<Name>.Report`). This rebuild:

- Top-level `.pbip` matches Microsoft's `Sales.pbip` sample byte-for-byte in structure
- Report folder has the REQUIRED `definition.pbir` pointing at the semantic model
- Semantic model folder has `definition.pbism` per the schema
- `.platform` files registered for Fabric Git integration  
- `model.bim` uses standard compatibility level 1550 with parameter-driven SQL endpoint

Schemas verified against:
- https://github.com/microsoft/json-schemas/tree/main/fabric/pbip
- https://github.com/microsoft/Analysis-Services/tree/master/pbidevmode/fabricps-pbip/SamplePBIP
