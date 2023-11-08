from typing import Optional

from renpy.ast import PyExpr
from renpy.lexer import Lexer
import renpy.exports as renpy

from game.achievements.Achievements_ren import Achievement

path_builder: bool
_in_replay: bool

"""renpy
python early:
"""


def parse_grant(lexer: Lexer) -> PyExpr:
    achievement: Optional[PyExpr] = lexer.simple_expression()
    if not achievement:
        renpy.error("Expected achievement")  # type: ignore

    return achievement  # type: ignore


def lint_grant(achievement_expr: PyExpr) -> None:
    try:
        achievement_: Achievement = eval(achievement_expr)
    except Exception:
        renpy.error(f"Invalid achievement: {achievement_expr}")  # type: ignore
        return

    if not renpy.has_image(achievement_.id):  # type: ignore
        renpy.error(f"Missing achievement image: {achievement_.id}")  # type: ignore


def execute_grant(achievement_expr: PyExpr) -> None:
    if path_builder or _in_replay:
        return

    achievement_: Achievement = eval(achievement_expr)

    renpy.show(achievement_.id, [show_achievement], "foreground")  # type: ignore
    achievement.grant(achievement_.id)  # type: ignore
    achievement.sync()  # type: ignore


def execute_init_grant(achievement_expr: PyExpr) -> None:
    achievement_: Achievement = eval(achievement_expr)

    Achievement.all_achievements[achievement_.id] = achievement_

    # Add achievements to renpy/steam
    achievement.register(achievement_.id)  # type: ignore
    achievement.sync()  # type: ignore


def translation_strings(achievement_expr: PyExpr) -> list[str]:
    _achievement: Achievement = eval(achievement_expr)
    return [_achievement.id, _achievement.description]


renpy.register_statement(  # type: ignore
    name="grant",
    parse=parse_grant,
    lint=lint_grant,
    execute=execute_grant,
    execute_init=execute_init_grant,
    # translation_strings=translation_strings,
)
