import time
import subprocess

if __name__ == '__main__':
    while True:
        print('Starting retraining process...')
        subprocess.run(['python', '-m', 'src.train'])
        # Sleep for an hour (3600 seconds) before the next training
        time.sleep(3600)
