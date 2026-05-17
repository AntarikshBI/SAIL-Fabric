# SAIL Operations Dashboard

Microsoft Fabric workspace for SAIL steel plant daily operations reporting.

## 🏗️ Structure

- **SAIL_CEO_Dashboard_Report/** - Power BI Report Item (PBIR) with CEO-level operations dashboard
  - 7 report pages (Overview, Production, Mills, Raw Materials, Despatch, Energy, Delays)
  - Custom dark theme
  - Connected to Gold lakehouse tables

## 📊 Data Architecture

**Bronze Layer** → Raw Excel files from daily plant operations
**Silver Layer** → Harmonized production data across 5 plants
**Gold Layer** → Star schema for Power BI (dims + facts + aggregates)

### Gold Tables Used in Report:
- `fact_production` - Daily production KPIs by plant
- `dim_plant` - 5 SAIL plants (BSP, DSP, RSP, BSL, ISP)
- `dim_date` - Date dimension
- `fact_delays` - Production delays and issues
- `agg_plant_daily_summary` - Pre-aggregated plant metrics

## 🚀 Deployment

### Prerequisites
- Microsoft Fabric workspace: **SAIL** (ID: `5964ac59-2715-4b7a-910e-c5d2dcb82a77`)
- Gold lakehouse: **Gold__lh**
- Power BI Desktop (for local development)

### Option 1: Git Integration (Recommended)
1. Connect SAIL workspace to this GitHub repo
2. Sync workspace → report appears automatically
3. Configure data source to Gold__lh

### Option 2: Power BI Desktop
1. Open `SAIL_CEO_Dashboard_Report/` folder in Power BI Desktop
2. Configure data source to Gold__lh
3. Publish to SAIL workspace

## 📁 Report Structure

```
SAIL_CEO_Dashboard_Report/
├── .pbi/
│   └── localSettings.json
├── definition/
│   ├── model.tmdl              # Data model + DAX measures
│   └── pages/
│       ├── overview.json       # KPI cards, production vs target
│       ├── production.json     # BF, SMS, sinter plants, coke ovens
│       ├── mills.json          # Rolling mill performance
│       ├── rawmaterials.json   # Stock positions
│       ├── despatch.json       # Loading and despatch
│       ├── energy.json         # Power generation
│       └── delays.json         # Production delays
├── StaticResources/
│   └── RegisteredResources/
│       └── SAIL-Dark-Theme.json
├── report.json
└── README.md
```

## 📈 DAX Measures

Key measures in the report:
- `[Total Actual]` - Sum of production actuals
- `[Total Target]` - Sum of production targets
- `[Achievement %]` - (Actual / Target) × 100
- `[KPI Status]` - Visual indicator (✓/✗)
- `[Hot Metal Actual/Target]` - Blast furnace production
- `[Crude Steel Actual/Target]` - SMS production
- `[Saleable Steel Actual/Target]` - Final product
- `[Total Delay Hours]` - Production downtime

## 🎨 Theme

Custom SAIL dark theme with:
- Primary: Orange (#e87a20)
- Success: Green (#1db954)
- Warning: Amber (#d4a017)
- Error: Red (#e84040)
- Info: Cyan (#0aafcf)
- Background: Dark blue (#080c14)

## 🔗 Related Artifacts

- Pipeline: `SAIL_Production_Pipeline` (ID: c67f5ae1-fad0-4059-8247-9bd90a808be5)
- Notebooks: 8 modular notebooks (00_Pipeline_Orchestrator through 07_Semantic_Model)
- Lakehouses: Bronze__lh, Silver__lh, Gold__lh

## 📝 Maintenance

- Report connects to Gold lakehouse tables
- Data refreshes automatically when pipeline runs
- No manual data refresh needed
- Theme can be customized in StaticResources/RegisteredResources/

## 📧 Contact

For issues or questions, contact the SAIL data engineering team.
