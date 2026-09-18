import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 1. Generate Synthetic Training Data
# Features: [packet_size_bytes, requests_per_sec, failed_logins]
# Target: 0 = Safe, 1 = Suspicious, 2 = Critical Threat
X_train = np.array([
    [200, 2, 0],    # Safe: Normal browsing
    [500, 5, 1],    # Safe: Standard API traffic
    [64, 150, 0],   # Suspicious: High request rate (DDoS probe)
    [1024, 1, 12],  # Suspicious: Brute-force attempt
    [64, 500, 25],  # Critical Threat: Active DDoS + Brute Force
    [1500, 250, 50] # Critical Threat: Automated exploit payload
])

y_train = np.array([0, 0, 1, 1, 2, 2])

# 2. Train Random Forest Model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# 3. Save the trained model to disk
joblib.dump(model, "model.joblib")
print("[+] Machine Learning model successfully trained and saved as 'model.joblib'")