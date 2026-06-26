# OS Mechanisms and Technical Specifications
### Component 4: Environmental and Safety Monitoring System 
**Team:** `Smart Fun Run TeamA Component5`

Introduction

Our group was responsible for developing the Environmental and Safety Monitoring System for the POPBL project. The system continuously collects data from IoT sensors, such as air quality, temperature, humidity, gas levels, and safety detectors, to provide real-time environmental monitoring and hazard alerts. To ensure reliable operation when multiple sensors transmit data simultaneously, we incorporated several core Operating System concepts into our backend architecture.

---

## 1. Handling Concurrency (Multithreading in server.py)

In a real-world monitoring environment, multiple IoT sensors may send environmental and safety readings at the same time. To prevent delays and maintain real-time monitoring capabilities, we implemented a multithreaded server architecture.

**Implementation**: Each incoming sensor request to the monitoring API is processed in its own dedicated thread. This enables the server to handle multiple sensor updates concurrently without blocking other incoming data streams.

**Tracking**: The system records the Thread ID and Process ID **(PID)** for each transaction, allowing developers to verify that the operating system is efficiently managing multiple tasks simultaneously.

**Purpose**: This approach prevents Head-of-Line Blocking, ensuring that delays from one sensor do not affect the responsiveness of the entire monitoring system. As a result, environmental data and safety alerts can be processed in real time.

---

## 2. Synchronization and Mutex Lock Mechanism

Since all sensor threads share a common database and log file for storing environmental readings, synchronization is essential to avoid data conflicts.

**Implementation**: A Mutex Lock using **threading.Lock()** is implemented within the backend to control access to shared resources.

**Critical Section**: All database and log-writing operations are enclosed within a protected with lock: block. This guarantees that only one thread can modify the shared data at any given moment.

**Result**: The synchronization mechanism eliminates race conditions, ensuring that sensor readings, safety alerts, and environmental records remain accurate and consistent even during periods of heavy system activity.

---

## 3. File Management and Data Logging System
  The Environmental and Safety Monitoring System maintains historical records of sensor readings for analysis and reporting purposes.

**Initialization Logic**: During startup, the backend uses the **os.path** library to verify the existence of monitoring log files. If the files do not exist, the system automatically generates new log files with predefined fields such as **Timestamp, Sensor ID, Process ID, Thread ID, Environmental Readings, Alert Status, and Device Location**.

**Automated Organization**: Data logs are automatically structured and formatted to improve readability and facilitate future analysis. This enables event organizers and administrators to review environmental trends and safety incidents efficiently.

**Purpose**: The file management system ensures reliable data persistence while maintaining organized records for operational monitoring and decision-making.

---

## 4. System Monitoring and Fault Tolerance
To ensure continuous operation and system reliability, several monitoring and fault-tolerance mechanisms are integrated into the backend.

**Device Verification**: The system records the IP Address and unique identifier of each connected IoT device to verify that data originates from authorized environmental monitoring sensors.

**Error Handling**: Critical operations are protected using try-except exception handling. If temporary issues occur, such as communication failures, sensor disconnections, or file access errors, the system logs the error and continues operating without interruption.

**Alert Management**: When environmental conditions exceed predefined safety thresholds like poor air quality, hazardous gas detection, or abnormal temperature levels then the system immediately generates alerts and records the incident for further action.

**Result**: These mechanisms improve system stability, minimize downtime, and ensure continuous environmental and safety monitoring in real-world deployment scenarios.



