from .divines import (
  scratch_divine,
  boutonMash,
  boutonCarotte,
  boutonFairyTalesRead,
  boutonMusketeerAsk,
  boutonDivination,
  boutonBoire,
  take_japanese_ufo,
  spice_horse
)


DIVINE_ACTIONS = {
  "Egyptian": scratch_divine,
  "Shark": scratch_divine,
  "UltraPowerForce": boutonMash,
  "Fire": boutonCarotte,
  "Fairy Tales": boutonFairyTalesRead,
  "Musketeers": boutonMusketeerAsk,
  "Celtic": boutonDivination,
  "Japanese": take_japanese_ufo,
  "Spice": spice_horse,
  "Tea": boutonBoire
}