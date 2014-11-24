from qiime.core.registry import plugin_registry

class Executor(object):
    def __init__(self, job):
        self.job = job

    def __call__(self):
        method_uri = self.job.workflow.template # TODO currently the template is just the method
        method = plugin_registry.get_plugin(method_uri).get_method(method_uri)

        study = self.job.study.id
        artifact_uris = [a.artifact.uri for a in self.job.artifacts]
        method(study, *artifact_uris)