import matplotlib.pyplot as plt
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=["blue", "green", "red", "purple", "orange", "cyan"])
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")
for i, value in enumerate(popularity):
    plt.text(i, value + 0.5, f"{value}%", ha="center")
plt.tight_layout()
plt.show()
