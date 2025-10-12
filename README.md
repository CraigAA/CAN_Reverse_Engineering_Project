# CAN_Reverse_Engineer_Project

## Research Objectives
Develop and validate a multi-modal data collection and semi-automated labeling framework that reduces manual effort in CAN bus reverse engineering by enabling an Machine Learning method of decoding of common vehicle signals.

Create a high-quality, synchronized multi-modal dataset combining CAN bus logs, timestamped video, periodic OBD-II messages, GPS data, and IMU measurements for automotive reverse engineering research
Develop machine learning models that can classify CAN message types and decode signal values for labeled message classes with measurable confidence metrics

## Research Questions
1. Data Collection & Labeling Framework
How effectively can multi-modal sensor data (video, GPS, IMU, OBD-II) be used to automatically generate labeled training data for CAN bus signals?

2. Automated Signal Classification
To what extent can machine learning models accurately classify CAN message IDs to their corresponding vehicle signals using semi-automatically labeled training data?

3. Signal Decoding Automation
Primary: How accurately can signal encoding parameters (byte position, endianness, scaling, offset) be automatically extracted for classified CAN messages?
```mermaid
gantt
    title Reverse Engineering Research Project
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y
    tickInterval 1month

    section Term 4 2025: <br>Project Part A
    Lit Review :crit, active, planning, 2025-10-12, 2025-11-01
    Develop & Finalize Data Pipeline :crit, active, pipeline, 2025-10-15, 2025-12-14
    Implement Baseline & Core Transformer :crit, active, coredev, 2025-11-01, 2025-12-31
    Progress Presentation          :milestone, pp, 2025-11-23, 1d
    
    %% ---Project Break from Late Jan to Mid-Feb ---
    
    section Semester 1 2026: <br>Project Part B
    Perform Core Comparative Analysis :active, cca, 2026-02-17, 2026-03-09
    Advanced Research & Stretch Goals  :active, stretch, 2026-03-10, 2026-04-06
    Final Report Writing & Submission  :crit, active, report, 2026-04-07, 2026-04-27
    Final Presentation                 :milestone, fpp, 2026-04-30, 1d
```
