import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

presurvey = pd.read_excel("presurvey.xlsx")
possurvey = pd.read_excel("postsurvey.xlsx")
pretest = pd.read_excel("pretest.xlsx")
postest = pd.read_excel("posttest.xlsx")


pre_test_list1 = []
pre_test_list2 = []
pos_test_list1 = []
pos_test_list2 = []
pre_survey_list1 = []
pre_survey_list2 = []
pos_survey_list1 = []
pos_survey_list2 = []

for i in range(0, 15):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    pre_survey_list1 = pretest.iloc[i, 3:9]
    sum1 = sum(pre_survey_list1)
    pre_survey_list2.append(sum1)

    pos_test_list1 = postest.iloc[i, 3:9]
    sum2 = sum(pos_test_list1)
    pos_test_list2.append(sum2)

    pre_test_list1 = pretest.iloc[i, 3:9]
    sum3 = sum(pre_test_list1)
    pre_test_list2.append(sum3)

    pos_survey_list1 = pretest.iloc[i, 3:9]
    sum4 = sum(pos_survey_list1)
    pos_survey_list2.append(sum4)

arr = np.array(pre_survey_list2)
presurvey["TOTAL"] = arr

arr = np.array(pos_survey_list2)
possurvey["TOTAL"] = arr

arr = np.array(pre_test_list2)
pretest["TOTAL"] = arr

arr = np.array(pos_test_list2)
postest["TOTAL"] = arr


maxpretest = 0
maxpostest = 0
maxpresurvey = 0
maxpostsurvey = 0


def maximum():
    maxpretest = pretest.nlargest(5, ["TOTAL"])
    maxpostest = postest.nlargest(5, ["TOTAL"])
    maxpresurvey = presurvey.nlargest(5, ["TOTAL"])
    maxpostsurvey = possurvey.nlargest(5, ["TOTAL"])


maximum()

minpretest = 0
minpostest = 0


def minimum():
    minpretest = pretest.nsmallest(3, ["TOTAL"])
    minpostest = postest.nsmallest(3, ["TOTAL"])
    return (minpretest, minpostest)


print(minimum())

avgpre = 0


def average():
    avgpre = pretest["TOTAL"].mean()
    avgpos = postest["TOTAL"].mean()

    return (avgpre, avgpos)


print(average())


def top_performer():
    return (pretest[pretest.TOTAL == pretest.TOTAL.max()])

maxpretest = 0
maxpostest = 0
maxpresurvey = 0
maxpostsurvey = 0


def maximum():
    maxpretest = pretest.nlargest(5, ["TOTAL"])
    maxpostest = postest.nlargest(5, ["TOTAL"])
    maxpresurvey = presurvey.nlargest(5, ["TOTAL"])
    maxpostsurvey = possurvey.nlargest(5, ["TOTAL"])


maximum()

minpretest = 0
minpostest = 0


def minimum():
    minpretest = pretest.nsmallest(3, ["TOTAL"])
    minpostest = postest.nsmallest(3, ["TOTAL"])
    return (minpretest, minpostest)


print(minimum())

avgpre = 0


def average():
    avgpre = pretest["TOTAL"].mean()
    avgpos = postest["TOTAL"].mean()

    return (avgpre, avgpos)


print(average())


def top_performer():
    return (pretest[pretest.TOTAL == pretest.TOTAL.max()])


print(top_performer())


def fail():
    return (pretest[pretest["TOTAL"] < 30])


print(fail())


def fail():
    return (pretest[pretest["TOTAL"] < 30])


print(fail())

def plot_pre_survey_chart(location):
    labels = np.array(['LO1', 'LO2', 'LO3', 'LO4', 'LO5', 'LO6'])
    stats = presurvey.loc[location, labels].values
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    # close the plot
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.show()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=3)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids((angles * 180/np.pi)[0:6], labels)

    ax.set_title([presurvey.loc[location, "NAME"]])
    ax.grid(True)
    plt.savefig('output1.jpeg', dpi=300, bbox_inches='tight')
    return


def plot_post_survey_chart(location):
        labels = np.array(['LO1', 'LO2', 'LO3', 'LO4', 'LO5', 'LO6'])
        stats = possurvey.loc[location, labels].values
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        # close the plot
        stats = np.concatenate((stats, [stats[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        fig = plt.show()
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=3)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids((angles * 180/np.pi)[0:6], labels)

        ax.set_title([possurvey.loc[location, "NAME"]])
        ax.grid(True)
        plt.savefig('output2.jpeg', dpi=300, bbox_inches='tight')
        return


def plot_pre_test_chart(location):
        labels = np.array(['LO1', 'LO2', 'LO3', 'LO4', 'LO5', 'LO6'])
        stats = pretest.loc[location, labels].values
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        # close the plot
        stats = np.concatenate((stats, [stats[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        fig = plt.show()
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=3)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids((angles * 180/np.pi)[0:6], labels)

        ax.set_title([pretest.loc[location, "NAME"]])
        ax.grid(True)
        plt.savefig('output3.jpeg', dpi=300, bbox_inches='tight')
        return


def plot_post_test_chart(location):
        labels = np.array(['LO1', 'LO2', 'LO3', 'LO4', 'LO5', 'LO6'])
        stats = postest.loc[location, labels].values
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        # close the plot
        stats = np.concatenate((stats, [stats[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        fig = plt.show()
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=3)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids((angles * 180/np.pi)[0:6], labels)

        ax.set_title([postest.loc[location, "NAME"]])
        ax.grid(True)
        plt.savefig('output4.jpeg', dpi=300, bbox_inches='tight')
        return


def get_ps(ps):

    for i in range(0, 15):
        if (ps == pretest.iloc[i, 0]):
            plot_pre_survey_chart(i)
            plot_post_survey_chart(i)
            plot_pre_test_chart(i)
            plot_post_test_chart(i)




