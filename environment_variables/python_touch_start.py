import os

toe_file = 'E:\\github\\ragan-git\\touchdesigner\\_workshops\\_summit-2019\\touchdesigner-summit-2019-large-systems\\environment_variables\\env-vars.toe'

# set environment variable
toe_env_var             = 'controller'
os.environ['STARTUP']   = toe_env_var
os.startfile(toe_file)
print("startting file with {}".format(toe_env_var))

# set environment variable
toe_env_var             = 'node'
os.environ['STARTUP']   = toe_env_var
os.startfile(toe_file)
print("startting file with {}".format(toe_env_var))