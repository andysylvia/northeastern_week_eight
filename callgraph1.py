import matplotlib.pyplot as plt

fig, ax = plt.subplots()

calls = ['argument', 'criminal threatening', 'harassment', ]
counts = [302,150,85]
bar_labels = ['red', '_red', 'orange']
bar_colors = ['tab:red',  'tab:red', 'tab:orange']

ax.bar(calls, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('types of call for service')
ax.set_title('total calls for service')
ax.legend(title='types of calls for service')

plt.show()
