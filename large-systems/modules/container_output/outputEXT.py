'''
TouchDesigner Summit 2019
Workshop | Large Systems

Instructors 
    Matthew Ragan https://matthewragan.com
    Zoe Sandoval https://zoesandoval.com
'''

class Output:
    '''
        The output class handles the general arrangement of outputs. This can look like
        a single node, e.g. a controller or a single node; this might also be a mixed 
        set of outputs, e.g. a controller and node. This provides the flexibility to work
        with configurations for single machine use, or distributed / multi-machine use
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
        self.Do_not_delete_tag  = 'keep'

        init_msg = 'Output Class Init from {}'.format(myOp)
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
        # self.Create_nodes()

        # completed startup from output
        print("Touch_start complete from Output | {}".format(self.MyOp))
        pass

    def Reset_network(self):
        # prep table for exporting sizes
        self.Dimensions_table.clear()
        self.Dimensions_table.appendRow(self.Export_header)

        # cleanup
        parent().Delete_old_ops(self.MyOp, self.MyOp)
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
        config_outputlist   = op.Project.fetch('configOutputlist')
        outputlists         = op.Project.fetch('outputlists')
        comp_width_list     = []
        comp_height_list    = []
        new_node_x_pos      = 0
        export_list         = []

        # prep network
        self.Reset_network()

        # loop through config_outputlist
        for each in enumerate( outputlists[config_outputlist] ):
            node_order          = each[0]
            each_node           = each[1]
            config              = op.Project.fetch('nodes')[each_node]
            role                = op.Project.fetch('nodes')[each_node]['role']
            module_loc          = op.Project.fetch('nodes')[each_node]['tox']
            channel_list        = op.Project.fetch('nodes')[each_node]['channels']

            # create new comp
            new_node    = parent().create(containerCOMP, 'container_{}'.format(role))
            
            # set-external tox and reload
            new_node.par.externaltox    = module_loc
            new_node.par.reinitnet.pulse()
            new_node.par.savebackup     = False
            new_node.par.alignorder     = node_order
            new_node.nodeX              = new_node_x_pos
            new_node_x_pos              += 200

            # calculate the size of this node
            new_node_width, new_node_height = self.Calculate_size(channel_list)
            
            # add size of this node to the comp list for parent's size
            comp_width_list.append(new_node_width)
            comp_height_list.append(new_node_height)

            # add new_node_size to the export list
            export_list.append([new_node.path, 'w', new_node_width, 1])
            export_list.append([new_node.path, 'h', new_node_height, 1])

            # add parent comp size to export list
            export_list.append(['..', 'w', sum(comp_width_list), 1])
            export_list.append(['..', 'h', max(comp_height_list), 1])

            # store node role for new node
            new_node.store('node', each_node)

            # kickoff initialization on new object
            new_node.Touch_start()

        # fill in the export table with resolutions
        for each_item in export_list:
            self.Dimensions_table.appendRow(each_item)
        pass
    
    def Delete_old_ops(self, targetOp, calledFrom):
        '''
            Helper function cleans up old components.

            A core element of good house keeping is to make sure that you've taken
            care of any possible pieces that may have accidentally gotten left committed
            in haste. This method loops through, and deletes any old components that are
            not marked as safe.

            Notes
            ---------
            
            Args
            ---------
            targetOp (touchDesignerOperator):
            > the operator whose children we want to find for deletion
            
            calledFrom (touchDesignerOperator):
            > the operator who requested / called the method, helpful for debugging 

            Returns
            ---------
            none		
        '''
        old_comps   = targetOp.findChildren(type=containerCOMP, depth=1)
        
        # loop through and destory old comps, passing over those with the tag "keep"
        for each_old_comp in old_comps:
            if self.Do_not_delete_tag in each_old_comp.tags:
                pass
            else:
                each_old_comp.destroy()
        print("Cleanup in {}".format(calledFrom))
        pass

    def Calculate_size(self, channel_list):
        '''
            Helper function calculates the total size of a list of channels.

            Correct display arrangement and size often depends on correctly setting up
            the display sizes. This helper function calculates the total width, and max height
            of an array of displays.

            Notes
            ---------
            
            Args
            ---------
            channel_list (list):
            > a list of keys that can be fetch from the loaded config file
            
            Returns
            ---------
            max_width (int):
            > the sum of all the widths of the channels added together 

            max_height (int):
            > the max value from a list of heights
        '''
        # fetch our channels from storage
        channels = op.Project.fetch('channels')

        # list comprehension to calculate the max width and max height 
        max_width = sum( [channels[each_chan]['width'] for each_chan in channel_list] )
        max_height = max( [channels[each_chan]['height'] for each_chan in channel_list] )

        return max_width, max_height