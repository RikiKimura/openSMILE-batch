import subprocess
import glob
from tqdm import tqdm


list = glob.glob('./data/*.wav') # wavファイルの置き場


for pathname in tqdm(list):
    pathname = pathname.strip("./opensmile-2.3.0/bin/Win32/")
    command = "./SMILExtract_Release.exe -C config/IS09_emotion.conf -I "+pathname+" -O ./output/output.arff -instname "+pathname+" -class NEU"
    print("\n"+command)
    subprocess.call(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
