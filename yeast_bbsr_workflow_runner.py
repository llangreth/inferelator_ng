from inferelator_ng.yeast_bbsr_workflow import Yeast_Bbsr_Workflow

workflow = Yeast_Bbsr_Workflow()
# Common configuration parameters
workflow.input_dir = 'data/yeast'
workflow.num_bootstraps = 2
workflow.delTmax = 110
workflow.delTmin = 0
workflow.tau = 45
workflow.run() 