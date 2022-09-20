
class AFD():
    def __init__(self, regex):

        self.count = 0
        self.rounds = 1
        self.states = []
        self.symbols = []
        self.transitions = []
        self.acc_states = []
        self.init_state = None
        self.leaf = [] 
        self.root = None
        self.id = 0
        self.final_state = None
        self.follow_pos = {}