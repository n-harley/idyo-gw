import pickle
import numpy as np
import pandas
import matplotlib.pyplot as plt

with open('gridworld-data.pkl', 'rb') as f:
    data = pickle.load(f)

with open('gridworld-states.pickle', 'rb') as f:
    states = pickle.load(f)

action_labels = ['start','forward','left','right','pickup','toggle']
orientation_rotation = [0,270,180,90]

def load_data(filename):
    return pandas.read_csv(filename)

def mission(data,id):
    return data.loc[data["melody.id"]==id]

def mission_length(data,id):
    stateT = states[id-1]
    return len(stateT)

def event(data,id,s):
    M = mission(data,id)
    S = M.loc[s]
    return S.to_dict()

def state(data,id,s):
    return states[id-1][s-1]

def ic(data,id):
    return mission(data,id)["information.content"].values

def ig(data,id):
    return mission(data,id)["information.gain"].values

def h(data,id):
    return mission(data,id)['entropy'].values

def h_ic(data,id):
    return h(data,id) / ic(data,id)

def action(data,id):
    return mission(data,id)['action'].values

def orientation(data,id):
    return mission(data,id)['orientation'].values

def agent_coords(data,id):
    agent_x = mission(data,id)['agentx'].values
    agent_y = mission(data,id)['agenty'].values
    return list(zip(agent_x,agent_y))

def pickup(data,id):
    return np.where(action(data,id) == 4)[0][0]

def ic_diff(data,id):
    return np.insert(np.diff(ic(data,id)),0,[0])

def h_diff(data,id):
    return np.insert(np.diff(h(data,id)),0,[0])

def ig_diff(data,id):
    return np.insert(np.diff(ig(data,id)),0,[0])

def min_ic(data,id):
    return np.argmin(ic(data,id))

def min_h(data,id):
    return np.argmin(h(data,id))

def max_h_diff(data,id):
    return np.argmax(h_diff(data,id))

def max_ic_diff(data,id):
    return np.argmax(ic_diff(data,id))

def max_ig_diff(data,id):
    return np.argmax(ig_diff(data,id))

def max_h_ic(data,id):
    return np.argmax(h_ic(data,id))

def plot(data,label):
    plt.plot(data,label=label)
    plt.legend()

def set_xaxis(acns):
    acn_ls = [action_labels[a] for a in acns]
    plt.xticks(np.arange(len(acns)),acn_ls,rotation='vertical')
    plt.xlabel('action')
    plt.xlim(0,len(acns)-1)

def mark(loc,c='y',linestyle='-',label=''):
    plt.axvline(loc,-10,10,c=c,linestyle=linestyle)
    plt.text(loc,1,label,rotation=90)


def display_state(data,id,s,a,o):
    state = states[id-1][s-1]
    agt_xy = agent_coords(data,id)[s-1]
    agt_x = agt_xy[0]
    agt_y = agt_xy[1]
    s = np.flip(state,axis=0)
    plt.imshow(s/10)
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.set_yticks([])
    plt.ylabel(a, fontsize='xx-large', fontweight='heavy')
    plt.text(agt_x-0.25,7.25-agt_y,"^",fontsize='xx-large',rotation=o,fontweight='heavy')

def display_mission(data,id):
    stateT = states[id-1]
    actions = action(data,id)
    orientations = orientation(data,id)
    acn_ls = [action_labels[a] for a in actions]
    orn_rs = [orientation_rotation[o] for o in orientations]
    rows = int(np.ceil(len(stateT)/5))
    fig = plt.gcf()
    fig = plt.figure(figsize=(20,5*rows))
    for i in range(1,len(stateT)):
        plt.subplot(rows,5,i)
        display_state(data,id,i,acn_ls[i-1],orn_rs[i-1])
