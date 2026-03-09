# Ask commit message
$commitMessage = Read-Host "Enter commit message"

# Add changes
git add .

# Commit
git commit -m "$commitMessage"

# Pull latest changes
git pull origin main

# Push to GitHub
git push origin main

Write-Host "✅ Project successfully updated to GitHub!"