import rarfile
import time
import os

RED = "\033[91m"
ORANGE = "\033[33m"
RESET = "\033[0m"

def print_custom_banner(main_text_ascii, author_name="Your Name"):

    print(f"{RED}{main_text_ascii}{RESET}")
    print("\n")

    author_line = f"{ORANGE}<------ Written By {author_name} ------>{RESET}"

    print(author_line.center(80))

    print("\n" * 2) 


rarfile.tool = r"C:\Unrar\UnRAR.exe" #Jangan lupa ganti dengan path UnRAR.exe kamu


def crack_rar(rar_path, wordlist_path):
    found = False
    try:
        try:
            rar_archive = rarfile.RarFile(rar_path)
        except rarfile.BadRarFile:
            print("[!] File RAR rusak atau tidak bisa dibuka.")
            return

        with open(wordlist_path, 'r', encoding='utf-8') as wordlist:
            for line_num, line in enumerate(wordlist, 1):
                password = line.strip()
                print(f"[{line_num}] Mencoba: {password}")

                try:
                    rar_archive.setpassword(password)
                    rar_archive.testrar()
                    print(f"[+] Password ditemukan: {password}")
                    print(f"[+] Daftar file di dalam RAR: {rar_archive.namelist()}")
                    found = True
                    break
                except rarfile.RarWrongPassword:
                    pass
                except rarfile.NoRarEntry:
                    print(f"[!] Warning: No RAR entry found with password {password}. Could be an unusual archive.")
                    pass
                except Exception as e:
                    print(f"[!] Error saat mencoba password {password}: {e}")
                    pass

    except FileNotFoundError:
        print(f"[!] File wordlist tidak ditemukan: {wordlist_path}")
    except Exception as e:
        print(f"[!] Error umum: {e}")

    finally:
        if not found:
            print("[-] Password tidak ditemukan di wordlist.")

if __name__ == "__main__":
    daniel_martin_ascii = r"""
______  ___  ____________            _   ___________ _____            _____ _____  _____ _      _____ 
| ___ \/ _ \ | ___ \ ___ \          | | |____ |  ___|  _  |          |_   _|  _  ||  _  | |    /  ___|
| |_/ / /_\ \| |_/ / |_/ /_ __ _   _| |_    / / |_  | |/' |_ __ ___ ___| | | | | || | | | |    \ `--. 
|    /|  _  ||    /| ___ \ '__| | | | __|   \ \  _| |  /| | '__/ __/ _ \ | | | | || | | | |     `--. \
| |\ \| | | || |\ \| |_/ / |  | |_| | |_.___/ / |   \ |_/ / | | (_|  __/ | \ \_/ /\ \_/ / |____/\__/ /
\_| \_\_| |_/\_| \_\____/|_|   \__,_|\__\____/\_|    \___/|_|  \___\___\_/  \___/  \___/\_____/\____/ 
                                                                                                      
    """
    print_custom_banner(main_text_ascii=daniel_martin_ascii, author_name="Daniel Martin")
    time.sleep(2) # Jeda 2 detik
rar_file = "test.rar" #Jangan lupa ganti dengan nama file rar kamu
wordlist_file = "wordlist.txt" #Jangan lupa ganti dengan nama file txt kamu
start = time.time()
crack_rar(rar_file, wordlist_file)
print(f"\nWaktu eksekusi: {time.time() - start:.2f} detik")
