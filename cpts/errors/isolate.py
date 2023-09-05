from cpts.errors.base import CPTSBaseError


class CPTSIsolateBaseError(CPTSBaseError):
    pass


class FailedToInitEnvError(CPTSBaseError):
    pass


class EnvAlreadyExistsError(FailedToInitEnvError):
    pass
