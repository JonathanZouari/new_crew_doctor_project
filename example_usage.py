"""
Interactive Medical Diagnostic Assistant
Example usage script for the CrewAI Medical Diagnostic Team
"""

from crew import analyze_symptoms


def interactive_medical_assistant():
    """
    Run an interactive medical symptom analysis session.
    Prompts user for symptoms and provides diagnostic guidance.
    """
    print("\n" + "=" * 70)
    print("🏥 MEDICAL DIAGNOSTIC ASSISTANT")
    print("=" * 70)
    print("\nThis tool helps you understand your symptoms and prepare for")
    print("a doctor's appointment. It is NOT a substitute for professional care.")
    print("\n" + "=" * 70)

    print("\n📝 Please describe your symptoms in as much detail as possible.\n")
    print("Include:")
    print("  • Your age and gender")
    print("  • What symptoms you're experiencing")
    print("  • When they started and how they've progressed")
    print("  • Severity (1-10 scale)")
    print("  • What makes them better or worse")
    print("  • Any relevant medical history")
    print("  • Current medications")
    print("  • Recent illnesses, travel, or exposures")

    print("\n" + "-" * 70)
    print("Type your symptoms below (press Enter twice when done):")
    print("-" * 70 + "\n")

    # Collect multi-line input
    lines = []
    empty_line_count = 0

    while empty_line_count < 1:
        line = input()
        if line.strip() == "":
            empty_line_count += 1
        else:
            empty_line_count = 0
            lines.append(line)

    patient_input = "\n".join(lines).strip()

    if not patient_input:
        print("\n❌ No symptoms provided. Exiting.\n")
        return

    print("\n" + "=" * 70)
    print("🔄 ANALYZING YOUR SYMPTOMS...")
    print("=" * 70)
    print("\nThis may take 1-2 minutes as we:")
    print("  1. Process your symptom information")
    print("  2. Analyze from multiple medical specialty perspectives")
    print("  3. Generate personalized guidance")
    print("\nPlease wait...\n")

    try:
        result = analyze_symptoms(patient_input)

        print("\n" + "=" * 70)
        print("📄 YOUR PERSONALIZED DIAGNOSTIC GUIDANCE")
        print("=" * 70 + "\n")
        print(result)

        # Save option
        print("\n" + "=" * 70)
        save = input("\n💾 Save this report to a file? (y/n): ").strip().lower()

        if save == 'y':
            filename = input("Enter filename (or press Enter for 'diagnostic_report.txt'): ").strip()
            if not filename:
                filename = "diagnostic_report.txt"

            with open(filename, 'w', encoding='utf-8') as f:
                f.write("MEDICAL DIAGNOSTIC GUIDANCE REPORT\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"Patient Input:\n{patient_input}\n\n")
                f.write("=" * 70 + "\n\n")
                f.write(str(result))

            print(f"\n✅ Report saved to: {filename}")

        print("\n" + "=" * 70)
        print("⚕️  IMPORTANT REMINDER")
        print("=" * 70)
        print("\nThis analysis is for educational purposes only.")
        print("Please consult with a healthcare provider for proper diagnosis and treatment.")
        print("\nIf you have emergency symptoms, call 911 or go to the nearest ER.")
        print("\n" + "=" * 70 + "\n")

    except Exception as e:
        print("\n" + "=" * 70)
        print("❌ ERROR OCCURRED")
        print("=" * 70)
        print(f"\nAn error occurred during analysis: {str(e)}")
        print("\nPossible issues:")
        print("  • Check your .env file has valid OPENAI_API_KEY")
        print("  • Ensure you have internet connection")
        print("  • Verify crewai is properly installed")
        print("\nFor support, check the README.md file.\n")


def quick_example():
    """
    Run a quick example with pre-populated symptoms.
    """
    print("\n" + "=" * 70)
    print("🏥 QUICK EXAMPLE - Sample Patient Analysis")
    print("=" * 70 + "\n")

    sample_input = """
    I'm a 34-year-old female. For the past week, I've been experiencing severe
    fatigue and weakness. I feel exhausted even after a full night's sleep.
    I've also noticed I'm more short of breath than usual when climbing stairs,
    and my heart seems to race sometimes. I've been having headaches almost daily.

    I also noticed my skin looks paler than normal. I'm a vegetarian and have been
    for about 5 years. My periods have been heavier than usual for the past 3 months.

    I'm not on any medications currently. No known allergies. I don't have any
    chronic medical conditions that I know of. My mother has a history of anemia.
    """

    print("Sample Patient Input:")
    print("-" * 70)
    print(sample_input)
    print("-" * 70)

    print("\n🔄 Analyzing symptoms...\n")

    try:
        result = analyze_symptoms(sample_input)

        print("\n" + "=" * 70)
        print("📄 DIAGNOSTIC GUIDANCE")
        print("=" * 70 + "\n")
        print(result)

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nCheck your setup (API key, dependencies, etc.)")


def main_menu():
    """
    Display main menu and handle user choice.
    """
    while True:
        print("\n" + "=" * 70)
        print("🏥 MEDICAL DIAGNOSTIC ASSISTANT - MAIN MENU")
        print("=" * 70)
        print("\n1. Interactive Mode - Analyze Your Symptoms")
        print("2. Quick Example - See Sample Analysis")
        print("3. Exit")
        print("\n" + "=" * 70)

        choice = input("\nSelect option (1-3): ").strip()

        if choice == "1":
            interactive_medical_assistant()
        elif choice == "2":
            quick_example()
        elif choice == "3":
            print("\n👋 Thank you for using Medical Diagnostic Assistant!")
            print("Remember: Always consult healthcare professionals for medical concerns.\n")
            break
        else:
            print("\n❌ Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    print("\n" + "🩺" * 35)
    print("\n   PROFESSIONAL CREWAI MEDICAL DIAGNOSTIC TEAM")
    print("   Educational Symptom Analysis System")
    print("\n" + "🩺" * 35)

    main_menu()
