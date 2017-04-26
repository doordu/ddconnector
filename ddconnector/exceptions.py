
class DecodeException(Exception):
    """
    解码异常
    """
    pass


class FormatException(Exception):
    """
    格式错误
    """
    pass


class UnkownCommandException(Exception):
    """
    未知命令
    """
    pass
    
class GuidDisonnected(Exception):
    """
    设置未连接
    """
    pass