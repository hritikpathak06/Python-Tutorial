# Dictionary and sets

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

car.clear()

car_copy = car.copy()


print(car)
print(car_copy)

marks = {
  "Ritik":23,
  "Rohit":25,
  "Kartik":77,
  "Aryan":100,
}

update_marks = marks.update({"Ritik":67})

print(marks)

print(marks["Rohit"],type(marks))
print(marks.keys())
print(marks.values())

print(marks.get("Ritik"))

# List in dict
students = [{
  "Ritik" :{
    "Science":67,
    "English":34,
    "Mathematics":56
  },
   "Kartik" :{
    "Science":97,
    "English":39,
    "Mathematics":96
  }
}]

ritik_marks = students[0]["Ritik"]

print(students)
print("Marks of ritik is: ",ritik_marks)



# ***********************SETS**************************************************

s = {1,2,3,4,56,7,5,5}

e= set();  #To declare a empty set in python

e.add("fruits")

print(s,type(s))

print(type(e),e)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.remove("apple")
x.pop()

print(x)

z = x.difference(y)

print(len(z),z) 

z = x.union(y);

z = x.intersection(y)

print(z)