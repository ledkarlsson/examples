"""

Author: Hossin azmoud (Moody0101)
Date: 10/18/2022
LICENCE: MIT
Language: Python3.10

"""


from time import sleep

from colorama import Fore as f
from UtilPackage import (
    DECODE,
    ENCODE,
    ENCODING,
    HASHING,
    Command,
    EncodingManager,
    Hasher,
    Shell,
)

DOC = f"""{f.YELLOW}

	Author: Hossin azmoud (Moody0101)
	Date: 10/18/2022
	LICENCE: MIT
	Language: {f.CYAN}Python3.10 {f.YELLOW}
	Descripion: A tool to hash, encode, decode text.
	command: hash, encode, decode, help, exit
	Usage:
		To encode/Decode:
			Encode/Decode <Text> <Algorithm>
			Encode/Decode only for help.
		To hash:
			Hash <Text> <Algorithm>
			Hash only for help.
"""


class Interface:
    """An interface that handles user interactions with the shell program"""

    def __init__(self) -> None:
        # Shell initializer
        self.shell = Shell()

        self.DefaultCommands = {
            "EXIT": self.Exit,
            "HELP": self.Help,
            "HASH": self.hashDoc,
            "DECODE": self.DeDoc,
            "ENCODE": self.EnDoc,
        }

        self.Commands = {
            "HASH": self.hashVal,
            "DECODE": self.Decode,
            "ENCODE": self.Encode,
        }

    def hashDoc(self):
        """Displays doc for hashing"""
        return HASHING["Doc"]

    def DeDoc(self):
        """Displays doc for decoding"""
        return ENCODING["Doc"][DECODE]

    def EnDoc(self):
        """Displays doc for encoding"""
        return ENCODING["Doc"][ENCODE]

    def Encode(self, Text, EncoderName):
        if EncoderName.upper().strip() not in ENCODING.keys():
            print()
            print(f"  False algorithm name, {EncoderName}")
            print("  you can only use from this list:")
            for i in ENCODING.keys():
                print("    %s", i)
            return

        # Get Encoder function
        func_ = ENCODING[EncoderName.upper().strip()][ENCODE]
        # Map the value
        encode = EncodingManager(func_, ENCODE)
        # return the value
        return encode(Text)

    def Decode(self, Text, DecoderName):
        if DecoderName.upper().strip() not in ENCODING.keys():
            print()
            print(f"  False algorithm name, {DecoderName}")
            print("  you can only use from this list:")
            for i in ENCODING.keys():
                print("    %s", i)
            return

        # Get Encoder function
        func_ = ENCODING[DecoderName.upper().strip()][DECODE]
        # Map the value
        decode = EncodingManager(func_, DECODE)
        # return the value
        return decode(Text)

    def hashVal(self, Text, HasherName):
        if HasherName.upper().strip() not in HASHING.keys():
            print()
            print(f"  False algorithm name, {DecoderName}")
            print("  you can only use from this list:")
            for i in HASHING.keys():
                print("    %s", i)
            return

        return Hasher(HASHING[HasherName.upper().strip()], Text)

    def showFuncs(self):
        if self.Tool:
            for i in CONFIG[self.Tool].keys():
                print("  ", i)

    def SetText(self, Text=None):
        self.text = Text

    def Exit(self) -> None:
        for i in [".", "..", "..."]:
            print(f"  Exiting{i}", end="\r")
            sleep(1)
        exit(0)

    def Help(self):
        return """

	To encode/Decode:
		Encode/Decode <Text> <Algorithm>
		Encode/Decode only for help.
	To hash:
		Hash <Text> <Algorithm>
		Hash only for help.

		"""

    def execute(self, command: Command) -> None:
        if command.CMD in self.DefaultCommands.keys():
            if len(command.argv) > 0:
                print(self.Commands[command.CMD](*command.argv))
            else:
                print(self.DefaultCommands[command.CMD]())
        elif command.CMD in self.Commands.keys():
            if len(command.argv) > 0:
                print(self.Commands[command.CMD](*command.argv))
            else:
                print(self.Commands[command.CMD]())

    def execute_return(self, command: Command) -> str:
        if command.CMD in self.DefaultCommands.keys():
            if len(command.argv) > 0:
                return self.Commands[command.CMD](*command.argv)
            else:
                print(self.DefaultCommands[command.CMD]())
        elif command.CMD in self.Commands.keys():
            if len(command.argv) > 0:
                return self.Commands[command.CMD](*command.argv)
            else:
                return self.Commands[command.CMD]()

    def run(self) -> None:
        print()
        print(DOC)
        Interact = True
        while Interact:
            self.command = self.shell.shellInput()
            if self.command:
                self.execute(self.command)
            else:
                pass

    def test_run(self) -> None:
        command = Command("HASH", ["Hello", "MD5"])
        assert "8b1a9953c4611296a827abf8c47804d7" == self.execute_return(command)
        command = Command("ENCODE", ["Hello", "base64"])
        assert "SGVsbG8=" == self.execute_return(command)
        command = Command("DECODE", ["SGVsbG8=", "base64"])
        assert "Hello" == self.execute_return(command)


def main():
    Interface_ = Interface()
    # Interface_.run()
    Interface_.test_run()


if __name__ == "__main__":
    main()
