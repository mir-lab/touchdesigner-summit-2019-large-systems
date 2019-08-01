'''
TouchDesigner Summit 2019
Workshop | Large Systems

Instructors 
    Matthew Ragan https://matthewragan.com
    Zoe Sandoval https://zoesandoval.com
'''

import json
import socket

class Project:
    '''
        The project class is at the root of our project and holds many of the essential
        pieces for starting and configuring our project.
    '''

    def __init__(self, myOp):
        '''
            Our class initialization
            
            Notes
            ---------
            
            Args
            ---------
            myOp (touchDesignerOperator):
            > the operator that is loading the current extension

            Returns
            ---------
            none		
        '''
        self.MyOp               = myOp
        self.Config_file        = parent().par.Configfile 
        self.Outputlist_file    = parent().par.Outputlistfile

        init_msg = 'Project Class Init from {}'.format(myOp)
        print(init_msg)
        pass

    def Touch_start(self):
        '''
            This is our start-up procedure for this component, this allows us to specify
            start-up execution order with precision
            
            Notes
            ---------
            
            Args
            ---------
            none

            Returns
            ---------
            none		
        '''
        # load our settings
        self.Load_config()
        self.Load_outputlist()

        # store our ip info
        self.Store_ip_info()

        # init modules by calling Touch_start()
        op('container_output').Touch_start()
        pass

    def Store_ip_info(self, host=socket.gethostname(), ip=socket.gethostbyname(socket.gethostname())):
        '''
            Helper function stores ip info about our computer
            
            Notes
            ---------
            
            Args
            ---------
            host (str):
            > the string host name for the computer.
            > Default value is from socket.gethostname()
            
            ip (str):
            > the string ip address for the computer.
            > Default value is from socket.gethostbyname(socket.gethostname())

            Returns
            ---------
            none		
        '''
        self.MyOp.store('host_name', host)
        self.MyOp.store('ip_address', ip)
        pass

    def Load_store_json(self, targetOp, file):
        '''
            Helper function moves json files to storage
            
            This helper function is intended to help move elements from a file
            into storage. This generalized function stands alone so it can be
            used with a variety of json files.

            Notes
            ---------
            
            Args
            ---------
            targetOp (touchDesignerOperator):
            > the operator where the opened dictionaries will be stored
            
            file (touchDesignerOperator):
            > the json file that will be converted to python dictionaries 

            Returns
            ---------
            none		
        '''
        with open(file) as file_contents:
        
            json_data = json.loads( file_contents.read() )
            
            for each_key, each_value in json_data.items():
                targetOp.store(each_key, each_value)

        pass
    
    def Load_config(self):
        '''
            Helper function to load the config file
            
            Notes
            ---------
            
            Args
            ---------
            none

            Returns
            ---------
            none		
        '''
        # location for config file
        config_loc = '{}/{}'.format(project.folder, self.Config_file.eval())

        # load store json call
        self.Load_store_json(self.MyOp, config_loc)

        # print confirmation message
        print("Config Loaded from {}".format( config_loc ) )
        pass
    
    def Load_outputlist(self):
        '''
            Helper function to load the outputlist file
            
            Notes
            ---------
            
            Args
            ---------
            none

            Returns
            ---------
            none		
        '''
        # location for role file
        outputlist_loc = '{}/{}'.format(project.folder, self.Outputlist_file.eval())

        # load store json call
        self.Load_store_json(self.MyOp, outputlist_loc)

        # print confirmation message
        print("Outputlist Loaded from {}".format( outputlist_loc ) )
        pass