class Controller:
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
        self.MyOp           = myOp

        init_msg = 'Controller Class Init from {}'.format(myOp)
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
        print("Startup process from Controller | {}".format(self.MyOp))

        parent(2).Delete_old_ops(self.MyOp, self.MyOp)
        pass
