Description
Your task is to create the data model and simple HTTP-based interface to manage Experiments
(A/B tests) and Teams. An experiment has two main attributes: a description and a sample ratio.
Each experiment has either 1 or 2 teams assigned to it. Each team has a name. Each team can
have any number of experiments.

Requirements
1. API to create and list experiments
Create an HTTP interface to create a new experiment and to list all existing experiments.
Listing must allow filtering by team.
2. API to change team assignments
Once an experiment was created, the number of teams cannot be changed, but
individual team assignments can be changed. E.g. an experiment can change from
teams A, B to teams A, C or D, E.
3. Team hierarchy
A team can optionally have a parent team. Expand the data model and change the
team-filter to include experiments of all child teams and restrict that the teams assigned
to an experiment cannot be a descendant of each other.
Provide a solution that you like and that can act as a healthy base for further development.
