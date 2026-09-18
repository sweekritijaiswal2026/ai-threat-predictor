# AI Cyber Threat Predictor

## Project Overview
The AI Cyber Threat Predictor is a real-time machine learning security dashboard built to detect, classify, and visualize network security anomalies before they impact core server infrastructure. Modern web applications face constant automated attacks ranging from brute-force login attempts to distributed denial-of-service (DDoS) probes. Traditional firewall rules often rely on static, hardcoded thresholds that fail to adapt to complex, multi-variable attack patterns. This project addresses that challenge by providing an intelligent, decoupled security layer that evaluates incoming traffic metrics and determines risk levels in real time. 

Reaching a 40% completion milestone—representing a fully functional vertical slice—the project successfully demonstrates end-to-end integration across three distinct computing tiers. An interactive client dashboard communicates asynchronously with a high-performance Python REST API, which forwards formatted telemetry data into a trained machine learning classification engine to generate immediate threat assessments.

## System Architecture & Workflow

```text
┌─────────────────────────┐       HTTP POST /predict       ┌─────────────────────────┐
│  Client Web Interface   │ ────────────────────────────>  │  FastAPI Backend Server │
│      (index.html)       │  <───────────────────────────  │        (app.py)         │
└─────────────────────────┘       Prediction JSON          └────────────┬────────────┘
                                                                        │
                                                                 Feature Vector
                                                                        │
                                                                        ▼
                                                           ┌─────────────────────────┐
                                                           │ Inference Engine (ML)   │
                                                           │     (model.joblib)      │
                                                           └─────────────────────────┘
Client Presentation Layer (index.html): The front-end user interface is built using HTML5, CSS3, and JavaScript. It provides an intuitive control panel where security analysts or administrators can input network parameters, including Packet Size (in bytes), Request Rate (requests per second), and Failed Login Counts. The JavaScript client packages these inputs into a structured JSON payload and sends an asynchronous HTTP POST request to the backend. Upon receiving a response, the dashboard dynamically updates the display with color-coded risk indicators: Green for Safe traffic, Yellow for Suspicious activity, and Red for Critical Threats.

Backend Orchestration Layer (app.py): The server is built on FastAPI, an asynchronous, high-performance Python framework. Upon receiving an incoming request at the /predict endpoint, FastAPI uses Pydantic schemas to strictly validate the data structure and data types. Once validated, the backend converts the numerical values into a structured NumPy feature vector array compatible with the machine learning model. FastAPI then handles the cross-origin resource sharing (CORS) middleware to ensure secure communication between the web frontend and the backend server.

Machine Learning Engine (model.joblib): The core intelligence of the application is powered by a Scikit-learn RandomForestClassifier trained via train_model.py. The model evaluates the numerical feature vectors against trained decision boundaries to predict network risk levels. The classification outputs are categorized into three distinct security tiers:

Class 0 (SAFE): Standard background web traffic and legitimate user browsing activity.

Class 1 (SUSPICIOUS): Anomalous traffic patterns, such as elevated request rates or repeated authorization failures, indicating potential brute-force or probing activity.

Class 2 (CRITICAL THREAT): Severe attack signatures, such as high-volume request bursts combined with massive failed login spikes, indicating active DDoS or automated exploit attempts.

Real-World Utility & Industry Relevance
In enterprise IT environments, security operations centers (SOC) process millions of log entries every minute. Human analysts cannot manually evaluate every incoming request. By placing an asynchronous machine learning pipeline in front of primary web services, organizations can automate initial threat triage. This system serves as a foundational prototype for Security Information and Event Management (SIEM) platforms, enabling security teams to visualize threat alerts instantly and prioritize responses based on machine-calculated severity scores.

Installation & Setup Guide
Prerequisites
Ensure you have Python 3.8+ and pip installed on your machine.

1. Clone the Repository
Bash
git clone [https://github.com/YOUR_USERNAME/ai-threat-predictor.git](https://github.com/YOUR_USERNAME/ai-threat-predictor.git)
cd ai-threat-predictor
2. Install Required Dependencies
Install all required Python libraries using pip:

Bash
pip install fastapi uvicorn scikit-learn joblib numpy
3. Train and Export the ML Model
Run the training script to generate the trained model artifact (model.joblib):

Bash
python train_model.py
4. Start the FastAPI Server
Launch the asynchronous Uvicorn web server hosting the FastAPI application:

Bash
uvicorn app:app --reload
The terminal will display INFO: Uvicorn running on http://127.0.0.1:8000.

5. Launch the Web Interface
Navigate to your project directory and double-click index.html to open the security dashboard in any standard modern web browser.

Product Roadmap (Future 60% Development)
While the current vertical slice delivers a functional detection core, the remaining 60% of the planned development roadmap focuses on expanding the system from passive threat monitoring into an active, automated defense platform:

Active Threat Mitigation Layer (20%): Integrating automated rate-limiting middleware using SlowAPI to throttle high-frequency connections, alongside automated firewall rules (iptables integration) that automatically drop incoming traffic from IP addresses flagged with Class 2 (Critical Threat) status.

Database & Audit Logging Tier (20%): Implementing persistent data storage using SQLite or PostgreSQL to record all incoming telemetry, model prediction scores, and timestamped alert histories for long-term security auditing and compliance reporting.

Interactive Analytics & Deployment Tier (20%): Embedding live dynamic charts using Chart.js on the web interface to display real-time attack frequency trends over time, and containerizing the entire application with Docker for seamless cloud deployment on platforms like AWS or Render.
