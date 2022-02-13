import interface
import research
import data_organizer

interface.startGUI()
print(interface.word)
research.extract(interface.word)
print(research.data)
data_organizer.list_to_series(research.data)