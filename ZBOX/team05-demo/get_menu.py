import sys
import csv
import numpy as np
#import tensorflow as tf

def csv_to_list(filename):
    print("reading",filename)
    f = open(filename,"r")
    csv_file=csv.reader(f)

    # last column is dummy, then it is deleted
    try:
        row = next(csv_file)[:-1]
    except:
        return np.array([])
    row = np.array([s for s in row])
    #print(row.shape)
    pose_list = row.reshape((int(row.shape[0]/3),3))
    print(pose_list)
    return pose_list


def get_menu(pose_list):
    print("Push-Up")
    return "Push-Up"
    

### main
if __name__ == "__main__":
    pose_list = csv_to_list(sys.argv[1])
    get_menu(pose_list)


