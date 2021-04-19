from pokemon import Pokemon
from player import Player

# TODO: If critical hit, ignores negative attack modifiers, positive defense modifiers, and defensive boosts from auroa veil, light screen, and reflect
# TODO: Add in light screen, reflect, and aurora veil
def calc_attack(team, crit):
    """Calculates the attack stat of the given pokemon by calculating its modified attack stat and mulitplying it with any additional modifiers.
    If the given attack roled a critical hit, a negative attack stat_mod is ignored and calc_modified_stat is not called.
    Additional modifiers are still applied."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1

    if cur_pokemon.item == "Choice Band":
        additional_modifier *= 1.5
    if cur_pokemon.status == "Burn":
        additional_modifier *= 0.5

    if crit == True and cur_pokemon.stat_mod["attack"] < 0:
        return int(cur_pokemon.stat["attack"] * additional_modifier)
    return int(cur_pokemon.calc_modified_stat("attack") * additional_modifier)


def calc_defense(team, crit):
    """Calculates the defense stat of the given pokemon by calculating its modified defense stat and mulitplying it with any additional modifiers.
    If the given attack roled a critical hit, a positive defense stat_mod is ignored and calc_modified_stat is not called.
    Additional modifiers are still applied."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1

    if crit == True and cur_pokemon.stat_mod["defense"] > 0:
        return int(cur_pokemon.stat["defense"] * additional_modifier)
    return int(cur_pokemon.calc_modified_stat("defense") * additional_modifier)


def calc_sp_attack(team, crit):
    """Calculates the special attack stat of the given pokemon by calculating its modified sp_attack stat and mulitplying it with any additional modifiers.
    If the given attack roled a critical hit, a negative sp_attack stat_mod is ignored and calc_modified_stat is not called.
    Additional modifiers are still applied."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1
    if cur_pokemon.item == "Choice Spec":
        additional_modifier *= 1.5
    if crit == True and cur_pokemon.stat_mod["sp_attack"] < 0:
        return int(cur_pokemon.stat["sp_attack"] * additional_modifier)
    return int(cur_pokemon.calc_modified_stat("sp_attack") * additional_modifier)


def calc_sp_defense(team, crit):
    """Calculates the special defense stat of the given pokemon by calculating its modified sp_defense stat and mulitplying it with any additional modifiers.
    If the given attack roled a critical hit, a positive sp_defense stat_mod is ignored and calc_modified_stat is not called.
    Additional modifiers are still applied."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1

    if crit == True and cur_pokemon.stat_mod["sp_defense"] > 0:
        return int(cur_pokemon.stat["sp_defense"] * additional_modifier)
    return int(cur_pokemon.calc_modified_stat("sp_defense") * additional_modifier)


def calc_speed(team, crit=False):
    """Calculates the speed stat of the given pokemon by calculating its modified speed stat and mulitplying it with any additional modifiers."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1
    if cur_pokemon.item == "Choice Scarf":
        additional_modifier *= 1.5
    if cur_pokemon.status == "Paralyzed":
        additional_modifier *= 0.5

    return int(cur_pokemon.calc_modified_stat("speed") * additional_modifier)


def calc_accuracy(team, crit=False):
    """Calculates the accuracy percentage of the given pokemon by calculating its modified accuaracy and multiplying it with any additional modifiers."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1
    return int(cur_pokemon.calc_modified_stat("accuracy") * additional_modifier)


def calc_evasion(team, crit=False):
    """Calculates the evasion percentage of the give pokemon by calculating its modified evasion and multiplying it with any additional modifiers."""
    cur_pokemon = team.cur_pokemon
    additional_modifier = 1
    return int(cur_pokemon.calc_modified_stat("evasion") * additional_modifier)
