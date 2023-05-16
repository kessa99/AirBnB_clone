#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    intro = '\nWelcome to the airbnb comsole.'
    intro += ' Type help or ? to list commands.\n'
    prompt = '(hbtn) '
    file = None


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
