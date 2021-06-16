from file_client_cli import send_command
import datetime
import threading


def get100kali(j):
    texec = dict()
    init = datetime.datetime.now()
    for i in range(0, j):
        print(f"GET pokijan.jpg ke {i}")
        # Threading dengan fungsi send_command
        texec[f"{i}"] = threading.Thread(target=send_command, args=("GET pokijan.jpg",))
        texec[f"{i}"].start()
    # join setelah thread selesai
    for i in range(0, j):
        texec[f"{i}"].join()

    end = datetime.datetime.now()
    total = end - init
    print(f"Waktu TOTAL yang dibutuhkan {total} detik {init} s/d {end}")


if __name__ == '__main__':
    get100kali(100)
