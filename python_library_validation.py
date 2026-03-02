# ============================================
# Data Science Runtime Verification Script
# ============================================

print("🔍 Running Data Science Library Tests...\n")

# 1️⃣ NumPy Test
try:
    import numpy as np
    arr = np.array([1, 2, 3])
    print("✅ NumPy working | Mean:", np.mean(arr))
except Exception as e:
    print("❌ NumPy failed:", e)

# 2️⃣ Pandas Test
try:
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    print("✅ Pandas working | Column Sum:", df["A"].sum())
except Exception as e:
    print("❌ Pandas failed:", e)

# 3️⃣ Matplotlib Test
try:
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Test Plot")
    plt.close()  # prevent display blocking
    print("✅ Matplotlib working | Plot created successfully")
except Exception as e:
    print("❌ Matplotlib failed:", e)

# 4️⃣ Scikit-learn Test
try:
    from sklearn.linear_model import LinearRegression
    import numpy as np
    
    X = np.array([[1], [2], [3]])
    y = np.array([2, 4, 6])
    
    model = LinearRegression()
    model.fit(X, y)
    
    prediction = model.predict([[4]])
    print("✅ Scikit-learn working | Prediction for 4:", prediction[0])
except Exception as e:
    print("❌ Scikit-learn failed:", e)

# 5️⃣ SciPy Test
try:
    from scipy import stats
    result = stats.ttest_ind([1,2,3], [4,5,6])
    print("✅ SciPy working | t-statistic:", result.statistic)
except Exception as e:
    print("❌ SciPy failed:", e)

print("\n🎯 Runtime test complete.")