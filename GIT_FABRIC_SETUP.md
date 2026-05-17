# Git + Fabric Integration Setup

## Quick Start

### 1. Create GitHub Repo

**Option A: GitHub CLI** (fastest)
```bash
cd C:\Users\ashahwal\SAIL-Fabric
gh repo create SAIL-Fabric --public --description "SAIL Operations Dashboard - Microsoft Fabric Workspace" --source=. --remote=origin --push
```

**Option B: GitHub Web**
1. Go to https://github.com/new
2. Name: `SAIL-Fabric`
3. Description: `SAIL Operations Dashboard - Microsoft Fabric Workspace`
4. Do NOT initialize with README
5. Create repo
6. Run:
   ```bash
   cd C:\Users\ashahwal\SAIL-Fabric
   git remote add origin https://github.com/<YOUR_USERNAME>/SAIL-Fabric.git
   git push -u origin master
   ```

### 2. Connect Fabric Workspace to Git

1. **Open Fabric Portal**: https://msit.powerbi.com
2. **Go to SAIL workspace**
3. **Click ⚙️ gear icon** → Workspace settings
4. **Git integration** (left panel) → Click **Connect**
5. **Configure**:
   - Organization: Your GitHub username/org
   - Repository: `SAIL-Fabric`
   - Branch: `master`
   - Git folder: `/` (root)
   - Click **Connect and sync**
6. **Wait for sync** → Report appears in workspace
7. **Configure data source** → Connect to `Gold__lh` → Refresh

## What Happens After Sync

✅ `SAIL_CEO_Dashboard_Report` appears as a Power BI Report artifact in SAIL workspace
✅ Bidirectional sync enabled (Git ↔ Fabric)
✅ Future changes to report automatically sync
✅ No manual upload needed

## File Structure in Git

```
SAIL-Fabric/
├── SAIL_CEO_Dashboard_Report/    ← This folder syncs to Fabric
│   ├── .pbi/
│   ├── definition/
│   │   ├── model.tmdl
│   │   └── pages/
│   ├── StaticResources/
│   ├── report.json
│   └── README.md
├── .gitignore
└── README.md
```

## Troubleshooting

### "Git integration not available"
- Ensure workspace is Premium/Fabric capacity
- Verify you have workspace admin permissions

### "Repository not found"
- Check repo visibility (public vs private)
- Verify GitHub permissions for Fabric app

### "Sync failed"
- Check file structure (PBIR folder must be valid)
- Ensure no merge conflicts in Git

## Next Steps After Setup

1. Open report in Fabric portal
2. Configure lakehouse connection (Gold__lh)
3. Refresh data
4. Verify all 7 pages render correctly
5. Test with live data

## Future Updates

To update the report:
1. Edit locally in Power BI Desktop
2. Save changes
3. Commit and push to Git
4. Fabric auto-syncs changes

OR:

1. Edit in Fabric portal
2. Use "Commit to Git" button
3. Changes push back to GitHub

## Workspace Details

- **Name**: SAIL
- **ID**: 5964ac59-2715-4b7a-910e-c5d2dcb82a77
- **Type**: Premium (Folder)
- **Capacity**: 15815a0f-4c24-4ef4-974f-36e9a7b14a60
