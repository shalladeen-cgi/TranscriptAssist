import sys, subprocess
from pathlib import Path

def main():
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    app = base / "app.py"
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app)], check=True)

if __name__ == "__main__":
    main()
