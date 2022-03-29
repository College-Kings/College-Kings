init python:
    # Helper functions
    
    def get_file_contents(file_path):
        with open(file_path, "r") as f:
            return f.read()

    def write_console(data):
        with open("console.txt", "w") as f:
            f.write(str(data))