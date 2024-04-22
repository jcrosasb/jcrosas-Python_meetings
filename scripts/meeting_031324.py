from dataclasses import dataclass

@dataclass
class FollowResearch1:

    id: int
    name: str
    parameters: dict


@dataclass
class FollowResearch2:

    experiment_date: str
    results: str


@dataclass
class ChildClass(FollowResearch1):
    
    comments: str


if __name__ == '__main__':

    experiment1 = FollowResearch1(id=1, 
                                 name='first_experiment', 
                                 parameters={'a': 1, 'b':2})
                                #  experiment_date='2024/03/13', 
                                #  results='success')
    
    print(experiment1)

    experiment2 = ChildClass(id=1, 
                             name='first_experiment', 
                             parameters={'a': 1, 'b':2},
                            #  experiment_date='2024/03/13', 
                            #  results='success',
                             comments='something')
    
    print(experiment2.id)
    print(experiment2.name)
    print(experiment2.parameters)
    # print(experiment2.experiment_date)
    # print(experiment2.results)
    # print(experiment2.comments)


