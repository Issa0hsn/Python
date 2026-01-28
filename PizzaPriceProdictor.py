import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.rcParams['grid.color'] = '#444444'


m=40
x=np.random.uniform(1,70,m)
noise=np.random.normal(1,2.5,m)
y=5 +0.8*x +noise


w=0
b=0
def pre_fun(w,b,x):
  return w*x + b
def cost(x,y,w,b):
  total_cost=0
  
  total_cost=(np.sum(pre_fun(w,b,x)-y)**2)/(2*m)
  return total_cost  
colors=['r','b','b','y','g','g']
cont=0


alpha=0.001  




plt.figure(figsize=(10, 6))

for i in range(2000):
  
  dj_dw=np.sum((pre_fun(w,b,x)-y)*x/m)
  dj_db=(np.sum((pre_fun(w,b,x)-y))/m)
  w-=alpha*dj_dw
  b-=alpha*dj_db
  if i in[0,1,10,100,1000,2000]:
    if cost(x,y,w,b) <0.01:
      plt.plot(x,w*x+b,c='g',label="our prediction")
      i=10000
    plt.plot(x,w*x+b,c=colors[cont],label="our prediction")
    cont+=1
      
#plt.style("dark_background")      
plt.scatter(x,y,c="r",marker="x",label="Actual data")
plt.title("pizza price prediction")
plt.xlabel('Diameter (inch)')
plt.ylabel("Price ($)")
plt.grid(True)
#plt.legend()

plt.show()
# رسم البيانات (نقاط نيون سماوي)
plt.scatter(x, y, color='#00FFFF', s=25, alpha=0.7, edgecolors='none', label='Training Data')

# رسم خط التوقعات (خط نيون زهري)
x_line = np.linspace(1, 70, 100) # نقاط للخط فقط
y_line = w * x_line + b
plt.plot(x_line, y_line, color='#FF00FF', linewidth=2.5, label='Machine Learning Fit')

# تزيين الرسمة
plt.title('Pizza Price Prediction Model (AI Training)', fontsize=16, fontweight='bold')
plt.xlabel('Diameter (inch)', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(facecolor='black', edgecolor='white')
error=(pre_fun(w,b,x)-y)/y
error_pers=np.mean(error)*100
if error_pers <0 :
  error_pers=error_pers*(-1)
# إضافة المعادلة المكتشفة على الرسمة (لمسة تقنية)
text_str = f'Model Found:\nPrice = {w:.2f} * Size + {b:.2f} \n error rate : {error_pers:.3f}%'
plt.text(5, 43, text_str, fontsize=12, color='yellow', 
         bbox=dict(facecolor='#222222', edgecolor='yellow', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()

 
  
  

