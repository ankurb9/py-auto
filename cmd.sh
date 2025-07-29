set -e -x

# Navigate to the script's directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "$DIR"

pip install -r requirements.txt

playwright install