init 999 python:
    if config.enable_steam:
        try:
            import _renpysteam as steamAPI
        except ImportError:
            config.enable_steam = False