__ALL__ = ['LoxShell']
class LoxShell:

    prompt = '>-->'
    intro = '> Welcome to the shell Lox <'

    def cmd_loop(self):

        print(self.intro)

        self.pre_loop()
        line = ''
        cmd_seq = []
        verb = ''
        adverbs = []
        objects = []
        
        while 1:
            line = input(self.prompt)
            cmd_seq = self.cmd_parse(line)
            verb, adverbs, objects = self.cmd_analysis(cmd_seq)
            if verb in cmd_rgt:
                pass
            if verb == 'quit':
                break
            else:
                print(f"! Unregistered command: {line}")
        self.post_loop()

    def pre_loop(self):
        pass
    
    def post_loop(self):
        pass

    def cmd_parse(self, a_line):
        return a_line.split(' ')
    
    def cmd_analysis(self, a_cmd_seq):
        v, adv, obj = '', [], []
        
        v = a_cmd_seq[0]
        a_cmd_seq.pop(0)
        for entry in a_cmd_seq:
            if entry[0] == '-':
                adv.append(entry)
                a_cmd_seq.remove(entry)
        obj = a_cmd_seq

        return v, adv, obj
