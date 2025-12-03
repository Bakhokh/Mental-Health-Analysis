import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load your dataset
df = pd.read_csv('data1\Mental_Health_Dataset.csv')

# Convert Stress Level into numeric values for plotting
# stress_map = {'Low': 1, 'Moderate': 2, 'High': 3}
# df['StressValue'] = df['Stress Level'].map(stress_map)

# # Create violin plot
# plt.figure(figsize=(8,5))
# sns.violinplot(x='Gender', y='StressValue', data=df)

# plt.title('Stress Level Distribution by Gender')
# plt.ylabel('Stress Level (1 = Low, 2 = Moderate, 3 = High)')
# plt.xlabel('Gender')
# plt.show()

