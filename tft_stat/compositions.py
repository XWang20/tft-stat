"""Curated team composition definitions used by the analysis pipeline."""

from __future__ import annotations

from typing import Sequence

from tft_stat.filter_expr import Item, Trait, Unit
from tft_stat.models import CompositionDefinition

# All Stargazer variant trait IDs (S17 splits Stargazer into sub-types in ES)
_STARGAZER_IDS = (
    'TFT17_Stargazer_Mountain', 'TFT17_Stargazer_Medallion',
    'TFT17_Stargazer_Shield', 'TFT17_Stargazer_Wolf',
    'TFT17_Stargazer_Fountain', 'TFT17_Stargazer_Huntress',
    'TFT17_Stargazer_Serpent',
)


def _any_stargazer(min_units: int) -> Trait:
    """Build an OR over all Stargazer variant traits with the given min_units."""
    expr = Trait(_STARGAZER_IDS[0], min_units=min_units)
    for tid in _STARGAZER_IDS[1:]:
        expr = expr | Trait(tid, min_units=min_units)
    return expr


COMPOSITIONS: Sequence[CompositionDefinition] = (
    # 5 costs
    CompositionDefinition(
        key='nova_95',
        display_name_cn='新星 95',
        display_name_en='N.O.V.A. 95',
        carry_unit_id='TFT17_Fiora',
        carry_unit_cost=5,
        filter=(
            (Unit('TFT17_Fiora', item_min=2)
             | Unit('TFT17_Vex', item_min=2)
             | Unit('TFT17_Graves', item_min=2))
            & Trait('TFT17_DRX', min_units=2)
            & ~Trait('TFT17_Mecha', min_units=4)
            & ~Unit('TFT17_Kindred')
            & ~Unit('TFT17_Aurora', item_min=3, item_max=3)
            & ~Unit('TFT17_MasterYi', item_min=3, item_max=3)
            & ~Unit('TFT17_Zed')
            & ~Unit('TFT17_Corki')
            & ~Unit('TFT17_Xayah')
        ),
    ),
    CompositionDefinition(
        key='vex_95',
        display_name_cn='AP 95',
        display_name_en='AP 95',
        carry_unit_cost=5,
        filter=(
            (Unit('TFT17_Vex', item_min=2)
             | Unit('TFT17_Bard', item_min=2)
             | Unit('TFT17_Sona', item_min=2))
            & Unit('TFT17_Mordekaiser')
            & ~Unit('TFT17_Leblanc')
            & ~Trait('TFT17_DRX', min_units=2)
            & ~Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Veigar')
            & ~Item('TFT_Item_Bloodthirster', carrier_unit_id='TFT17_Leona')
            & ~Unit('TFT17_Xayah')
            & ~Unit('TFT17_Jhin', item_min=3, item_max=3)
            & ~Unit('TFT17_AurelionSol', item_min=3, item_max=3)
        ),
    ),
    CompositionDefinition(
        key='zed',
        display_name_cn='劫',
        display_name_en='Zed',
        carry_unit_id='TFT17_Zed',
        carry_unit_cost=5,
        filter=Unit('TFT17_Zed'),
    ),

    # 4 costs
    CompositionDefinition(
        key='dark_star',
        display_name_cn='暗星',
        display_name_en='Dark Star',
        carry_unit_id='TFT17_Karma',
        carry_unit_cost=4,
        filter=(
            Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Illaoi', item_min=3, item_max=3)
            & ~Unit('TFT17_Ezreal', item_min=3, item_max=3)
            & ~Unit('TFT17_Mordekaiser', star_min=3, star_max=3, item_min=3, item_max=3)
            & ~Unit('TFT17_Lissandra', star_min=3, star_max=3)
        ),
    ),
    CompositionDefinition(
        key='space_groove',
        display_name_cn='太空律动',
        display_name_en='Space Groove',
        carry_unit_cost=4,
        filter=(
            (Unit('TFT17_Nami', item_min=3, item_max=3)
             | Unit('TFT17_Samira', item_min=3, item_max=3))
            & Trait('TFT17_SpaceGroove', min_units=5)
            & ~Unit('TFT17_Nasus', item_min=3, item_max=3, star_min=3, star_max=3)
        ),
    ),
    CompositionDefinition(
        key='meeple_corki',
        display_name_cn='木灵族库奇',
        display_name_en='Meeple Corki',
        carry_unit_id='TFT17_Corki',
        carry_unit_cost=4,
        filter=(
            Unit('TFT17_Corki', item_min=3, item_max=3)
            & Trait('TFT17_Astronaut', min_units=5)
            & ~Unit('TFT17_Veigar', item_min=3, item_max=3)
            & ~Unit('TFT17_IvernMinion', item_min=3, item_max=3, star_min=3, star_max=3)
            & ~Unit('TFT17_Poppy', item_min=3, item_max=3)
            & ~Unit('TFT17_Zed')
            & ~Unit('TFT17_Gnar', item_min=3, item_max=3)
        ),
    ),
    CompositionDefinition(
        key='vanguard_asol',
        display_name_cn='走地龙王',
        display_name_en='Asol Non-Mech',
        carry_unit_id='TFT17_AurelionSol',
        carry_unit_cost=4,
        filter=(
            Unit('TFT17_AurelionSol', item_min=3, item_max=3)
            & ~Trait('TFT17_Mecha', min_units=4)
            & ~Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Leblanc')
        ),
    ),
    CompositionDefinition(
        key='mecha',
        display_name_cn='霸天机甲',
        display_name_en='Mecha ASOL',
        carry_unit_cost=4,
        filter=(
            Trait('TFT17_Mecha', min_units=4)
            & Unit('TFT17_AurelionSol', item_min=2)
            & Unit('TFT17_Galio', item_min=2)
        ),
    ),
    CompositionDefinition(
        key='vanguard_leblanc',
        display_name_cn='重装妖姬',
        display_name_en='Vanguard LeBlanc',
        carry_unit_id='TFT17_Leblanc',
        carry_unit_cost=4,
        filter=(
            Unit('TFT17_Leblanc', item_min=3, item_max=3)
            & Trait('TFT17_ShieldTank', min_units=2)
            & Trait('TFT17_SummonTrait', min_units=3, max_units=3)
            & ~Unit('TFT17_Diana', item_min=3, item_max=3)
            & ~Unit('TFT17_Nasus', item_min=3, item_max=3)
            & ~Unit('TFT17_Zoe', item_min=3, item_max=3)
            & ~Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Unit('TFT17_Vex', item_min=3, item_max=3)
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Leona')
            & ~Item('TFT_Item_Bloodthirster', carrier_unit_id='TFT17_Leona')
        ),
    ),
    CompositionDefinition(
        key='shepherd',
        display_name_cn='牧羊人',
        display_name_en='Shepherd',
        carry_unit_id='TFT17_Leblanc',
        carry_unit_cost=4,
        filter=(
            Trait('TFT17_SummonTrait', min_units=5)
            & ~Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Unit('TFT17_Lissandra', item_min=3, item_max=3)
        ),
    ),
    CompositionDefinition(
        key='nova_yi',
        display_name_cn='狂战易',
        display_name_en='Marauder Yi',
        carry_unit_id='TFT17_MasterYi',
        carry_unit_cost=4,
        filter=(
            Unit('TFT17_MasterYi', item_min=3, item_max=3)
            & Trait('TFT17_DRX', min_units=2)
            & ~Unit('TFT17_Aatrox', item_min=3, item_max=3, star_min=3, star_max=3)
            & ~Unit('TFT17_Zed')
            & ~Unit('TFT17_Gragas', item_min=3, item_max=3, star_min=3, star_max=3)
        ),
    ),
    CompositionDefinition(
        key='xayah',
        display_name_cn='霞',
        display_name_en='Xayah',
        carry_unit_id='TFT17_Xayah',
        carry_unit_cost=4,
        filter=(
            Unit('TFT17_Xayah', item_min=3, item_max=3)
            & ~Unit('TFT17_Lulu', item_min=3, item_max=3)
            & ~Unit('TFT17_Samira', item_min=3, item_max=3)
            & ~Unit('TFT17_Jax', item_min=3, item_max=3)
            & ~Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Ezreal', item_min=3, item_max=3)
        ),
    ),
    CompositionDefinition(
        key='voyager',
        display_name_cn='旅人娜美',
        display_name_en='Voyager Nami',
        carry_unit_id='TFT17_Nami',
        carry_unit_cost=4,
        filter=(
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
    ),

    # 3 costs
    CompositionDefinition(
        key='conduit_mf',
        display_name_cn='神谕女枪',
        display_name_en='Conduit MF',
        carry_unit_id='TFT17_MissFortune',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_MissFortune', item_min=2)
            & Trait('TFT17_ManaTrait', min_units=2)
        ),
    ),
    CompositionDefinition(
        key='replicator_mf',
        display_name_cn='魔术师女枪',
        display_name_en='Replicator MF',
        carry_unit_id='TFT17_MissFortune',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_MissFortune', item_min=2)
            & Trait('TFT17_APTrait', min_units=2)
        ),
    ),
    CompositionDefinition(
        key='challenger_mf',
        display_name_cn='挑战者女枪',
        display_name_en='Challenger MF',
        carry_unit_id='TFT17_MissFortune',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_MissFortune', item_min=2)
            & Trait('TFT17_ASTrait', min_units=2)
        ),
    ),
    CompositionDefinition(
        key='lulu',
        display_name_cn='璐璐',
        display_name_en='Lulu Reroll',
        carry_unit_id='TFT17_Lulu',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_Lulu', item_min=3, item_max=3)
            & _any_stargazer(3)
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Jax')
            & ~Item('TFT_Item_GuinsoosRageblade', carrier_unit_id='TFT17_Jax')
            & ~Unit('TFT17_MissFortune')
            & ~Unit('TFT17_TwistedFate', item_min=3, item_max=3, star_min=3, star_max=3)
        ),
    ),
    CompositionDefinition(
        key='anima_diana',
        display_name_cn='幻灵皎月',
        display_name_en='Anima Diana',
        carry_unit_id='TFT17_Diana',
        carry_unit_cost=3,
        filter=(
            (Unit('TFT17_Aurora', item_min=3, item_max=3)
             | Unit('TFT17_Diana', item_min=3, item_max=3))
            & Unit('TFT17_Diana')
            & Trait('TFT17_AnimaSquad', min_units=3)
        ),
    ),
    CompositionDefinition(
        key='viktor',
        display_name_cn='维克托',
        display_name_en='Viktor',
        carry_unit_id='TFT17_Viktor',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_Viktor', item_min=3, item_max=3)
            & ~Unit('TFT17_MissFortune')
            & ~Unit('TFT17_Pyke', item_min=3, item_max=3)
            & ~Unit('TFT17_MasterYi', item_min=3, item_max=3)
            & ~Item('TFT_Item_JeweledGauntlet', carrier_unit_id='TFT17_IvernMinion')
            & ~Item('TFT_Item_GuardianAngel', carrier_unit_id='TFT17_IvernMinion')
            & ~Unit('TFT17_AurelionSol', item_min=3, item_max=3)
            & ~Item('TFT_Item_JeweledGauntlet', carrier_unit_id='TFT17_Gragas')
            & ~Unit('TFT17_Vex')
        ),
    ),
    CompositionDefinition(
        key='kaisa',
        display_name_cn='卡莎',
        display_name_en="Kai'Sa",
        carry_unit_id='TFT17_Kaisa',
        carry_unit_cost=3,
        filter=(
            (
                (
                    Unit('TFT17_Kaisa', item_min=2)
                    & Unit('TFT17_Fizz', item_min=2)
                )
                | (
                    Unit('TFT17_Kaisa', item_min=2)
                    & Unit('TFT17_Illaoi', item_min=2)
                    & Trait('TFT17_DarkStar', min_units=4)
                )
            )
            & ~Unit('TFT17_Lissandra', item_min=3, item_max=3)
        ),
    ),
    CompositionDefinition(
        key='two_tanky_samira',
        display_name_cn='莎弥拉',
        display_name_en='Samira',
        carry_unit_id='TFT17_Samira',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_Samira')
            & Unit('TFT17_Ornn', count=2)
        ),
    ),
    CompositionDefinition(
        key='mecha_aurora',
        display_name_cn='机甲阿萝拉',
        display_name_en='Mecha Aurora',
        carry_unit_id='TFT17_Urgot',
        carry_unit_cost=3,
        filter=(
            Unit('TFT17_Urgot', item_min=2)
            & Unit('TFT17_Aurora', item_min=2)
        ),
    ),

    # 2 costs
    CompositionDefinition(
        key='gnar',
        display_name_cn='纳尔',
        display_name_en='Gnar Reroll',
        carry_unit_id='TFT17_Gnar',
        carry_unit_cost=2,
        filter=Unit('TFT17_Gnar', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='pyke',
        display_name_cn='派克',
        display_name_en='Pyke Reroll',
        carry_unit_id='TFT17_Pyke',
        carry_unit_cost=2,
        exclude_dmg_items_for_carriers=['TFT17_IvernMinion', 'TFT17_Gragas'],
        filter=(
            Unit('TFT17_Pyke', item_min=3, item_max=3)
            & ~Unit('TFT17_Viktor', item_min=3, item_max=3)
        ),
    ),
    CompositionDefinition(
        key='reach_for_the_stars',
        display_name_cn='摘星之志',
        display_name_en='Reach for the Stars',
        carry_unit_id='TFT17_Jax',
        carry_unit_cost=2,
        exclude_tank_items_for_carriers=['TFT17_Jax'],
        filter=Unit('TFT17_Jax', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='the_big_bang',
        display_name_cn='宇宙大爆炸',
        display_name_en='The Big Bang',
        carry_unit_id='TFT17_IvernMinion',
        carry_unit_cost=2,
        exclude_tank_items_for_carriers=['TFT17_IvernMinion'],
        filter=Unit('TFT17_IvernMinion', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='zoe',
        display_name_cn='佐伊',
        display_name_en='Zoe Reroll',
        carry_unit_id='TFT17_Zoe',
        carry_unit_cost=2,
        exclude_dmg_items_for_carriers=['TFT17_Mordekaiser'],
        filter=(
            (
                Unit('TFT17_Zoe', star_min=3, star_max=3)
                | (
                    Unit('TFT17_Zoe', star_min=2, star_max=2, item_min=3, item_max=3)
                    & ~Unit('TFT17_Leblanc', item_min=3, item_max=3)
                )
            )
            & ~Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Leona')
            & ~Item('TFT_Item_Bloodthirster', carrier_unit_id='TFT17_Leona')
            & ~Unit('TFT17_AurelionSol', item_min=3, item_max=3)
        ),
    ),

    CompositionDefinition(
        key='heat_death',
        display_name_cn='热寂',
        display_name_en='Heat Death',
        carry_unit_id='TFT17_Mordekaiser',
        carry_unit_cost=2,
        exclude_tank_items_for_carriers=['TFT17_Mordekaiser'],
        filter=Unit('TFT17_Mordekaiser', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='self_destruct',
        display_name_cn='自我毁灭',
        display_name_en='Self Destruct',
        carry_unit_id='TFT17_Gragas',
        carry_unit_cost=2,
        exclude_tank_items_for_carriers=['TFT17_Gragas'],
        filter=Unit('TFT17_Gragas', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='bel_jinx',
        display_name_cn='大卑金克丝',
        display_name_en="Bel'Veth Jinx",
        carry_unit_id='TFT17_Belveth',
        carry_unit_cost=2,
        filter=(
            (Unit('TFT17_Belveth', item_min=3, item_max=3)
             | Unit('TFT17_Jinx', item_min=3, item_max=3))
            & Unit('TFT17_Belveth')
            & Unit('TFT17_Jinx')
            & ~Unit('TFT17_Briar', item_min=3, item_max=3)
            & ~Unit('TFT17_Diana', item_min=3, item_max=3)
            & ~Unit('TFT17_MissFortune', item_min=3, item_max=3)
        ),
    ),

    # 1 costs
    CompositionDefinition(
        key='primordian',
        display_name_cn='贝蕾亚',
        display_name_en='Briar Reroll',
        carry_unit_id='TFT17_Briar',
        carry_unit_cost=1,
        filter=(
            Unit('TFT17_Briar', item_min=3, item_max=3)
            & Trait('TFT17_Primordian', min_units=2)
            & ~Unit('TFT17_Jinx')
        ),
    ),
    CompositionDefinition(
        key='shieldmaiden',
        display_name_cn='盾女',
        display_name_en='Shieldmaiden',
        carry_unit_id='TFT17_Leona',
        carry_unit_cost=1,
        exclude_tank_items_for_carriers=['TFT17_Leona'],
        filter=Unit('TFT17_Leona', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='bonk',
        display_name_cn='邦！',
        display_name_en='Bonk!',
        carry_unit_id='TFT17_Nasus',
        carry_unit_cost=1,
        exclude_tank_items_for_carriers=['TFT17_Nasus'],
        filter=Unit('TFT17_Nasus', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='stellar_combo',
        display_name_cn='星界连招',
        display_name_en='Stellar Combo',
        carry_unit_id='TFT17_Aatrox',
        carry_unit_cost=1,
        exclude_tank_items_for_carriers=['TFT17_Aatrox'],
        filter=Unit('TFT17_Aatrox', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='termeepnal_velocity',
        display_name_cn='飙速木灵',
        display_name_en='Termeepnal Velocity',
        carry_unit_id='TFT17_Poppy',
        carry_unit_cost=1,
        exclude_tank_items_for_carriers=['TFT17_Poppy'],
        filter=Unit('TFT17_Poppy', item_min=3, item_max=3),
    ),
    CompositionDefinition(
        key='ez_chogath',
        display_name_cn='EZ科加斯',
        display_name_en="EZ Cho'Gath Reroll",
        carry_unit_id='TFT17_Chogath',
        carry_unit_cost=1,
        filter=(
            (Unit('TFT17_Chogath', item_min=2)
             | Unit('TFT17_Pantheon', item_min=2))
            & Unit('TFT17_Ezreal', item_min=2)
        ),
    ),
    CompositionDefinition(
        key='tf',
        display_name_cn='崔斯特',
        display_name_en='TF Reroll',
        carry_unit_id='TFT17_TwistedFate',
        carry_unit_cost=1,
        filter=(
            Unit('TFT17_TwistedFate', item_min=2)
            & Unit('TFT17_Jax', item_min=2)
            & ~Item('TFT_Item_Bloodthirster', carrier_unit_id='TFT17_Aatrox')
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Jax')
            & ~Item('TFT_Item_GuinsoosRageblade', carrier_unit_id='TFT17_Jax')
            & ~Unit('TFT17_Lulu')
        ),
    ),
    CompositionDefinition(
        key='veigar',
        display_name_cn='维迦',
        display_name_en='Veigar Printer',
        carry_unit_id='TFT17_Veigar',
        carry_unit_cost=1,
        filter=(
            Unit('TFT17_Veigar', item_min=3, item_max=3)
            & ~Item('TFT_Item_InfinityEdge', carrier_unit_id='TFT17_Poppy')
        ),
    ),
    CompositionDefinition(
        key='teemo',
        display_name_cn='提莫',
        display_name_en='Teemo Reroll',
        carry_unit_id='TFT17_Teemo',
        carry_unit_cost=1,
        filter=(
            Unit('TFT17_Teemo', item_min=3, item_max=3)
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Nasus')
            & ~Item('TFT_Item_GuinsoosRageblade', carrier_unit_id='TFT17_Nasus')
            & ~Item('TFT_Item_TitansResolve', carrier_unit_id='TFT17_Leona')
            & ~Item('TFT_Item_Bloodthirster', carrier_unit_id='TFT17_Leona')
        ),
    ),
    CompositionDefinition(
        key='lisscho',
        display_name_cn='冰女',
        display_name_en='Lissandra Reroll',
        carry_unit_id='TFT17_Lissandra',
        carry_unit_cost=1,
        filter=(
            Unit('TFT17_Lissandra', item_min=3, item_max=3)
            & Trait('TFT17_DarkStar', min_units=4)
            & ~Unit('TFT17_Ezreal', item_min=3, item_max=3)
            & ~Unit('TFT17_Veigar')
            & ~Unit('TFT17_Teemo')
        ),
    ),
)

__all__ = ["COMPOSITIONS"]
