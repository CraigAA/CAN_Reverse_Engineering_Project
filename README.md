# CAN_Reverse_Engineer_Project

## Research Objectives
Develop and validate a multi-modal data collection and semi-automated labeling framework that reduces manual effort in CAN bus reverse engineering by enabling systematic identification and decoding of common vehicle signals.

Create a high-quality, synchronized multi-modal dataset combining CAN bus logs, timestamped video, periodic OBD-II messages, GPS data, and IMU measurements for automotive reverse engineering research
Develop machine learning models that can classify CAN message types and decode signal values for labeled message classes with measurable confidence metrics

## Research Questions
RQ1: Data Collection & Labeling Framework
How effectively can multi-modal sensor data (GPS, IMU, OBD-II) be used to automatically generate labeled training data for CAN bus signals?

RQ2: Automated Signal Classification
To what extent can machine learning models accurately classify CAN message IDs to their corresponding vehicle signals using semi-automatically labeled training data?

RQ3: Signal Decoding Automation
Primary: How accurately can signal encoding parameters (byte position, endianness, scaling, offset) be automatically extracted for classified CAN messages?

## Gantt Chart
```mermaid
gantt
    title CAN Bus Reverse Engineering Research Project
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b %Y
    tickInterval 2week
    section Phase 1:<br>Proposal
    Research Draft Proposal     :crit, active, rp, 2025-10-01, 2025-10-10
    Plan Hardware               :done, oh, 2025-10-02, 2025-10-05
    Finish Project Proposal     :milestone, frp, 2025-10-10, 2025-10-12
    Literature Review           :active, lr, 2025-10-01, 2025-11-02
    Finish Project Proposal     :milestone, frp, 2025-11-01, 2025-11-02
    Instrument Testing          :it, 2025-10-15, 2025-11-18
    Progress Presentation       :milestone, pp, 2025-11-19, 2025-11-23

    section Phase 2:<br>Data Collection
    Code Data Pipeline          :dp, 2025-11-18, 2025-12-14
    Data Collection             :dc, 2025-12-08, 2025-12-31
    Data Cleaning & Sync        :dc, 2025-12-21, 2026-01-10

    section Phase 3:<br>Model Development
    Feature Engineering         :fe, 2026-02-23, 2026-03-08
    Baseline Models             :bm, 2026-03-02, 2026-03-08
    Classification Models (RQ2) :cm, 2026-03-09, 2026-03-29
    Decoding Algorithms (RQ3)   :da, 2026-03-30, 2026-05-03

    section Phase 4:<br>Evaluation<br>and Report
    Model Evaluation            :ce, 2026-03-09, 2026-05-17
    Report Writing              :wr, 2026-03-09, 2026-05-31
    Finish Project Report       :milestone, fta, 2026-05-25, 2026-05-31
```
