
def beat():
    pass

def rest():
    # The character is doing nothing
    #rest can restore some physical strength,add some enregy
    #the effect of recovery is related to time and environment

#The character will perform a withdraw/dodge.
def dofge():
    pass

class Attack():
"""Instances of this class wanna repr
the attack action for every character."""
    def __init__():
        # attack range
        # attack effect
        '''stun after the blow(stunned for a while,,,)
            the blow move away the character,
            
        '''
        # the effect is determined by the size of the force
    
    def beforeAttack():
        pass

    def ingAttack():
    '''The character is performing an attack towards an enemy'''
        pass
    
    def afterAttack():
        pass

    
    def passiveAttack():
    '''This state is the base state for a character hit by a blow.
    Commonly only external action can move a character in this state.'''
        pass
    def attack():
        
        pass

def eat():
    pass

class move():
    #E,S,W,N,UP,DOWN,LEFT,RIGHT,FRON,BACK

    #move in defferent ways,get different speed,the
    #energy consumption is also different

    def fly():
        if 0<SPEED<1:
            pass
    #leave the ground,the surface
    def walk():
    #in a certain speed range of movement
    def run():
    #in a certain speed range of movement
    pass
