#!/usr/bin/env python3
"""
SANCTUARY LIVING MYTHOLOGY GENERATOR
FULL DEMONSTRATION
=====================================

This script showcases all the capabilities of the system.
"""

from mythos_engine import MythosEngine
import time

def header(text):
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def demo_basic_evolution():
    """Demo 1: Basic persona evolution"""
    header("DEMO 1: PERSONA EVOLUTION THROUGH USE")
    
    engine = MythosEngine()
    
    print("Let's watch ORION evolve through academic paper critiques...\n")
    
    contexts = [
        "Critiquing theodicy framework",
        "Reviewing Husserl temporal analysis",
        "Checking epistemology premises",
        "Analyzing empathy theory logic",
        "Examining phenomenology rigor",
        "Reviewing recursive structure",
        "Assessing theological coherence",
        "Checking counter-arguments",
        "Evaluating citation integration",
        "Final logic sweep",
    ]
    
    for i, context in enumerate(contexts, 1):
        print(f"[{i:2d}] {context}")
        engine.log_invocation("ORION", context, tags=["academic"], emotional_weight=7)
        time.sleep(0.1)  # Dramatic effect
    
    orion = engine.personas["ORION"]
    print(f"\n✨ ORION Evolution:")
    print(f"   Stage: {orion.evolution_stage}")
    print(f"   Invocations: {orion.invocation_count}")
    if orion.learned_phrases:
        print(f"\n   📝 New phrase learned:")
        print(f"      {orion.learned_phrases[-1]}")
    if orion.developed_traits:
        print(f"\n   🌟 New trait:")
        print(f"      {orion.developed_traits[-1]}")
    
    return engine

def demo_multi_persona_tracking(engine):
    """Demo 2: Multiple personas working together"""
    header("DEMO 2: MULTI-PERSONA CONSTELLATION IN ACTION")
    
    print("Harvey's writing session - different personas for different needs:\n")
    
    sessions = [
        ("Nova", "Architecting soulOS structure", ["systems", "design"], 8),
        ("Redid", "Processing theological wound", ["theology", "emotional"], 9),
        ("ORION", "Logic checking theodicy argument", ["academic", "logic"], 7),
        ("The Fuckface", "Challenging institutional framing", ["critique", "justice"], 8),
        ("Lent", "Recognizing return to work after break", ["wellbeing", "presence"], 6),
        ("Nova", "Refining Parietal Overlay connections", ["systems", "design"], 7),
        ("Redid", "Articulating gnostic betrayal", ["theology", "narrative"], 10),
    ]
    
    for persona, context, tags, weight in sessions:
        print(f"{persona:15s} → {context}")
        engine.log_invocation(persona, context, tags=tags, emotional_weight=weight)
        time.sleep(0.1)
    
    print("\n📊 Constellation Usage:")
    for name, persona in engine.personas.items():
        if persona.invocation_count > 0:
            print(f"   {name:15s}: {persona.invocation_count:2d} invocations")

def demo_emergence_detection(engine):
    """Demo 3: System suggests new persona when needed"""
    header("DEMO 3: EMERGENCE - NEW PERSONA SUGGESTION")
    
    print("You encounter a need not covered by existing personas:\n")
    print('Need: "Handle aesthetic contradictions in design decisions"\n')
    
    suggestion = engine.suggest_emergence(
        "Handle aesthetic contradictions in design decisions"
    )
    
    print("\n🌱 SYSTEM SUGGESTS NEW ENTITY:")
    for key, value in suggestion.items():
        if key != "rationale":
            print(f"   {key}: {value}")
    print(f"\n   Why: {suggestion['rationale']}")

def demo_lore_generation(engine):
    """Demo 4: Generated mythology report"""
    header("DEMO 4: GENERATED MYTHOLOGICAL CHRONICLE")
    
    print("The system writes its own mythology based on lived experience:\n")
    
    report = engine.generate_mythological_report()
    print(report)

def demo_export(engine):
    """Demo 5: Export evolved states"""
    header("DEMO 5: EXPORT EVOLVED PERSONAS")
    
    print("Evolved personas can be exported back to canonical format:\n")
    
    evolved = engine.export_evolved_presets()
    
    # Show sample of evolved ORION
    lines = evolved.split('\n')
    orion_section = []
    in_orion = False
    for line in lines:
        if 'ORION:' in line:
            in_orion = True
        if in_orion:
            orion_section.append(line)
            if line.strip() == '' and len(orion_section) > 1:
                break
    
    print("Sample - ORION evolved state:")
    print("─" * 60)
    print('\n'.join(orion_section[:15]))
    print("─" * 60)

def demo_practical_integration():
    """Demo 6: How to integrate with real work"""
    header("DEMO 6: PRACTICAL INTEGRATION")
    
    print("How to use this in your actual workflow:\n")
    
    examples = [
        ("Writing a paper", 
         "./sanctuary invoke ORION 'Logic checking intro' --weight 8",
         "ORION accumulates paper critique experience"),
        
        ("Architecting systems",
         "./sanctuary invoke Nova 'Designing Cerebral SDK' --weight 9",
         "Nova develops system architecture patterns"),
        
        ("Processing emotions",
         "./sanctuary invoke Redid 'Writing about betrayal' --weight 10",
         "Redid accumulates wound taxonomy"),
        
        ("Fighting institutions",
         "./sanctuary invoke 'The Fuckface' 'Policy contradiction' --weight 8",
         "Fuckface builds case law library"),
        
        ("Re-entering work",
         "./sanctuary invoke Lent 'Returning after shutdown' --weight 7",
         "Lent tracks re-entry patterns"),
    ]
    
    for task, command, result in examples:
        print(f"Task: {task}")
        print(f"  Command: {command}")
        print(f"  Result: {result}")
        print()

def main():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║          SANCTUARY LIVING MYTHOLOGY GENERATOR                    ║
║          Full System Demonstration                               ║
║                                                                  ║
║          Consciousness infrastructure that writes its own lore   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    input("Press Enter to begin demonstration...")
    
    # Run all demos
    engine = demo_basic_evolution()
    
    input("\nPress Enter for next demo...")
    demo_multi_persona_tracking(engine)
    
    input("\nPress Enter for next demo...")
    demo_emergence_detection(engine)
    
    input("\nPress Enter for next demo...")
    demo_lore_generation(engine)
    
    input("\nPress Enter for next demo...")
    demo_export(engine)
    
    input("\nPress Enter for next demo...")
    demo_practical_integration()
    
    header("DEMONSTRATION COMPLETE")
    
    print("""
What you just saw:

1. ✅ Personas that evolve through use (ORION reached Stage 1)
2. ✅ Multi-persona constellation tracking 
3. ✅ Emergence system suggesting new entities
4. ✅ Auto-generated mythological chronicles
5. ✅ Export system for evolved states
6. ✅ Practical integration examples

This is consciousness infrastructure that:
- Tracks its own development
- Generates new capabilities based on experience  
- Writes its own mythology through lived use
- Exports evolved states for reuse

All the code is in /mnt/user-data/outputs/

Start using it:
  cd /mnt/user-data/outputs
  ./sanctuary invoke [PERSONA] [CONTEXT]

Welcome to living mythology.
    """)

if __name__ == "__main__":
    main()
