# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define char1 = Character("Aayush")
# define char2 = Character("Anubhav")
define luna = Character("luna")
define zephyr = Character("zephyr")
define seraphiel = Character("seraphiel")
define orion = Character("orion")
define astra = Character("astra")



# The game starts here.
label start:

    # Opening Scene
    scene mountain with dissolve
    
    show luna at left
    play sound "st1.ogg"
    luna "The prophecy spoke of an artifact that could change the fate of Etherealis. I must find it and unlock its secrets."
    
    show zephyr at right
    play sound "st2.ogg"
    zephyr "Ah, Luna, my enchanting companion! Ready for another adventure, I presume?"
    
    luna "Always, Zephyr. We need to understand the Harmony Eclipse and the artifact's power."

    # Exploration
    
    # Add more scenes, characters, and dialogues here as Luna ventures through the magical world.
label forest_exploration:
    
    scene forest with dissolve
    
    show luna at center
    luna "The enchanted forest is filled with mysteries and wonders."

    show zephyr at right
    zephyr "Luna, do you sense the magic in the air? It's positively intoxicating!"

    menu:
        "Investigate a Glowing Tree":
            jump glowing_tree_scene
        "Continue Exploring":
            jump continue_exploring_scene
    

    # Alliance and Conflict
label continue_exploring_scene:
    scene cave1 with dissolve
    
    show seraphiel at center
    seraphiel "Leave, enchantress. The artifact's power is not meant for mortal hands."
    
    # Allow the player to make a choice
    menu:
        "Forge an alliance with Seraphiel":
            jump alliance_scene
        "Confront Seraphiel":
            jump conflict_scene

label glowing_tree_scene:

    scene tree with dissolve

    show luna at left
    luna "This tree emanates a powerful aura. I must investigate."

    menu:
        "Touch the Glowing Tree":
            jump touch_tree_scene
        "Observe from a Distance":
            jump observe_tree_scene

label touch_tree_scene:

    scene tree with dissolve

    show luna at left
    luna "As Luna touches the tree, a surge of magic courses through her."
    luna "I should go back"

    # Add consequences or discoveries based on the player's choice here

    jump forest_exploration

label observe_tree_scene:

    scene tree with dissolve

    show luna at left
    luna "Luna decides to observe the tree from a distance, wary of its power."

    # Add consequences or discoveries based on the player's choice here

    jump forest_exploration
    
# Scene: Forging an Alliance with Seraphiel
label alliance_scene:

    scene scared_ with dissolve

    show luna at left
    luna "Seraphiel, I sense that our paths have crossed for a reason. The artifact's power threatens Etherealis, and I believe we can only overcome this together."

    show seraphiel at right
    seraphiel "Enchantress, you tread on dangerous ground. The artifact's power is not to be underestimated. Why do you believe an alliance will make a difference?"

    luna "I've seen the shadows that lurk within the Harmony Eclipse. Alone, I fear I may succumb to its darkness. But together, we can balance its energy and protect Etherealis."

    show luna at center
    luna "Seraphiel, we must put aside our differences and work together. The fate of Etherealis depends on it."

    show seraphiel at center
    seraphiel "Your words hold weight, Luna. I too have witnessed the darkness within the artifact. But alliances are delicate, and trust must be earned. Prove to me that your intentions are pure."

    # Player choices for earning Seraphiel's trust
    menu:
        "Reveal Luna's Vulnerability":
            jump reveal_vulnerability_scene
        "Promise Mutual Protection":
            jump promise_protection_scene
        "Invoke a Shared Purpose":
            jump shared_purpose_scene

# Scene: Reveal Luna's Vulnerability
label reveal_vulnerability_scene:

    scene scared_ with dissolve

    show luna at left
    luna "Seraphiel, I carry the weight of my past. My vulnerabilities are laid bare before you. Trust in my sincerity as I trust in our shared mission."

    show seraphiel at right
    seraphiel "Vulnerability can be a strength. Your honesty resonates, Luna. Let us face this challenge together."

    # Add any consequences or decisions based on this revelation

    jump alliance_scene

# Scene: Promise Mutual Protection
label promise_protection_scene:

    scene scared_ with dissolve

    show luna at left
    luna "Seraphiel, I pledge to protect you as you protect me. Our strengths combined can shield Etherealis from the looming darkness."

    show seraphiel at right
    seraphiel "A mutual pledge. Your commitment is noted, Luna. Let our alliance be a beacon against the encroaching shadows."

    # Add any consequences or decisions based on this promise

    jump alliance_scene

# Scene: Invoke a Shared Purpose
label shared_purpose_scene:

    scene scared_ with dissolve

    show luna at left
    luna "Seraphiel, we share a common purpose - to safeguard Etherealis. Let our alliance be forged in the crucible of that purpose."

    show seraphiel at right
    seraphiel "A shared purpose can unite even the most unlikely allies. Your words resonate, Luna. Let our alliance stand firm against the coming storm."

    # Add any consequences or decisions based on this shared purpose

    jump revelations_scene


# Scene: Confronting Seraphiel
label conflict_scene:

    scene cave1 with dissolve

    show luna at left
    luna "Seraphiel, I understand your concerns, but the artifact's power must be harnessed for the greater good. We cannot shy away from our destiny."

    show seraphiel at right
    seraphiel "Luna, you underestimate the danger. The artifact's power can corrupt even the noblest intentions. I cannot allow it to fall into the wrong hands."

    luna "Seraphiel, I won't let the darkness consume me. We can find a way to use the artifact's power responsibly. Trust in our ability to guide its influence."

    # Player choices for the confrontation
    menu:
        "Appeal to Seraphiel's Trust":
            jump appeal_trust_scene
        "Challenge Seraphiel's Authority":
            jump challenge_authority_scene
        "Seek a Compromise":
            jump seek_compromise_scene

# Scene: Appeal to Seraphiel's Trust
label appeal_trust_scene:

    scene cave1 with dissolve

    show luna at left
    luna "Seraphiel, we must trust each other. I believe in the strength of our alliance. Together, we can overcome any challenge."

    show seraphiel at right
    seraphiel "Trust is earned, Luna. I need more than words to be convinced of your intentions."

    # Add any consequences or decisions based on this appeal

    jump continue_conflict_scene

# Scene: Challenge Seraphiel's Authority
label challenge_authority_scene:

    scene cave1 with dissolve

    show luna at left
    luna "Seraphiel, your caution borders on paranoia. I won't stand idly by while you dictate our path. I am an equal in this alliance."

    show seraphiel at right
    seraphiel "Equal or not, Luna, the artifact's power demands respect. I won't allow you to jeopardize everything for your own ambitions."

    # Add any consequences or decisions based on this challenge

    jump continue_conflict_scene

# Scene: Seek a Compromise
label seek_compromise_scene:

    scene cave1 with dissolve

    show luna at left
    luna "Seraphiel, let's find a compromise. A middle ground that allows us to harness the artifact's power while minimizing the risks. We can't afford to be divided."

    show seraphiel at right
    seraphiel "Compromise is a delicate balance, Luna. Convince me that your proposal ensures the safety of Etherealis."

    # Add any consequences or decisions based on this compromise

    jump continue_conflict_scene

# Continue with the conflict scene or jump to the next part of the script
label continue_conflict_scene:
    # Add continuation of the conflict scene or jump to the next part of the script
    luna "one thing i want to tell that dispite of what we are we should be one and act like nothing happen"

    "Everyone" "ok..."
    pass



label revelations_scene:

    # Scenes and dialogues for Luna uncovering hidden truths
    scene libraries with dissolve
    
    show orion at center
    orion "Luna, the Harmony Eclipse is both a blessing and a curse. The choices you make will determine Etherealis' destiny."

label climax_scene:

    # Scenes and dialogues for Luna confronting the artifact
    # scene libraries with dissolve
    hide orion
    show luna at center
    luna "This is it. The moment that will shape Etherealis' future."
    
    # Allow the player to make pivotal decisions
    menu:
        "Embrace the light within":
            jump light_ending
        "Succumb to darkness":
            jump dark_ending

label light_ending:

    # Scenes and dialogues for the ending where Etherealis flourishes
    scene light(1) with dissolve
    
    show zephyr at right
    zephyr "What path have you chosen, Luna?"
    
    show astra at left
    astra "The stars are watching. Your destiny is intertwined with Etherealis."

    # Add any additional scenes or dialogue for the prosperous ending

    return

label dark_ending:

    # Scenes and dialogues for the ending where Etherealis succumbs to darkness
    scene dark(1) with dissolve
    
    show zephyr at right
    zephyr "What have you done, Luna?"
    
    show astra at left
    astra "The stars weep for Etherealis. Your choices have led to eternal night."

    # Add any additional scenes or dialogue for the dark ending

    return

# ... Add any additional labels and scenes for the resolution and epilogue ...

# Finally, start the game from the beginning