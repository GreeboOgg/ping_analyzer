import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration
INPUT_FILE = 'D:/Eclipse/python/output.txt'

# Read the CSV file
df = pd.read_csv(INPUT_FILE)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Calculate statistics
average_ping = df['time_ms'].mean()
max_ping = df['time_ms'].max()
min_ping = df['time_ms'].min()

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['time_ms'], marker='o', linestyle='-', linewidth=1, markersize=3)
plt.axhline(y=average_ping, color='r', linestyle='--', label=f'Average: {average_ping:.2f} ms')
plt.axhline(y=max_ping, color='g', linestyle='--', label=f'Max: {max_ping:.2f} ms')
plt.axhline(y=min_ping, color='b', linestyle='--', label=f'Min: {min_ping:.2f} ms')

# Customize the plot
plt.title('Ping Times to 8.8.8.8 Over Time')
plt.xlabel('Time')
plt.ylabel('Ping Time (ms)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()

# Print statistics
print(f"\nPing Statistics:")
print(f"Average ping time: {average_ping:.2f} ms")
print(f"Maximum ping time: {max_ping:.2f} ms")
print(f"Minimum ping time: {min_ping:.2f} ms")
print(f"Total number of pings: {len(df)}") 