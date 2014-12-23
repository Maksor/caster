import sys

BASE_PATH = r"C:\NatLink\NatLink\MacroSystem"
if BASE_PATH not in sys.path:
    sys.path.append(BASE_PATH)
from asynch.hmc.hmc_vocabulary import Homunculus_Vocabulary
from asynch.hmc.homunculus import Homunculus
from lib import paths, settings, utilities
from lib import runner
from asynch.hmc import hmc_vocabulary, homunculus


def launch(htype=None, info=None):
    instructions=["pythonw", paths.HOMUNCULUS_PATH]
    if htype!=None:
        instructions.append(htype)
        if info!=None:
            instructions.append(info)
    else:
        instructions.append(homunculus.QTYPE_DEFAULT)
    runner.run(instructions)

def clean_homunculi():
    while utilities.window_exists(None, settings.HOMUNCULUS_VERSION):
        utilities.kill_process("pythonw.exe")
    while utilities.window_exists(None, settings.HOMUNCULUS_VERSION+" :: Vocabulary Manager"):
        utilities.kill_process("pythonw.exe")

if __name__ == '__main__':
    if sys.argv[1]==homunculus.QTYPE_DEFAULT:
        app = Homunculus(sys.argv[1])
    elif sys.argv[1] in [hmc_vocabulary.QTYPE_SET, hmc_vocabulary.QTYPE_REM]:
        found_word=None
        if len(sys.argv)>2:
            found_word=sys.argv[2]
        if sys.argv[1]==hmc_vocabulary.QTYPE_SET:
            app = Homunculus_Vocabulary([hmc_vocabulary.QTYPE_SET, found_word])
        elif sys.argv[1]==hmc_vocabulary.QTYPE_REM:
            app = Homunculus_Vocabulary([hmc_vocabulary.QTYPE_REM, found_word])
            