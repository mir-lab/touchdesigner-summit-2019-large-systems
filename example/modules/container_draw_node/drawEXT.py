class Draw:
    '''
        The Draw class is specifically focused on the needs of setting up
        our windows that draw some kind of graphics. This is a little different
        from our control class, as the controller typically is focused on UI pieces
        and the actions that it drives. This class is focused entirely on the
        creation and arrangement of individual outputs.
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
        self.Dimensions_table   = op('table_dimensions')
        self.Export_header      = ['path', 'parameter', 'value', 'enable']

        init_msg = 'Draw Class Init from {}'.format(myOp)
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
        self.Create_nodes()

        print("Startup process from Draw Node | {}".format(self.MyOp))
        pass
    
    def Create_nodes(self):
        '''
            Here we create all nodes in our output list.

            This is the key element of the configuration process. This allows you the
            flexibility to configure any number of ways as you see appropriate for a
            given project. 
            
            Notes
            ---------
            
            Args
            ---------
            none

            Returns
            ---------
            none		
        ''' 
        # set up all the variables for this process
        node            = op.Project.fetch('role')
        config          = op.Project.fetch('nodes')[node]
        node_channels   = op.Project.fetch('nodes')[node]['channels']
        channels        = op.Project.fetch('channels')
        channel_types   = op.Project.fetch('channel_type')

        # prep table for exporting sizes
        self.Dimensions_table.clear()
        export_list = []
        export_list.append(self.Export_header)

        # cleanup
        parent(2).Delete_old_ops(self.MyOp, self.MyOp)

        # loop through and create new channels
        new_node_x_pos = 0

        for each in enumerate(node_channels):
            channel_order   = each[0]
            each_channel    = each[1]
            
            # create new comp
            new_node        = parent().create(containerCOMP, 'container_{}'.format(each_channel))
            
            chan_type       = channels[each_channel]['type']
            module_loc      = channel_types[chan_type]['tox']

            # add width and height to export list
            export_list.append( [ new_node.path, 'w',channels[each_channel]['width'], 1] )
            export_list.append( [ new_node.path, 'h',channels[each_channel]['height'], 1] )

            # set-external tox and reload
            new_node.par.externaltox    = module_loc
            new_node.par.reinitnet.pulse()
            new_node.par.savebackup     = False
            new_node.par.alignorder     = channel_order
            new_node.nodeX              = new_node_x_pos
            new_node_x_pos              += 200

        # fill in the export table with resolutions
        for each_item in export_list:
            self.Dimensions_table.appendRow(each_item)

        # completed startup from output
        print("Startup process from Output | {}".format(self.MyOp))

        # kickoff initialization on new object
        #new_node.Touch_start()
