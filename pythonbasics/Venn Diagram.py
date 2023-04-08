# Venn Diagram
# I want to write a venn diagram in python that indicates my interests, skills and needs which eventually can help me to choose a career.

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Create the Venn diagram
venn3(subsets=(1,1,1,1,1,1), set_labels=('Interests', 'Skills', 'Needs'), 
      set_colors=('red', 'green', 'blue'), subset_label_formatter=lambda x: f"{x:,}")

# Customize the plot
plt.title('Career Decision')

# Show the plot
plt.show()
