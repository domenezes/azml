from azureml.core.workspace import Workspace
from azureml.core import Experiment
ws = Workspace.from_config()
for experiment in ws.experiments:
    #if (sys.argv[1] in experiment):
        print( "experiment->" + experiment + "<" )
        for run in Experiment(ws, experiment).get_runs():
            print ( "  run->" + run.get_status() + "<" )
            if ( run.get_status() == "Running" ):
                run.cancel()
                #run.complete()
                print( "    cancelled->" + experiment + "<" )