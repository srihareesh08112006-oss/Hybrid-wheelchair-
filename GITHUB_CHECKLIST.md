# Checklist: Publishing to GitHub

## Before you push
- [ ] Replace `<Your Name>` in LICENSE and `<your-username>` in README
- [ ] Add your real firmware code to `firmware/`
- [ ] Confirm `.env` is NOT in the repo (only `.env.example`)
- [ ] No passwords, API keys, or personal data in any file
- [ ] Run `pip install -r requirements.txt && pytest tests/`

## Create the repo
- [ ] Sign in at github.com, click **+ > New repository**
- [ ] Name: `hybrid-wheelchair`
- [ ] Choose Public or Private
- [ ] Leave "Add README/.gitignore/license" **unchecked** (you already have them)
- [ ] Click **Create repository**

## Push
```bash
cd hybrid-wheelchair
git init
git add .
git commit -m "Initial commit: README, design doc, samples, license"
git branch -M main
git remote add origin https://github.com/<your-username>/hybrid-wheelchair.git
git push -u origin main
```

## After pushing
- [ ] Confirm Mermaid diagrams render in docs/TECHNICAL_DESIGN.md
- [ ] Add a repo description and topics (e.g. `wheelchair`, `assistive-tech`, `embedded`)
- [ ] Your link: `https://github.com/<your-username>/hybrid-wheelchair`
- [ ] Optional: add screenshots, a CI workflow, a CONTRIBUTING.md
