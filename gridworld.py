import pickle
import os
import numpy as np
import pandas
import matplotlib.pyplot as plt

with open('gridworld-data.pkl', 'rb') as f:
    data = pickle.load(f)

with open('gridworld-states.pickle', 'rb') as f:
    states = pickle.load(f)

action_labels = ['start','forward','left','right','pickup','toggle']
orientation_rotation = [0,270,180,90]

def list_model_names():
    def rm_ext(fn):
        return fn[:fn.find(".")]
    
    model_filenames = os.listdir("models/")
    return [rm_ext(mfn) for mfn in model_filenames]

def load_data(model_name):
    return pandas.read_csv("models/"+model_name+".csv")

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

def en(data,id):
    return mission(data,id)['entropy'].values

def en_ic(data,id):
    return np.array([x/y for (x,y) in zip(en(data,id),ic(data,id))])

def ig_ic(data,id):
    return np.array([x/y for (x,y) in zip(ig(data,id),ic(data,id))])

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

def en_diff(data,id):
    return np.insert(np.diff(en(data,id)),0,[0])

def ig_diff(data,id):
    return np.insert(np.diff(ig(data,id)),0,[0])

def min_ic(data,id):
    return np.argmin(ic(data,id)[:-1])

def min_en(data,id):
    return np.argmin(en(data,id)[:-1])

def max_en_diff(data,id):
    return np.argmax(en_diff(data,id)[2:-1])+2

def max_en_diff_minus1(data,id):
    return max_en_diff(data,id)-1

def max_ic_diff(data,id):
    return np.argmax(ic_diff(data,id)[2:-1])+2

def max_ic_diff_minus1(data,id):
    return max_ic_diff(data,id)-1

def max_ig_diff(data,id):
    return np.argmax(ig_diff(data,id)[2:-1])+2

def max_ig_diff_minus1(data,id):
    return max_ig_diff(data,id)-1

def max_en_ic(data,id):
    return np.argmax(en_ic(data,id)[1:-1])+1

def max_ig_ic(data,id):
    return np.argmax(ig_ic(data,id)[1:-1])+1

def eval_mission(data,id,estimator):
    return pickup(data,id) == estimator(data,id)

def eval_model(data,estimator):
    res = np.array([eval_mission(data,i,estimator) for i in np.arange(1,1000)])
    return len(np.where(res)[0])

def plot(data,label):
    plt.plot(data,label=label)
    plt.legend()

def set_xaxis(acns):
    acn_ls = [action_labels[a] for a in acns]
    plt.xticks(np.arange(len(acns)),acn_ls,rotation='vertical')
    plt.xlabel('action')
    plt.xlim(0,len(acns)-1)

def mark(loc,c='k',linestyle='-',label='',line=False,pos=1):
    ax = plt.gca()        
    if line:
        plt.axvline(loc,-10,10,c=c,linestyle=linestyle)
    else:
        ax.annotate(label,(loc,pos),fontsize='large',horizontalalignment='right', verticalalignment='center')
        ax.scatter([loc],[pos],s=200,color=c,marker='x',linewidth=4)
        #plt.scatter([loc],[ypos],s=100,c=c,marker='x')
        #plt.text(loc,ypos+0.3,label)
    


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
    ax.annotate('^', (agt_x,7-agt_y),fontsize='xx-large',rotation=o,fontweight='heavy',horizontalalignment='center', verticalalignment='center')
    plt.ylabel(a, fontsize='xx-large', fontweight='heavy')

def display_mission(data,id):
    stateT = states[id-1]
    actions = action(data,id)
    orientations = orientation(data,id)
    acn_ls = [action_labels[a] for a in actions]
    orn_rs = [orientation_rotation[o] for o in orientations]
    rows = int(np.ceil(len(stateT)/5))
    fig = plt.gcf()
    fig = plt.figure(figsize=(20,5*rows))
    for i in range(1,len(stateT)+1):
        plt.subplot(rows,5,i)
        display_state(data,id,i,acn_ls[i-1],orn_rs[i-1])
