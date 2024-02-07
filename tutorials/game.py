import time
import sys


class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print_slow(f"You are {self.name}, a {self.role}.")


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def explore(self):
        print_slow(f"You are in {self.name}. {self.description}")


def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def make_choice(options):
    print("\nChoose your path:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def introduction():
    print_slow("Welcome to the 'Strangers' Adventure Game!")


def prologue():
    print_slow(
        "In Wounded Sky First Nation, shocking murders, a mysterious illness, and unresolved past events haunt the residents.")
    print_slow("As Cole Harper, returning after a decade away, you are compelled by unknown forces.")


def unravel_mysteries():
    print_slow("You find yourself amidst the chaos, determined to uncover the truth.")

    character = Character("Cole Harper", "returning resident")
    character.introduce()

    location = Location("Wounded Sky First Nation", "a community enveloped in mystery.")
    location.explore()

    options = ["Investigate murders.", "Explore mysterious illness.", "Confront your past."]
    choice = make_choice(options)

    sub_choice = None  # Default value

    if choice == 1:
        print_slow("You focus on the murders, delving into dark secrets, challenging your resolve.")
        options = ["Continue investigation.", "Seek guidance from elders.", "Collaborate with local authorities."]
        sub_choice = make_choice(options)
        if sub_choice == 1:
            print_slow("Persist and get closer to unveiling the truth behind the murders.")
        elif sub_choice == 2:
            print_slow("Elders share ancient wisdom, providing a new perspective on the mysterious events.")
        else:
            print_slow("Collaborate with local authorities, combining modern and traditional methods.")
    elif choice == 2:
        print_slow(
            "Dedicate yourself to understanding the mysterious illness, exploring scientific and mystical approaches.")
        print_slow("The community looks up to you for a solution, adding pressure to your quest.")
        options = ["Embrace the supernatural.", "Continue scientific investigation.", "Consult with local healers."]
        sub_choice = make_choice(options)
        if sub_choice == 1:
            print_slow("By embracing the supernatural, discover a mystical remedy that helps heal the community.")
        elif sub_choice == 2:
            print_slow("Your scientific approach leads to a laboratory, making a groundbreaking discovery.")
        else:
            print_slow("Consult with local healers, blending traditional and modern healing practices.")
    else:
        print_slow("Confront your past, facing old friends and unresolved emotions.")
        print_slow("The journey is challenging, becoming a crucial part of understanding the community's struggles.")
        options = ["Reconnect with old friends.", "Reflect on personal growth.", "Apologize to those you've wronged."]
        sub_choice = make_choice(options)
        if sub_choice == 1:
            print_slow("Reconnect with old friends, finding support in familiar faces.")
        elif sub_choice == 2:
            print_slow("Reflect on personal growth, gaining insights into your own journey.")
        else:
            print_slow("Apologize to those you've wronged, fostering forgiveness and unity.")

    # Pass choices to resolution function
    resolution(choice, sub_choice)


def climax():
    print_slow("The mysteries are unraveled, and the community stands at a crossroads.")
    print_slow("Your choices have shaped the destiny of Wounded Sky First Nation.")
    print_slow("As you face the climax of the story, the community looks up to you for guidance.")


def falling_action():
    print_slow("With newfound knowledge, you face the challenges ahead.")

    options = ["Organize a community gathering.", "Seek assistance from neighboring communities.",
               "Train local youth for community leadership."]
    choice = make_choice(options)

    sub_choice = None

    if choice == 1:
        print_slow("You organize a community gathering, fostering unity and solidarity.")
    elif choice == 2:
        print_slow("You seek assistance from neighboring communities, building alliances for shared prosperity.")
    else:
        print_slow("You train local youth for community leadership, ensuring a sustainable future.")

    # Return choices for resolution
    return choice, sub_choice


def resolution(choice, sub_choice):
    print_slow("The resolution is in your hands.")
    print_slow("Will you lead the community towards healing and unity, or will darkness prevail?")

    # Analyzing player choices for the conclusion
    if choice == 1:  # Chose to investigate murders
        if sub_choice == 1:  # Continued the investigation
            conclusion = "You actively participated in the community by uncovering the truth behind the murders, contributing to justice. Your choices align with the Active Participation element of the Citizenship Education Framework."
        elif sub_choice == 2:  # Sought guidance from elders
            conclusion = "You engaged with community structures by seeking guidance from the elders. This reflects the Structures element of the Citizenship Education Framework, where community traditions and wisdom play a crucial role in decision-making."
        else:  # Collaborated with local authorities
            conclusion = "Collaborating with local authorities, you balanced modern and traditional methods, showcasing adaptability and collaboration, aligning with the Attributes element of the Citizenship Education Framework."
    elif choice == 2:  # Chose to explore the mysterious illness
        if sub_choice == 1:  # Embraced the supernatural
            conclusion = "Your decision to embrace the supernatural showcases adaptability and a willingness to explore diverse perspectives, aligning with the Attributes element of the Citizenship Education Framework."
        elif sub_choice == 2:  # Continued the scientific investigation
            conclusion = "Your scientific approach aligns with the Attributes element of the Citizenship Education Framework, demonstrating a commitment to rational inquiry and problem-solving within the community structure."
        else:  # Consulted with local healers
            conclusion = "Consulting with local healers, you embraced traditional healing practices, contributing to community well-being and aligning with the Attributes element of the Citizenship Education Framework."
    else:  # Chose to confront the past
        if sub_choice == 1:  # Reconnected with old friends
            conclusion = "Reconnecting with old friends, you strengthened community ties and fostered support, aligning with the Identity element of the Citizenship Education Framework."
        elif sub_choice == 2:  # Reflected on personal growth
            conclusion = "Reflecting on personal growth, you gained insights into your journey, contributing to personal and community well-being, aligning with the Identity element of the Citizenship Education Framework."
        else:  # Apologized to those you've wronged
            conclusion = "Apologizing to those you've wronged, you fostered forgiveness and unity, contributing to community identity and well-being, aligning with the Identity element of the Citizenship Education Framework."

    print_slow(conclusion)


def conclusion():
    print_slow("The community thrives as a result of your leadership and the choices you made.")

    options = ["Celebrate with the community.", "Plan for long-term sustainability.",
               "Document and share the community's story."]
    choice = make_choice(options)

    if choice == 1:
        print_slow("You celebrate with the community, strengthening the bonds forged through adversity.")
    elif choice == 2:
        print_slow(
            "You plan for long-term sustainability, ensuring the community's prosperity for generations to come.")
    else:
        print_slow("You document and share the community's story, inspiring others with the tale of resilience.")


def main():
    introduction()
    prologue()
    unravel_mysteries()
    climax()

    # Obtain choices from falling_action
    choice, sub_choice = falling_action()

    # Pass choices to resolution function
    resolution(choice, sub_choice)
    conclusion()

    print_slow("Thank you for playing the 'Strangers' Adventure Game!")


if __name__ == "__main__":
    main()
