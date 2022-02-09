import wandb

wandb.init(project="visualize-labels", name="images")  #initialisation

count={}
for i in range(0,10):
	count[i]=0


c=0
index=0
classes=[]
while(c<=10)
	if(count[index]==0):                  # generation
		label=Y_train(index,0)
		image=X_train(c,:)
		classes.append(image)
		count[label]=1
		c++

	index+=1


for image in classes:                                 # logging or plotting
	wandb.log("images":image)

wandb.finish()     # generation