# Basic Venn Diagram

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Create the Venn diagram
venn3(subsets=(1,1,1,1,1,1), set_labels=('Interests', 'Skills', 'Needs'), 
      set_colors=('red', 'green', 'blue'), subset_label_formatter=lambda x: f"{x:,}")

# Customize the plot
plt.title('Career Decision')

# Show the plot
plt.show()
