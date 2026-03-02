# ============================================
# Data Science & Machine Learning Env Check
# ============================================

required_libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scipy",
    "sklearn",          # scikit-learn
    "statsmodels",
    "xgboost",
    "lightgbm",
    "tensorflow",
    "torch",            # PyTorch
    "plotly",
    "jupyter"
]

import importlib

missing = []
installed = []

print("🔍 Checking installed libraries...\n")

for lib in required_libraries:
    try:
        module = importlib.import_module(lib)
        version = getattr(module, "__version__", "unknown version")
        print(f"✅ {lib:<15} | Version: {version}")
        installed.append(lib)
    except ImportError:
        print(f"❌ {lib:<15} | NOT INSTALLED")
        missing.append(lib)

print("\n======================================")
print(f"Installed: {len(installed)}")
print(f"Missing:   {len(missing)}")
print("======================================")

if missing:
    print("\n📦 To install missing libraries, run:\n")
    print(f"pip install {' '.join(missing)}")
else:
    print("\n🎉 All core data science libraries are installed!")


import pip
pip install nbformat numpy pandas matplotlib seaborn scipy sklearn statsmodels xgboost lightgbm tensorflow torch plotly



