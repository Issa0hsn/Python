import numpy as np

# الدفعة الأولى من البيانات (وصلت الساعة 8 صباحاً)
# الأعمدة: [ProductID, CategoryID, Price, UnitsInStock, CustomerRating]



data_batch_1 = np.array([
    ['P101', 'C1', 120.0, 50, 4.5],
    ['P102', 'C2', 80.0, 150, 4.1],
    ['P103', 'C1', 110.0, 60, 4.4],
    ['P104', 'C3', 250.0, 20, 3.8],
    ['P105', 'C2', 75.0, 200, -1.0], # -1.0 يعني "لا يوجد تقييم"
    ['P106', 'C1', 130.0, 40, 4.6],
    ['P107', 'C3', 280.0, 15, 3.9],
    ['P108', 'C2', 90.0, 180, 4.0]
], dtype=object)

# الدفعة الثانية من البيانات (وصلت الساعة 9 صباحاً)


data_batch_2 = np.array([
    ['P109', 'C1', 125.0, 55, 4.7],
    ['P110', 'C2', 85.0, 160, 4.2],
    ['P111', 'C3', 265.0, 10, 3.5],
    ['P112', 'C1', 115.0, 45, 4.5]
], dtype=object)

#split the data 

master_batch=np.vstack([data_batch_1,data_batch_2])

identity_data=master_batch[:,0:2]
degrees_data=np.astype(master_batch[:,2:],float)


#cleaning the data 
degrees_data[degrees_data[:,2]<0,2]=np.mean(degrees_data[degrees_data[:,2]>=0,2])

# adding new column to numerical data           
inventory_values= degrees_data[:,1]*degrees_data[:,2]
inventory_values=inventory_values.reshape(len(degrees_data),1)
numerical_data=np.hstack([degrees_data,inventory_values])

#searching for the best rating product

best_product_id=identity_data[numerical_data[:,2]==np.max(numerical_data[identity_data[:,1]=="C1",2]),0]
print(best_product_id)


# refuel the inventory 

refuel_mask=(numerical_data[:,1]<50 )& (numerical_data[:,2]>4.0) 

products_to_refuel=identity_data[refuel_mask,0]

print("the products that need to refuel are {} and {}".format(products_to_refuel[0],products_to_refuel[1]))

# 
wight=np.array([0.4,-0.1,2.5,0.0])
expected_profit=np.dot(numerical_data,wight)

print(expected_profit)