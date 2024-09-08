import os, time

ORANGE_TEXT = '\033[38;5;208m'
BLUE_TEXT = '\033[94m'
RED_TEXT = '\033[91m'
GREEN_TEXT = '\033[92m'
RESET_TEXT = '\033[0m'

print(f"{RED_TEXT}  ,d88b.d88b,{RESET_TEXT}")
time.sleep(0.1)
print(f"{RED_TEXT}  88888888888{RESET_TEXT}")
time.sleep(0.1)
print(f"{RED_TEXT}  `Y8888888Y'{RESET_TEXT}")
time.sleep(0.1)
print(f"{RED_TEXT}    `Y888Y'{RESET_TEXT}")
time.sleep(0.1)
print(f"{RED_TEXT}      `Y'{RESET_TEXT}")
time.sleep(0.1)
print(f"{GREEN_TEXT}CONSOLE{RESET_TEXT} {BLUE_TEXT}FILE MANAGER{RESET_TEXT}")
time.sleep(0.2)

def get_file_action() -> str:
    return input(f'{RED_TEXT}What operation would you like to perform on the file? (read, write, append, delete): {RESET_TEXT}').strip().lower()

def handle_file_operation(filename, operation) -> None:
    try:
        if operation in ['read', 'r']:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\n{RED_TEXT}File content:\n{RESET_TEXT}")
                print(f'{BLUE_TEXT}{content}{RESET_TEXT}\n')

        elif operation in ['write', 'w']:
            content = input(f'{RED_TEXT}What content would you like to write to the file? {RESET_TEXT}')
            with open(filename, 'w') as file:
                file.write(content)
                print(f'{RED_TEXT}Content written to {RESET_TEXT}{BLUE_TEXT}{filename}{RESET_TEXT}{RED_TEXT}.{RESET_TEXT}')

        elif operation in ['append', 'a']:
            content = input(f'{RED_TEXT}What content would you like to append to the file? {RESET_TEXT}')
            with open(filename, 'a') as file:
                file.write(content)
                print(f'{RED_TEXT}Content appended to {RESET_TEXT}{BLUE_TEXT}{filename}{RESET_TEXT}{RED_TEXT}.{RESET_TEXT}')
                
        elif operation in ['delete', 'd']:
            os.remove(filename)
            print(f'{RED_TEXT}File{RESET_TEXT} {BLUE_TEXT}{filename}{RESET_TEXT} {RED_TEXT}has been deleted.{RESET_TEXT}')

    except Exception as e:
        print(f'{RED_TEXT}An error occurred: {RESET_TEXT}{GREEN_TEXT}{e}{RESET_TEXT}')

def create_new_file(filename) -> None:
    content = input(f'{RED_TEXT}Would you like to write content to the file?{RESET_TEXT} ({GREEN_TEXT}Y{RESET_TEXT}/{RED_TEXT}n{RESET_TEXT}): ').strip().lower()
    if content == 'y':
        content_to_write = input(f'{RED_TEXT}What content would you like to write to the file?{RESET_TEXT} ')
        with open(filename, 'w') as file:
            file.write(content_to_write)
            print(f'{RED_TEXT}File{RESET_TEXT} {BLUE_TEXT}{filename}{RESET_TEXT} {RED_TEXT}has been created and content written.{RESET_TEXT}')
    else:
        print(f'{RED_TEXT}File {filename} has been created without content.{RESET_TEXT}')

def main() -> None:
    while True:
        fInput = input(f'{RED_TEXT}Would you like to perform an operation on a file or a folder? {RESET_TEXT}').strip()

        if fInput.lower() in ['folder', 'dir', 'directory']:
            import subprocess
            executable_path = './dir'  # Ensure that this is the correct executable path!!
            subprocess.run(executable_path)

        else:
            filename = input(f'{RED_TEXT}What file would you like to perform operations on? {RESET_TEXT}').strip()

            if os.path.exists(filename):
                operation = get_file_action()
                if operation in ['read', 'r', 'write', 'w', 'append', 'a', 'delete', 'd']:
                    handle_file_operation(filename, operation)
                else:
                    print(f'{RED_TEXT}Invalid operation. Please choose read, write, append, or delete.{RESET_TEXT}')   
            else:
                yn = input(f'{RED_TEXT}The file does not exist. Would you like to create it?{RESET_TEXT} ({GREEN_TEXT}Y{RESET_TEXT}/{RED_TEXT}n{RESET_TEXT}): ').strip().lower()
                if yn in 'y':
                    create_new_file(filename)
                else:
                    print(f'{RED_TEXT}No file created.{RESET_TEXT}')

            another_operation = input(f'{RED_TEXT}Would you like to perform another operation?{RESET_TEXT} ({GREEN_TEXT}Y{RESET_TEXT}/{RED_TEXT}n{RESET_TEXT}): ').strip().lower()
            if another_operation != 'y':
                print(f'{RED_TEXT}Exiting...{RESET_TEXT}')
                break

if __name__ == '__main__':
    main()
