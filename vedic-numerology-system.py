import datetime

class VedicNumerology:
    def __init__(self, name, birth_date):
        self.name = name.upper()
        self.birth_date = birth_date
        self.numerology_chart = {
            1: "Sun", 2: "Moon", 3: "Jupiter", 4: "Rahu", 5: "Mercury",
            6: "Venus", 7: "Ketu", 8: "Saturn", 9: "Mars"
        }

    def calculate_life_path_number(self):
        return sum(int(char) for char in self.birth_date.strftime("%d%m%Y") if char.isdigit()) % 9 or 9

    def get_ruling_planet(self, number):
        return self.numerology_chart[number]

    def create_lo_shu_grid(self):
        birth_date_str = self.birth_date.strftime("%d%m%Y")
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        lo_shu_positions = {1: (2, 0), 2: (1, 1), 3: (0, 2), 4: (0, 1), 5: (1, 1), 
                            6: (2, 1), 7: (0, 0), 8: (1, 0), 9: (2, 2)}
        
        for digit in birth_date_str:
            num = int(digit)
            if num != 0:
                row, col = lo_shu_positions[num]
                grid[row][col] += 1
        
        return grid

    def analyze_lo_shu_grid(self, grid):
        analysis = {
            "Horizontal": self.analyze_lines(grid),
            "Vertical": self.analyze_lines(list(map(list, zip(*grid)))),
            "Diagonal": self.analyze_diagonals(grid),
            "Missing Numbers": self.find_missing_numbers(grid),
            "Repeat Numbers": self.find_repeat_numbers(grid)
        }
        return analysis

    def analyze_lines(self, lines):
        return [sum(line) for line in lines]

    def analyze_diagonals(self, grid):
        return [sum(grid[i][i] for i in range(3)), sum(grid[i][2-i] for i in range(3))]

    def find_missing_numbers(self, grid):
        flat_grid = [num for row in grid for num in row]
        return [i for i in range(1, 10) if i not in flat_grid]

    def find_repeat_numbers(self, grid):
        flat_grid = [num for row in grid for num in row]
        return [i for i in range(1, 10) if flat_grid.count(i) > 1]

    def interpret_lo_shu_grid(self, analysis):
        interpretations = []
        
        # Interpret horizontal lines
        for i, sum_value in enumerate(analysis["Horizontal"]):
            if sum_value == 0:
                interpretations.append(f"Horizontal line {i+1} is empty, indicating potential challenges in that area of life.")
            elif sum_value > 3:
                interpretations.append(f"Horizontal line {i+1} is strong, suggesting good energy in that life aspect.")
        
        # Interpret vertical lines
        for i, sum_value in enumerate(analysis["Vertical"]):
            if sum_value == 0:
                interpretations.append(f"Vertical line {i+1} is empty, possibly indicating a lack in that area of life.")
            elif sum_value > 3:
                interpretations.append(f"Vertical line {i+1} is powerful, suggesting strength in that life domain.")
        
        # Interpret diagonals
        for i, sum_value in enumerate(analysis["Diagonal"]):
            if sum_value == 0:
                interpretations.append(f"Diagonal {i+1} is empty, which might indicate imbalance.")
            elif sum_value > 3:
                interpretations.append(f"Diagonal {i+1} is strong, suggesting good overall balance and energy flow.")
        
        # Interpret missing numbers
        if analysis["Missing Numbers"]:
            interpretations.append(f"Missing numbers {analysis['Missing Numbers']} suggest areas for personal growth.")
        
        # Interpret repeat numbers
        if analysis["Repeat Numbers"]:
            interpretations.append(f"Repeat numbers {analysis['Repeat Numbers']} indicate amplified energies in those areas.")
        
        return interpretations

    def suggest_remedies(self, analysis):
        remedies = []
        
        for missing in analysis["Missing Numbers"]:
            if missing == 1:
                remedies.append("To boost the Sun energy (1), spend more time outdoors and work on self-confidence.")
            elif missing == 2:
                remedies.append("To enhance Moon energy (2), practice meditation and work on emotional balance.")
            elif missing == 3:
                remedies.append("To increase Jupiter energy (3), focus on personal growth and learning new skills.")
            elif missing == 4:
                remedies.append("To strengthen Rahu energy (4), embrace change and take calculated risks.")
            elif missing == 5:
                remedies.append("To boost Mercury energy (5), improve communication skills and mental agility.")
            elif missing == 6:
                remedies.append("To enhance Venus energy (6), focus on relationships and creative pursuits.")
            elif missing == 7:
                remedies.append("To increase Ketu energy (7), practice spirituality and self-reflection.")
            elif missing == 8:
                remedies.append("To strengthen Saturn energy (8), work on discipline and long-term planning.")
            elif missing == 9:
                remedies.append("To boost Mars energy (9), engage in physical activities and assertiveness training.")
        
        return remedies

    def analyze(self):
        life_path = self.calculate_life_path_number()
        lo_shu_grid = self.create_lo_shu_grid()
        grid_analysis = self.analyze_lo_shu_grid(lo_shu_grid)
        
        analysis = {
            "Name": self.name,
            "Birth Date": self.birth_date.strftime("%d-%m-%Y"),
            "Life Path Number": {
                "Number": life_path,
                "Ruling Planet": self.get_ruling_planet(life_path),
                "Significance": self.get_life_path_significance(life_path)
            },
            "Lo Shu Grid": lo_shu_grid,
            "Grid Analysis": grid_analysis,
            "Interpretations": self.interpret_lo_shu_grid(grid_analysis),
            "Remedies": self.suggest_remedies(grid_analysis)
        }
        return analysis

    def get_life_path_significance(self, number):
        significances = {
            1: "Leadership, independence, and individuality.",
            2: "Cooperation, diplomacy, and sensitivity.",
            3: "Creativity, self-expression, and optimism.",
            4: "Stability, hard work, and practicality.",
            5: "Freedom, adaptability, and progressive thinking.",
            6: "Responsibility, harmony, and nurturing.",
            7: "Analysis, understanding, and spiritual awareness.",
            8: "Personal power, authority, and material success.",
            9: "Humanitarianism, compassion, and artistic talents."
        }
        return significances.get(number, "Unknown life path significance.")

def display_analysis(analysis):
    print("\nComprehensive Vedic Numerology Analysis:")
    print(f"\nName: {analysis['Name']}")
    print(f"Birth Date: {analysis['Birth Date']}")
    
    print("\nLife Path Number:")
    print(f"  Number: {analysis['Life Path Number']['Number']}")
    print(f"  Ruling Planet: {analysis['Life Path Number']['Ruling Planet']}")
    print(f"  Significance: {analysis['Life Path Number']['Significance']}")
    
    print("\nLo Shu Grid:")
    for row in analysis['Lo Shu Grid']:
        print("  " + " ".join(str(num) for num in row))
    
    print("\nGrid Analysis:")
    for key, value in analysis['Grid Analysis'].items():
        print(f"  {key}: {value}")
    
    print("\nInterpretations:")
    for interpretation in analysis['Interpretations']:
        print(f"  - {interpretation}")
    
    print("\nRemedies:")
    for remedy in analysis['Remedies']:
        print(f"  - {remedy}")

# Example usage
if __name__ == "__main__":
    name = input("Enter your full name: ")
    birth_date_str = input("Enter your birth date (DD-MM-YYYY): ")
    birth_date = datetime.datetime.strptime(birth_date_str, "%d-%m-%Y")

    vedic_analysis = VedicNumerology(name, birth_date)
    result = vedic_analysis.analyze()
    display_analysis(result)