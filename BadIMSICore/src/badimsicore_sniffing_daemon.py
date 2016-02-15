from daemon import Daemon


class BadIMSICoreSniffingDaemon(Daemon):
    def run(self):
        """
        You should override this method when you subclass Daemon. It will be called after the process has been
        daemonized by start() or restart().
        """