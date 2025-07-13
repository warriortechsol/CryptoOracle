#!/bin/bash

echo "📁 Cleaning up CryptoOracle repo..."

# Navigate to CryptoOracle root
cd "$(dirname "$0")"

# Ensure frontend public folder exists
mkdir -p CryptoOracle-Frontend/public
mkdir -p CryptoOracle-Frontend/src/components

# Move images to frontend/public
if [ -f "logo.png" ]; then
  mv logo.png CryptoOracle-Frontend/public/
  echo "✅ Moved logo.png to public/"
fi

if [ -f "icon.ico" ]; then
  mv icon.ico CryptoOracle-Frontend/public/
  echo "✅ Moved icon.ico to public/"
fi

# Move misplaced README and rename
if [ -f "README.txt" ]; then
  mv README.txt CryptoOracle-Frontend/README.md
  echo "✅ Renamed and moved README.txt to README.md"
fi

# Delete stray frontend files if they're redundant
[ -f "predictionpanel.jsx" ] && rm predictionpanel.jsx && echo "🗑 Removed stray predictionpanel.jsx"
[ -f "clean_requirements.py" ] && rm clean_requirements.py && echo "🗑 Removed clean_requirements.py"

# Suggest reviewing legacy folders
if [ -d "frontend" ] || [ -d "CryptoOracle" ]; then
  echo "⚠️ Review legacy folders: 'frontend/' and 'CryptoOracle/' — they may be outdated or duplicated."
fi

echo "🎉 Cleanup complete. Your workspace is now tidy and deploy-ready."
