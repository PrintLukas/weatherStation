for entry in last24hours:
        print(entry)
print(len(last24hours))

dateX = []
for date in last24hours:
        dateX.append(date[1].strftime("%m-%d %H:%M"))

dateY = []
for date in last24hours:
        dateY.append(date[2])

x = dateX
y = dateY

# Checking and if so, deleting, old file

path = "/var/www/html/img/"
file = "plotTemp.png"

if os.path.exists(os.path.join(path, file)):
        os.system(f"rm {file}")
else:
        print("False")

# Create a line plot
plt.figure(figsize=(7.5,5))
plt.scatter(x, y, marker='o')
plt.tight_layout()
plt.xticks(rotation=45)
plt.title("temperature")
plt.xlabel("time")
plt.ylabel("temp")
plt.grid(True)
plt.savefig("/var/www/html/img/plotTemp.png")

dateY = []
for date in last24hours:
        dateY.append(date[4])

x = dateX
y = dateY

# Checking and if so, deleting, old file

path = "/var/www/html/img/"
file = "plotHumi.png"

if os.path.exists(os.path.join(path, file)):
        os.system(f"rm {file}")
else:
        print("False")

# Create a line plot
plt.figure(figsize=(7.5,5))
plt.scatter(x, y, marker='o')
plt.tight_layout()
plt.xticks(rotation=45)
plt.title("humidity")
plt.xlabel("time")
plt.ylabel("humid.")
plt.grid(True)
plt.savefig("/var/www/html/img/plotHumi.png")