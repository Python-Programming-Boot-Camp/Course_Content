# pip install matplotlib
import matplotlib.pyplot as plt
x = ["java","javascript","python"]
h = [100,200,300]
c = ["green","red","blue"]
b = [10,20,30]
plt.bar(x,h,width=0.5,align="center",color=c,linewidth=4,edgecolor="black",bottom=b)
plt.xlabel("Computer Language")
plt.ylabel("Values")
plt.title("Sample Bar Graph")
plt.show()