from random import randint
import time

from move import Move
from game_data import type_key, type_chart
from pokemon import Pokemon


def roll_crit(i=None):
    """Rolls to determine if a move lands a critical hit. Critical hits boost damage by 1.5 ignore the attacker's negative stat stages,
    the defender's positive stat stages, and Light Screen/Reflect/Auorar Veil. Burn is not ignored."""
    if i is None or i < 0 or i > 24:
        i = randint(1, 24)
    if i == 1:
        print("A critical hit!")
        return 1.5
    else:
        return 1


def check_stab(user, attack):
    """Checks to see if the attacking move is the same type as the attacker. If so, attack power is boosted by 50%."""
    if attacker.typing[0] == attack.type or attacker.typing[1] == attack.type:
        return 1.5
    else:
        return 1


def check_type_effectiveness(user, target, attack):
    """Return the damage multiplier for how super effective the move is. type_chart is a matrix showing how each type matches up between each
    other. X-axis is the defending type, y-axis is the attacking type. Top left corner is (0, 0). Each type corresponds to a number on the
    x and y axis."""

    atk_id = type_key.get(attack.type)
    def1_id = type_key.get(target.typing[0])
    mult_1 = type_chart[atk_id][def1_id]
    try:
        def2_id = type_key.get(target.typing[1])
        mult_2 = type_chart[atk_id][def2_id]
    except:
        mult_2 = 1

    return mult_1 * mult_2


def random():

    pass


def calc_modified_base_damage():
    pass


def calc_modified_damage():
    pass


def activate_defog(player1, player2):
    """Using defog clears entry hazards from both sides of the field and lowers the opposing pokemon's evasion by 1."""
    player1.clear_hazards()
    player2.clear_hazards()
    print("The entry hazards were removed from the field!")
    player2.cur_pokemon.update_stat_modifier("evasion", -1)


"""General attack layout:
Switch:
Intimidate
Psychic Surge
Regenerator
Sand Stream
Grassy Surge

Before Damage Calc:
Sand Rush (should already be implemented)
Libero
Unseen Fist
Rock Blast
Grassy Glide



During Damage Calc:
Flash Fire
Psyshock
Eruption
Knock Off

Post Damage:
Static
High Jump Kick
Defog
Knock Off
Wood Hammer

Status effects:
Toxic
Defog
Slack Off
"""


def attack(attacker, n, defender):
    """Determines if a move hits and how much damage is dealt."""
    #  TODO: Critical hit ignore thes attacker's negative stat stages, the defender's positive stat stages, and Light Screen/Reflect/Auorar Veil.
    # print(f'{attacker.name} used {attacker.moves[n]["name"]}!')
    print(f"{attacker.name} used {attacker.moves[n].name}!")
    if accuracy_check(attacker, n, defender):
        crit = crit_check()
        stab = stab_check(attacker, n)
        typ = type_effectiveness_check(attacker, n, defender)
        burn = burn_check(attacker, n)

        if attacker.moves[n].category == "Physical":
            attack_stat = attacker.attack
            defense_stat = defender.defense
        elif attacker.moves[n].category == "Special":
            attack_stat = attacker.sp_attack
            defense_stat = defender.sp_defense

        damage = int(
            (
                int(
                    (
                        (int(2 * attacker.level / 5) + 2)
                        * int(attacker.moves[n].power)
                        * (attack_stat / defense_stat)
                    )
                    / 50
                )
                + 2
            )
            * crit
            * stab
            * typ
            * burn
        )

        defender.hp -= damage

        if typ > 1:
            print("It's super effective!")
        elif typ < 1 and typ > 0:
            print("It's not very effective...")
        elif typ == 0:
            print("It had no effect...")