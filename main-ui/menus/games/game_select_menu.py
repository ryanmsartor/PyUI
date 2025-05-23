
import os
from pathlib import Path
import subprocess
import time
from controller.controller import Controller
from devices.device import Device
from display.display import Display
from games.utils.game_entry import GameEntry
from games.utils.rom_utils import RomUtils
from menus.games.roms_menu_common import RomsMenuCommon
from menus.games.utils.rom_select_options_builder import RomSelectOptionsBuilder
from themes.theme import Theme
from views.grid_or_list_entry import GridOrListEntry
from games.utils.game_system import GameSystem 


class GameSelectMenu(RomsMenuCommon):
    def __init__(self, display: Display, controller: Controller, device: Device, theme: Theme):
        super().__init__(display,controller,device,theme)

    def _is_favorite(self, favorites: list[GameEntry], rom_file_path):
        return any(Path(rom_file_path).resolve() == Path(fav.rom_path).resolve() for fav in favorites)

    def _get_rom_list(self) -> list[GridOrListEntry]:
        return self.rom_select_options_builder.build_rom_list(self.game_system)

    def run_rom_selection(self,game_system : GameSystem) :
        self.game_system = game_system
        self._run_rom_selection(game_system.display_name)