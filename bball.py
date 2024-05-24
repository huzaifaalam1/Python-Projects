'''
File: bball.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program defines classes for
        managing sports teams, conferences,
        and conference sets. It provides 
        functionality to organize teams into 
        conferences, calculate average win ratios
        for conferences, and identify conferences
        with the highest average win ratio.
'''
class Team:
    '''
    Represents a sports team with its name, conference, and win ratio.
    '''
    def __init__(self, line):
        '''
        Initialize a Team object.

        Args:
            line (str): A string containing the team's name, conference, wins, and losses
        '''
        # strip and split the data to initialize 
        parts = line.split('(')
        name_conf = parts[0].strip()
        self._name = ' '.join(name_conf.split()[:-1])
        self._conf = parts[-1].split(')')[0].strip()
        stats = parts[-1].split(')')[1].strip().split()
        self._wins = int(stats[0])
        self._losses = int(stats[1])
        self._ratio = self._wins / (self._wins + self._losses)

    def name(self):
        '''
        Get the name of the team.

        Returns:
            A string name of the team.
        '''
        return self._name
    
    def conf(self):
        '''
        Get the conference of the team.

        Returns:
            A string conference of the team.
        '''
        return self._conf
    
    def win_ratio(self):
        '''
        Get the win ratio of the team.

        Returns:
            A float win ratio of the team.
        '''
        return self._ratio

    def __str__(self):
        '''
        String representation of the Team object.

        Returns:
            The formatted string containing the team's name and win ratio.
        '''
        return "{} : {}".format(self._name, self.win_ratio())

class Conference:
    '''
    Represents a conference containing multiple teams.
    '''
    def __init__(self, conf):
        '''
        Initialize a Conference object.

        Args:
            The name of the conference.
        '''
        self._name = conf
        self._teams = []

    def __contains__(self, team):
        '''
        Check if a team is present in the conference.

        Args:
            The team to check for membership in the conference.

        Returns:
            A boolean value True if the team is in the conference, False otherwise.
        '''
        for teams in self._teams:
            if teams == team:
                return True
        return False

    def name(self):
        '''Get the name of the conference.

        Returns:
            The name of the conference.
        '''
        return self._name

    def add(self, team):
        '''
        Add a team to the conference.

        Args:
            The team to add to the conference.
        '''
        for teams in self._teams:
            if teams == team:
                break
        else:
            self._teams.append(team)


    def win_ratio_avg(self):
        '''
        Calculate the average win ratio of all teams in the conference.

        Returns:
            The average win ratio of the conference's teams.
        '''
        total_win_ratio = 0
        if self._teams:
            for team in self._teams:
                total_win_ratio += team.win_ratio()
            return total_win_ratio / len(self._teams)
        else:
            return 0.0

    def __str__(self):
        '''
        String representation of the Conference object.

        Returns:
            The formatted string containing the conference's name and average win ratio.
        '''
        return "{} : {}".format(self._name, self.win_ratio_avg())


class ConferenceSet:
    '''
    Represents a set of conferences.
    '''
    def __init__(self):
        '''
        Initialize a ConferenceSet object.
        '''
        self._conferences = []

    def add(self, team):
        '''
        Add a team to the appropriate conference in the set.

        Args:
            The team to add to a conference.
        '''
        # Find the conference name of the team
        conf_name = team.conf()
        fixed = False
        # Check each conference in the set
        for conf in self._conferences:
            # If the team's conference matches the conference in the set
            if conf.name() == conf_name:
                # Add the team to the conference
                conf.add(team)
                fixed = True
                break
        # If the team's conference was not found, create a new conference
        if not fixed:
            new_conf = Conference(conf_name)
            new_conf.add(team)
            self._conferences.append(new_conf)

    def best(self):
        '''
        Find the conference(s) with the highest average win ratio.

        Returns:
            A list of Conference objects with the highest average win ratio.
        '''
        # If there are no conferences, return an empty list
        if not self._conferences:
            return []
        # Find the highest average win ratio among conferences
        highest_avg = 0
        for conf in self._conferences:
            if conf.win_ratio_avg() > highest_avg:
                highest_avg = conf.win_ratio_avg()
        # Collect conferences with the highest average win ratio
        best_conf = []
        for conf in self._conferences:
            if conf.win_ratio_avg() == highest_avg:
                best_conf.append(conf)
        # Sort the conferences
        sorted_conf = []
        while best_conf:
            min_conf = best_conf[0]
            for conf in best_conf:
                if conf.name() < min_conf.name():
                    min_conf = conf
            sorted_conf.append(min_conf)
            best_conf.remove(min_conf)

        return sorted_conf

    def __repr__(self):
        '''
        Representation of the ConferenceSet object.

        Returns:
            string representation of the ConferenceSet object.
        '''
        return repr(self._conferences)


def main():
    file_name = input()
    filename = open(file_name, 'r')
    conf_set = ConferenceSet()
    for line in filename:
        if line[0] != "#":
            team = Team(line)
            conf_set.add(team)
    best_conf = conf_set.best()
    for conf in best_conf:
        print("{} : {}".format(conf.name(), conf.win_ratio_avg()))
    filename.close()

main()
