#!/bin/bash

set -e

pip install -r requirements.txt

echo "Which class are you trying to download PDF's from: (combo : 1) (OR : 2) "
read class

echo "Which homework are you working on: "
read homework

echo "Name the directory to download files to: "
read dir

if  [ "$class" == "1" ]; then
    echo "Downloading files for Combinatorics (21-301) ..." 
    python3 scraper.py --class=combo --homework=$homework --directory=$dir
elif [ "$class" == "2" ]; then
    echo "Downloading files for Operations Research 2 (21-392) ..." 
    python3 scraper.py --class=OR --homework=$homework --directory=$dir
else
    echo "Invalid choice for class. Exiting..."
    exit
fi
