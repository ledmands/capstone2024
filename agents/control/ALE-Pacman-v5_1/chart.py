from numpy import load
import matplotlib.pyplot as plt 
import matplotlib.axes

data = load("evaluations.npz")
lst = data.files # data.files lists the keys that are available for data

# print('timesteps: \n', data['timesteps'])
# print('results: \n', data['results'])
print('ep_lengths: \n', data['ep_lengths'])

# results and ep_lengths are 2d arrays, because each evaluation is 5 episodes long.
# I want to plot the average of each evaluation.

# for each item in results, loop through the array and save the average
avg_ep_result_arr = []
for eval in data['results']:
    result_sum = 0
    
    for result in eval:
        result_sum = result_sum + result
        
    avg_ep_result = result_sum / len(eval)
    avg_ep_result_arr.append(avg_ep_result)
    
avg_ep_len_arr = []
for eval in data['ep_lengths']:
    ep_len_sum = 0
    
    for ep_length in eval:
        ep_len_sum = ep_len_sum + ep_length
        
    avg_ep_len = ep_len_sum / len(eval)
    avg_ep_len_arr.append(avg_ep_len)
    
kwargs = {"xscale":"log"}
plt.axes(kwargs=kwargs)
plt.plot(data['timesteps'], avg_ep_result_arr)
plt.bar(data['timesteps'], avg_ep_len_arr, width=10000)

plt.show()