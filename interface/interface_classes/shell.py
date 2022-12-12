import os


class LoxSh:

    prompt_in = '=<< '
    prompt_out_0 = '=-> '
    prompt_out_1 = '=~> '
    prompt_out_2= '=*> '
    intro = 'Welcome to the shell Lox.'
    cmd_list = os.listdir('commands')

    def cmd_loop(self, if_intro = 0):
        if if_intro:
            self.out_put(self.intro)

        self.pre_loop()
        line = ''
        cmd_seq = []
        verb = ''
        adverbs = []
        objects = []
        
        while 1:
            line = self.in_put()
            cmd_seq = self.cmd_parse(line)
            verb, adverbs, objects = self.cmd_analysis(cmd_seq)
            if verb in self.cmd_list:
                pass    # need modified
            elif verb == 'Q':
                break
            else:
                self.out_put(f"LoxSh: Unregistered command: {verb}", 2)
        self.post_loop()

    def pre_loop(self):
        pass
    
    def post_loop(self):
        pass

    def cmd_parse(self, a_line):
        return a_line.split()
    
    def cmd_analysis(self, a_cmd_seq):
        v, adv, obj = '', [], []
        v = a_cmd_seq[0]
        a_cmd_seq.pop(0)
        for entry in a_cmd_seq:
            if entry[0] == '-' and entry.strip('-'):
                adv.append(entry)
                a_cmd_seq.remove(entry)
        obj = a_cmd_seq

        return v, adv, obj

    def out_put(self, a_line, info_type = 0):
        if isinstance(a_line, str):
            if info_type == 0:
                print(self.prompt_out_0 + a_line)
            elif info_type == 1:
                print(self.prompt_out_1 + a_line)
            else:
                print(self.prompt_out_2 + a_line)
        else:
            print('>*> LoxSh.out_put: ERROR! Output type should be str!')

    def in_put(self):
        return input(self.prompt_in)
        
