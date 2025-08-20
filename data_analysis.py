import matplotlib.pyplot as plt

# Quarterly retention data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
retention_rates = [67.97, 73.43, 72.04, 72.22]
industry_target = 85
average = sum(retention_rates) / len(retention_rates)

# Plotting the retention trend
plt.figure(figsize=(10, 6))
plt.plot(quarters, retention_rates, marker='o', color='blue', label='Retention Rate')
plt.axhline(y=industry_target, color='red', linestyle='--', label='Industry Target (85%)')
plt.title('Customer Retention Rate - 2024')
plt.xlabel('Quarter')
plt.ylabel('Retention Rate (%)')
plt.ylim(60, 90)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('retention_plot.png')
plt.show()

# Print average for confirmation
print(f"Average Retention Rate: {average:.2f}")
