

Known_bit_labels = [  # 64 per-bit classes (one per bit position)
                     # Byte 0 (Sensor)
                     3, 3, 3, 3, 3, 3, 3, 3,
                     # Byte 1 (Sensor)
                     3, 3, 3, 3, 3, 3, 3, 3,
                     # Byte 2 (Spare)
                     0, 0, 0, 0, 0, 0, 0, 0,
                     # Byte 3 (Spare, Counter, Spare)
                     0, 0, 0, 0, 2, 2, 2, 0,
                     # Byte 4 (Checksum)
                     1, 1, 1, 1, 1, 1, 1, 1,
                     # Byte 5 (Spare)
                     0, 0, 0, 0, 0, 0, 0, 0,
                     # Byte 6 (Spare)
                     0, 0, 0, 0, 0, 0, 0, 0,
                     # Byte 7 (Spare)
                     0, 0, 0, 0, 0, 0, 0, 0]

Known_frames = {
    # CAN ID 140: field layout is stable; counter/sensor values change per payload.
    "140#0009FD4300000D00": Known_bit_labels,
    "140#000AFD4300000D00": Known_bit_labels,
    "140#000BFD4300000D00": Known_bit_labels,
    "140#000CFD4300000D00": Known_bit_labels,
    "140#000DFD4300000D00": Known_bit_labels,
    "140#000EFD4300000D00": Known_bit_labels,
    "140#000FF94300000D00": Known_bit_labels,
    "140#0000F84300000D00": Known_bit_labels,
    "140#0001F84300000D00": Known_bit_labels,
    "140#0002F64300000D00": Known_bit_labels,
    "140#0003F44300000D00": Known_bit_labels,
    "140#0004F44300000D00": Known_bit_labels,
    "140#0005F04300000D00": Known_bit_labels,
    "140#0006EF4300000D00": Known_bit_labels,
    "140#0007EF4300000D00": Known_bit_labels,
}


