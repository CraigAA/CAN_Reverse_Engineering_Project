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
flowchart TD

    A[Raw CAN Log CSV<br/>(timestamp, bus, raw_frame)] --> B[Filter rows by CAN ID<br/>(regex match "^ID#")]
    B --> C[Extract payload hex<br/>(split at '#')]
    C --> D[Convert hex → 64-bit vector<br/>(int → bin → list)]
    D --> E[bit_data array<br/>(N × 64 bits, int8)]
    E --> F[Compute window start indices<br/>(0, stride, 2×stride...)]
    F --> G[Build samples list<br/>(array_id, start_idx pairs)]

    G --> H[CANClassificationDataset]

    H --> I[__getitem__(idx)]
    I --> I1[Slice 200-frame window]
    I --> I2[Load base label vector for CAN ID]
    I --> I3[Compute static_mask via peak-to-peak]
    I --> I4[Zero out labels where bits never change]
    I --> I5[Return (window_tensor, label_tensor)]

    H --> J[PyTorch DataLoaders<br/>(train / val / test)]
```
