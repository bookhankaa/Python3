"""
black 800 dot is negative, red 200 diamond is positive
"""
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(141, aspect='equal')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([0, 1])
frame1.axes.get_yaxis().set_ticks([0, 1])
plt.ylim((-.2, 1.2))
plt.xlim((-.2, 1.2))
plt.scatter([0, 0, 1], [0, 1, 0], marker='.', c='b', s=800)
plt.scatter([1], [1],  marker='D', c='r', s=200)
plt.title('AND')
plt.plot([-.2, 2.8], [1.4, -1.4])

plt.subplot(142, aspect='equal')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([0, 1])
frame1.axes.get_yaxis().set_ticks([0, 1])
plt.ylim((-.2, 1.2))
plt.xlim((-.2, 1.2))
plt.scatter([0, 0, 1], [0, 1, 0], marker='D', c='r', s=200)
plt.scatter([1], [1],  marker='.', c='b', s=800)
plt.title('NAND')
plt.plot([-.2, 2.8], [1.4, -1.4])

plt.subplot(143, aspect='equal')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([0, 1])
frame1.axes.get_yaxis().set_ticks([0, 1])
plt.ylim((-.2, 1.2))
plt.xlim((-.2, 1.2))
plt.scatter([0], [0], marker='.', c='b', s=800)
plt.scatter([0, 1, 1], [1, 1, 0],  marker='D', c='r', s=200)
plt.title('OR')
plt.plot([-.8, 1.8], [1.4, -1.4])

plt.subplot(144, aspect='equal')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([0, 1])
frame1.axes.get_yaxis().set_ticks([0, 1])
plt.ylim((-.2, 1.2))
plt.xlim((-.2, 1.2))
plt.scatter([0, 1], [1, 0], marker='D', c='r', s=200)
plt.scatter([0, 1], [0, 1],  marker='.', c='b', s=800)
plt.title('XOR')
plt.savefig("test.png", bbox_inches='tight')
plt.show()
