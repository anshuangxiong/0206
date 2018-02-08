from pylab import *

# 创建一个8*6点的图，并设置分辨率为80
figure(figsize=(8,6),dpi=80)

# 创建一个新的1*1的子图，接下来的图样绘制在其中的第一块
ax = subplot(1, 1, 1)


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的 连续的 宽度为1 的线条
plot(X, C, color='green', linewidth=2.0, linestyle='-', label='cosine')


# 绘制正弦曲线，使用蓝色的 连续的 宽度为1 的线条
plot(X, S, color='blue', linewidth=1.0, linestyle='-', label='sine')
legend(loc='upper left')
# 设置横轴的上下限
xlim(-4.0, 4.0)
xlim(X.min()*1.1, X.max()*1.1)

# 设置横轴记号
xticks(np.linspace(-4, 4, 9, endpoint=True))
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# 设置纵轴的上下限
ylim(-1.1, 1.10)
ylim(C.min()*1.1, C.max()*1.1)

# 设置纵轴记号
yticks(np.linspace(-1, 1, 5, endpoint=True))
yticks([-1, 0, 1],[r'$-1$', r'$0$', r'$+1$'])
# 以分辨率72 来保存图片
savefig('exercice_1.png', dpi=72)

show()