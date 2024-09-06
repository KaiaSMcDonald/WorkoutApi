# Make a requests to the workout api
# Use the appropriate endpoint and parameters to retrieve data
# Save the response data as a variable (must be in JSON format)
# Extract a specific item from the nested dictionary in the response
# Use print statement to display this information 

import requests
from pprint import pprint 

url = "https://workout-planner1.p.rapidapi.com/customized"

#These parameters are for 33 minute work session
querystring = {"time":"33","equipment":"barbell","muscle":"glutes","fitness_level":"beginnner","fitness_goals":"strength"}

headers = {
    "x-rapidapi-key":
"c209679b5dmsh0587feb4f7e05d3p157d19jsn19aad2a49e80",
    "x-rapidapi-host":
"workout-planner1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pprint(response.json(),compact = True) #prints out the response in a more organized way

result = response.json() #saving the reponse data as a variable 

print(result.keys()) #Displays all the keys within the dictionary

#Extract and filter out exercises that require 10 reps 

exercises = result.get("Exercises",[])

exercises_with_10_reps = []


#Loop through all of the exercises to locate those with 12 reps 
for exercise in exercises:
    reps = exercise.get("Reps", "") #access the value associated with the key "Reps" in the dictionary
    if "10 reps" in reps: # checks to see if "10 reps" exists as a substring within the reps variable
        exercises_with_10_reps.append(exercise.get("Exercise", "Unnamed Exercise")) #adds the name of an exercise to the list called "exerise_with_10_reps"

# Print the exercises that require 10 reps 
print("Exercises that require exactly 10 reps:")
print(exercises_with_10_reps)