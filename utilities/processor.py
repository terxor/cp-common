import sys, subprocess, os, json

# Use config.json from same directory as script
configDir = os.path.dirname(os.path.realpath(__file__))
configFile = "config.json"
config = None

bcolors = {
  "OKGREEN" : "\033[92m",
  "WARNING" : "\033[93m",
  "FAIL" : "\033[91m",
  "ENDC" : "\033[0m",
  "BOLD" : "\033[1m",
  "UNDERLINE" : "\033[4m",
  "NONE" : ""
}

def loadConfig():
  try:
    with open(configDir + "/" + configFile, "r") as read_file:
      global config
      config = json.load(read_file)
  except:
    err("Invalid JSON")

# Print colored string
def pf(string, color):
  if config["useColors"]:
    print(bcolors[color] + string + bcolors["ENDC"])
  else:
    print(string)

def compile(srcName, lang):
  commands = lang["commands"]
  if not "compile" in commands.keys():
    pf("Compile command not defined", "WARNING")
    return
  pf("Compile (lang = " + lang["name"] + ")", "NONE")
  cc = commands["compile"].replace("%", srcName)
  result = subprocess.run(cc, cwd = os.getcwd(), shell=True)
  if result.returncode == 0:
    pf("DONE", "OKGREEN")
  else:
    pf("FAILED", "FAIL")

def run(srcName, lang):
  # pf("Running...", "BOLD")
  runCommand = lang["commands"]["run"].replace("%", srcName)
  rc = config["runConfig"]
  inFile = None
  outFile = None
  if not rc["terminalIO"]:
    fd = "" if rc["useSameDir"] else (configDir + "/")
    inFile = open(fd + rc["inputFile"], "r");
    outFile = open(fd + rc["outputFile"], "w");
  try:
    pf("---- STDIN -----", "UNDERLINE")
    result = subprocess.run(
      runCommand,
      cwd = os.getcwd(), 
      timeout=(None if rc["terminalIO"] else rc["timeLimit"]),
      stdin=sys.stdin,
      capture_output=True
    )
    pf("---- STDOUT ----", "UNDERLINE")
    pf(result.stdout.decode("utf-8"), "BOLD")
    pf("---- STDERR ----", "UNDERLINE")
    pf(result.stderr.decode("utf-8"), "WARNING")
    pf("----------------", "NONE")
  except Exception as e:
    print(e)
    pf("Time Limit Exceeded (" + str(rc["timeLimit"]) + " seconds)", "FAIL")

def err(s):
  pf("ERROR: " + s, "WARNING")
  sys.exit(1)

def processFileName(f):
  i = f.rindex(".")
  return [f[:i], f[i+1:]]

def main():
  if (len(sys.argv) < 3 or (sys.argv[1] not in ["-compile", "-run"])):
    err("Usage processor.py [-compile/-run] [source-file]")

  loadConfig()

  # Split name and extension
  try:
    srcName, srcExt = processFileName(sys.argv[2])
  except:
    err("Unknown file extension")
  
  # Process
  try:
    lang = None
    for l in config["langs"]:
      if l["ext"] == srcExt: lang = l
    if lang == None: raise Exception("Unsupported extension")
    if (sys.argv[1] == "-compile"): compile(srcName, lang)
    else: run(srcName, lang)
  except Exception as e:
    err(str(e))

if __name__ == "__main__":
  main()
