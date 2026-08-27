import numpy as np
names = np.array(['Zubin', 'Tanvi', 'Arnav', 'Ishani', 'Devrat', 
                   'Kiara', 'Yash', 'Riya', 'Nakul', 'Avantika'])

hours_studied = np.array([5, 8, 2, 6, 3, 9, 4, 7, 1, 6])
attendance = np.array([85, 95, 60, 90, 70, 98, 75, 88, 55, 92])
previous_score = np.array([72, 81, 55, 76, 60, 88, 65, 79, 48, 74])
final_score = np.array([78, 91, 52, 83, 61, 95, 68, 85, 45, 80])
print("names:", names.shape, names.dtype)
print("hours_studied:", hours_studied.shape, hours_studied.dtype)
print("attendance:", attendance.shape, attendance.dtype)
print("previous_score:", previous_score.shape, previous_score.dtype)
print("final_score:", final_score.shape, final_score.dtype)
print("Mean of final scores:", np.mean(final_score))
print("max of final scores:", np.max(final_score))
print("min of final scores:", np.min(final_score))
print("Standard deviation of final scores:", np.std(final_score))
final_score+=5
boolean=final_score>75
print(final_score[boolean])
