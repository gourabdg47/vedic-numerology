import datetime

class LoShuGrid:
    def __init__(self, birth_date):
        self.birth_date = birth_date
        self.grid = [
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
        ]
        self.birth_numbers = [int(char) for char in birth_date.strftime("%d%m%Y") if char.isdigit()]

    def calculate_grid(self):
        calculated_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for num in self.birth_numbers:
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j] == num:
                        calculated_grid[i][j] += 1
        return calculated_grid

    def draw_ascii_grid(self, grid):
        ascii_grid = """
+---+---+---+
| {} | {} | {} |
+---+---+---+
| {} | {} | {} |
+---+---+---+
| {} | {} | {} |
+---+---+---+
""".format(*[num if num > 0 else ' ' for row in grid for num in row])
        return ascii_grid

    def analyze_grid(self, grid):
        analysis = {
            "Mind Plane": sum(grid[0]),
            "Emotional Plane": sum(grid[1]),
            "Practical Plane": sum(grid[2]),
            "Thought Plane": sum(row[0] for row in grid),
            "Will Plane": sum(row[1] for row in grid),
            "Action Plane": sum(row[2] for row in grid),
            "Golden Yog": 1 if grid[0][0] > 0 and grid[1][1] > 0 and grid[2][2] > 0 else 0,
            "Silver Yog": 1 if grid[0][2] > 0 and grid[1][1] > 0 and grid[2][0] > 0 else 0,
            "Missing Numbers": [i for i in range(1, 10) if all(i not in row for row in grid)],
            "Repeated Numbers": [i for i in range(1, 10) if sum(row.count(i) for row in grid) > 1]
        }
        return analysis

    def interpret_analysis(self, analysis):
        interpretations = []
        
        planes = {
            "Mind Plane": ("rational and logical approach", "deficient in memory or impulsive"),
            "Emotional Plane": ("significant heavy emotions", "lack of emotional depth"),
            "Practical Plane": ("wealthy personality", "lack of material focus"),
            "Thought Plane": ("strong ability to generate ideas", "difficulty in idea generation"),
            "Will Plane": ("strong determination and potential", "lack of willpower"),
            "Action Plane": ("good at implementing ideas", "difficulty in taking action")
        }
        
        for plane, (positive, negative) in planes.items():
            if analysis[plane] == 3:
                interpretations.append(f"{plane}: Complete. You have a {positive}.")
            elif analysis[plane] == 0:
                interpretations.append(f"{plane}: Empty. You may have a {negative}.")
            else:
                interpretations.append(f"{plane}: Partially filled. You have some aspects of {positive}, but may also experience some {negative}.")
        
        if analysis["Golden Yog"]:
            interpretations.append("Golden Yog: Present. This indicates potential for name, fame, and money.")
        if analysis["Silver Yog"]:
            interpretations.append("Silver Yog: Present. This indicates potential for property and wealth, but also personal strengths and weaknesses.")
        
        if analysis["Missing Numbers"]:
            interpretations.append(f"Missing Numbers: {', '.join(map(str, analysis['Missing Numbers']))}. These areas of life may need more attention.")
        
        if analysis["Repeated Numbers"]:
            interpretations.append(f"Repeated Numbers: {', '.join(map(str, analysis['Repeated Numbers']))}. These areas may have an outsized influence in your life.")
        
        return interpretations

def main():
    birth_date_str = input("Enter your birth date (DD-MM-YYYY): ")
    birth_date = datetime.datetime.strptime(birth_date_str, "%d-%m-%Y")

    lo_shu = LoShuGrid(birth_date)
    calculated_grid = lo_shu.calculate_grid()
    
    print("\nYour Lo Shu Grid:")
    print(lo_shu.draw_ascii_grid(calculated_grid))
    
    analysis = lo_shu.analyze_grid(calculated_grid)
    interpretations = lo_shu.interpret_analysis(analysis)
    
    print("\nGrid Analysis:")
    for key, value in analysis.items():
        print(f"{key}: {value}")
    
    print("\nInterpretations:")
    for interpretation in interpretations:
        print(f"- {interpretation}")

if __name__ == "__main__":
    main()