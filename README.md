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
    title CAN Bus Reverse Engineering Research Project
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b %Y
    tickInterval 2week

    section Phase 1: Foundation & Core Project (Part A)
    Initial Planning & Setup       :
    Research Draft Proposal        :crit, active, rp, 2025-10-01, 2025-10-10
    Finalise Project Proposal      :milestone, frp, 2025-10-10, 2025-10-12
    Literature Review              :active, lr, 2025-10-01, 2025-11-02
    
    Data Pipeline Development      :
    Environment Setup & Data Parsing :crit, active, dpenv, 2025-10-13, 2025-10-26
    Sliding Window & Labeling Logic :crit, active, dpsw, 2025-10-27, 2025-11-16
    Finalize Data Pipeline         :milestone, dpm, 2025-11-17, 2025-11-18

    Progress & Mid-Point Review    :
    Prepare Progress Presentation  :crit, active, ppp, 2025-11-17, 2025-11-21
    Progress Presentation          :milestone, pp, 2025-11-22, 2025-11-23

    section Phase 2: Advanced Research & Development (Part B)
    Core Model Development         :
    Implement Baseline Method      :crit, active, bl1, 2026-01-20, 2026-02-09
    Develop Transformer Arch.      :crit, active, tda, 2026-02-10, 2026-03-02
    Train & Tune Transformer (Veh A) :crit, active, tta, 2026-03-03, 2026-03-23
    Core Models Complete           :milestone, cpmc, 2026-03-23, 2026-03-23

    Analysis & Stretch Goals       :
    Perform Core Comparative Analysis :active, cca, 2026-03-24, 2026-04-06
    Stretch: Generalization on Veh B  :active, sg1, 2026-04-07, 2026-04-27
    Stretch: Investigate Transfer Learning :active, sg2, 2026-04-28, 2026-05-11

    section Phase 3: Finalization & Submission
    Final Report & Presentation    :
    Draft Final Report & Results   :crit, active, dfr, 2026-05-05, 2026-05-18
    Prepare Final Presentation     :active, pfp, 2026-05-19, 2026-05-24
    Submit Final Report            :milestone, fta, 2026-05-25, 2026-05-28
    Final Project Presentation     :milestone, fpp, 2026-05-29, 2026-05-31
```
