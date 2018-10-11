class Bowling:
    def __init__(self):
        self.score = 0
        self.rolls = self.set_rolls()
        self.position = 0

# Gets the roll input from the user
    def set_rolls(self):
        tmprolls = []
        tmpstr = input("Input rolls: ")
        for i in range(len(tmpstr)):
            tmprolls.append(tmpstr[i])
        return tmprolls

# Checks if the first roll of the frame is a strike or not, cannot be a spare.
# If a strike it moves up one position (next frame).
# If its not a strike you get the score and move up two positions to the next frame.
    def run(self):
        for self.frame in range(10):
            if self.rolls[self.position] == "X":
                self.score += self.strike()
                self.position += 1

            elif self.rolls[self.position] == "/":
                print("Error: Spare Detected at begging of frame at position", self.position)
                print(self.rolls)
                exit()

            else:
                self.score += self.non_strike()
                self.position += 2
        print(self.score)
        return

# If the first roll is not a strike then add the current score plus the next pin to complete the frame
# If the second pin is a spare add up the rolls to ten and grab the next roll and add it as well
    def non_strike(self):
        if self.rolls[self.position + 1] == "/":
            return 10 + self.check_value(self.rolls[self.position + 2])

        if self.rolls[self.position + 1] == "X":
            print("Error: A strike cannot be in the second shot of a frame, error at", self.position)
            print(self.rolls)
            exit()

        else:
            return self.check_value(self.rolls[self.position]) + self.check_value(self.rolls[self.position + 1])

# A strike adds 10 then grabs the values of the next two rolls
    def strike(self):
        return 10 + self.check_value(self.rolls[self.position + 1]) + self.check_value(self.rolls[self.position + 2])

    def check_value(self, roll_value):
        if roll_value == "X":
            return 10
        elif roll_value == "/":
            return 10 - int(self.rolls[self.position + 1])
        elif roll_value == "-":
            return 0
        else:
            try:
                return int(roll_value)
            except ValueError:
                print("Error: Invalid character")
                exit()
