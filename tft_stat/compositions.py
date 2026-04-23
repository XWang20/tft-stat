"""S17 team composition definitions.

Ported from XWang20/tft_data/analysis/team_comp/compositions.py.
Each comp has a key, display name, and a filter expression tree.

Hero augment comps (low-cost tanky carries) have `exclude_dmg_items_for`
listing unit IDs whose damage items should be excluded when analyzing
tank carry builds.  These tanky carries' BIS are tank items — damage
items on them are typically leftover/carousel items that add noise.
Use with `--exclude-dmg-items` in CLI.
"""

from __future__ import annotations

from tft_stat.filter_expr import Item, Trait, Unit

COMPOSITIONS = {
    # --- 5 costs ---
    "nova_95": {
        "name": "N.O.V.A. 95 / 新星 95",
        "filter": (
            (Unit('TFT17_Fiora', item_min=3, item_max=3)
             | Unit('TFT17_Vex', item_min=3, item_max=3)
             | Unit('TFT17_Graves', item_min=3, item_max=3))
            & Trait('TFT17_DRX', min_units=2)
            & ~Trait('TFT17_Mecha', min_units=4)
            & ~Unit('TFT17_Kindred')
            & ~Unit('TFT17_Aurora', item_min=3, item_max=3)
            & ~Unit('TFT17_MasterYi', item_min=3, item_max=3)
            & ~Unit('TFT17_Zed')
        ),
    },
    "vex_95": {
        "name": "Vex 95 / 薇古丝 95",
        "filter": (
            Unit('TFT17_Vex', item_min=3, item_max=3)
            & Unit('TFT17_Blitzcrank')
            & Unit('TFT17_Mordekaiser')
            & ~Unit('TFT17_Leblanc')
            & ~Trait('TFT17_DRX', min_units=2)
            & ~Unit('TFT17_Jhin', item_min=3, item_max=3)
        ),
    },
    "zed": {
        "name": "Zed / 劫",
        "filter": Unit('TFT17_Zed', item_min=3, item_max=3),
    },

    # --- 4 costs ---
    "dark_star": {
        "name": "Dark Star / 暗星",
        "filter": (
            Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Kaisa', star_min=3, star_max=3)
            & ~Unit('TFT17_Chogath', star_min=3, star_max=3)
        ),
    },
    "space_groove": {
        "name": "Space Groove / 太空律动",
        "filter": (
            (Unit('TFT17_Nami', item_min=3, item_max=3)
             | Unit('TFT17_Samira', item_min=3, item_max=3))
            & Trait('TFT17_SpaceGroove', min_units=5)
            & ~Unit('TFT17_Nasus', item_min=3, item_max=3, star_min=3, star_max=3)
        ),
    },
    "meeple_corki": {
        "name": "Meeple Corki / 木灵族库奇",
        "filter": (
            Unit('TFT17_Corki', item_min=3, item_max=3)
            & Trait('TFT17_Astronaut', min_units=5)
            & ~Unit('TFT17_Veigar', item_min=3, item_max=3)
            & ~Unit('TFT17_IvernMinion', item_min=3, item_max=3, star_min=3, star_max=3)
            & ~Unit('TFT17_Poppy', item_min=3, item_max=3)
        ),
    },
    "mecha": {
        "name": "Mecha ASOL / 霸天机甲",
        "filter": (
            Trait('TFT17_Mecha', min_units=6, max_units=6)
            & Unit('TFT17_AurelionSol', item_min=2)
            & Unit('TFT17_Galio', item_min=2)
        ),
    },
    "vanguard_leblanc": {
        "name": "Vanguard LeBlanc / 重装妖姬",
        "filter": (
            Unit('TFT17_Leblanc', item_min=3, item_max=3)
            & Trait('TFT17_ShieldTank', min_units=2)
            & Trait('TFT17_SummonTrait', min_units=3, max_units=3)
            & ~Unit('TFT17_Diana', item_min=3, item_max=3)
            & ~Unit('TFT17_Nasus', item_min=3, item_max=3)
            & ~Unit('TFT17_Zoe', item_min=3, item_max=3)
            & ~Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Unit('TFT17_Vex', item_min=3, item_max=3)
        ),
    },
    "shepherd": {
        "name": "Shepherd / 牧羊人",
        "filter": (
            Trait('TFT17_SummonTrait', min_units=5)
            & ~Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Unit('TFT17_Lissandra', item_min=3, item_max=3)
        ),
    },
    "nova_yi": {
        "name": "N.O.V.A. Yi / 新星 易",
        "filter": (
            (Unit('TFT17_MasterYi', item_min=3, item_max=3)
             | Unit('TFT17_Kindred', item_min=3, item_max=3))
            & Trait('TFT17_DRX', min_units=2)
            & ~Trait('TFT17_Primordian', min_units=2)
            & ~Unit('TFT17_Aatrox', item_min=3, item_max=3, star_min=3, star_max=3)
        ),
    },
    "xayah": {
        "name": "Xayah / 霞",
        "filter": (
            Unit('TFT17_Xayah', item_min=3, item_max=3)
            & ~Unit('TFT17_Lulu', item_min=3, item_max=3)
            & ~Unit('TFT17_Samira', item_min=3, item_max=3)
            & ~Unit('TFT17_Jax', item_min=3, item_max=3)
            & ~Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Ezreal', item_min=3, item_max=3)
        ),
    },
    "voyager": {
        "name": "Voyager Nami / 旅人娜美",
        "filter": (
            Unit('TFT17_Karma')
            & Unit('TFT17_Nami')
            & Unit('TFT17_Lissandra')
            & ~Unit('TFT17_Veigar')
            & ~Unit('TFT17_Pyke', item_min=3, item_max=3)
            & ~Unit('TFT17_IvernMinion', item_min=3, item_max=3)
            & ~Unit('TFT17_Viktor', item_min=3, item_max=3)
            & ~Unit('TFT17_Aurora', item_min=3, item_max=3)
            & ~Unit('TFT17_Leblanc')
            & ~Trait('TFT17_DarkStar', min_units=4)
        ),
    },

    # --- 3 costs ---
    "conduit_mf": {
        "name": "Conduit MF / 神谕女枪",
        "filter": (
            Unit('TFT17_MissFortune', item_min=2)
            & Trait('TFT17_ManaTrait', min_units=2)
        ),
    },
    "lulu": {
        "name": "Lulu Reroll / 璐璐",
        "filter": (
            Unit('TFT17_Lulu', item_min=3, item_max=3)
            & (Trait('TFT17_Stargazer_Mountain', min_units=3)
               | Trait('TFT17_Stargazer_Medallion', min_units=3)
               | Trait('TFT17_Stargazer_Shield', min_units=3)
               | Trait('TFT17_Stargazer_Wolf', min_units=3)
               | Trait('TFT17_Stargazer_Fountain', min_units=3)
               | Trait('TFT17_Stargazer_Huntress', min_units=3)
               | Trait('TFT17_Stargazer_Serpent', min_units=3))
            & ~Item('TFT_Item_GuinsoosRageblade', carrier_unit_id='TFT17_Jax')
            & ~Unit('TFT17_MissFortune')
        ),
    },
    "anima_diana": {
        "name": "Anima Diana / 幻灵皎月",
        "filter": (
            (Unit('TFT17_Aurora', item_min=3, item_max=3)
             | Unit('TFT17_Diana', item_min=3, item_max=3))
            & Unit('TFT17_Diana')
            & Trait('TFT17_AnimaSquad', min_units=3)
        ),
    },
    "viktor": {
        "name": "Viktor / 维克托",
        "filter": (
            Unit('TFT17_Viktor', item_min=3, item_max=3)
            & ~Unit('TFT17_MissFortune')
            & ~Unit('TFT17_Pyke', item_min=3, item_max=3)
            & ~Unit('TFT17_MasterYi', item_min=3, item_max=3)
        ),
    },
    "kaisa": {
        "name": "Kai'Sa Reroll / 卡莎",
        "filter": Unit('TFT17_Kaisa', item_min=3, item_max=3),
    },
    "two_tanky_samira": {
        "name": "Two Tanky Samira / 成双莎弥拉",
        "filter": Unit('TFT17_Samira', count=2),
    },

    # --- 2 costs ---
    "pyke": {
        "name": "Pyke Reroll / 派克",
        "filter": (
            Unit('TFT17_Pyke', item_min=3, item_max=3)
            & ~Unit('TFT17_Viktor', item_min=3, item_max=3)
        ),
    },
    "reach_for_the_stars": {
        "name": "Reach for the Stars / 摘星之志",
        "filter": Unit('TFT17_Jax', item_min=3, item_max=3),
        "exclude_dmg_items_for": ["TFT17_Jax"],
    },
    "the_big_bang": {
        "name": "The Big Bang / 宇宙大爆炸",
        "filter": Unit('TFT17_IvernMinion', item_min=3, item_max=3),
        "exclude_dmg_items_for": ["TFT17_IvernMinion"],
    },
    "primordian": {
        "name": "Primordian Reroll / 海魔人",
        "filter": (
            (Unit('TFT17_Belveth', item_min=3, item_max=3)
             | Unit('TFT17_Akali', item_min=3, item_max=3))
            & Trait('TFT17_Primordian', min_units=2)
        ),
    },

    # --- 1 costs ---
    "bonk": {
        "name": "Bonk! / 邦！",
        "filter": Unit('TFT17_Nasus', item_min=3, item_max=3),
        "exclude_dmg_items_for": ["TFT17_Nasus"],
    },
    "stellar_combo": {
        "name": "Stellar Combo / 星界连招",
        "filter": Unit('TFT17_Aatrox', item_min=3, item_max=3),
        "exclude_dmg_items_for": ["TFT17_Aatrox"],
    },
    "termeepnal_velocity": {
        "name": "Termeepnal Velocity / 飙速木灵",
        "filter": Unit('TFT17_Poppy', item_min=3, item_max=3),
        "exclude_dmg_items_for": ["TFT17_Poppy"],
    },
    "ez_chogath": {
        "name": "EZ Cho'Gath Reroll / EZ科加斯",
        "filter": (
            (Unit('TFT17_Chogath', item_min=2)
             | Unit('TFT17_Pantheon', item_min=2))
            & Unit('TFT17_Ezreal', item_min=2)
        ),
    },
    "tf": {
        "name": "TF Reroll / 崔斯特",
        "filter": (
            Unit('TFT17_TwistedFate', item_min=2)
            & Unit('TFT17_Jax', item_min=2)
            & ~Item('TFT_Item_Bloodthirster', carrier_unit_id='TFT17_Aatrox')
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Jax')
        ),
    },
    "veigar": {
        "name": "Veigar Printer / 维迦",
        "filter": Unit('TFT17_Veigar', item_min=3, item_max=3),
    },
    "teemo": {
        "name": "Teemo Reroll / 提莫",
        "filter": (
            Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Item('TFT_Item_GuinsoosRageblade', carrier_unit_id='TFT17_Nasus')
        ),
    },
}
