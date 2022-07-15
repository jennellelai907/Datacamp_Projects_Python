from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()
