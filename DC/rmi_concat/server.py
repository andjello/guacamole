import Pyro5.api

@Pyro5.api.expose
class StringService:
    def concatenate(self, str1, str2):
        return str1 + str2

def main():
    daemon = Pyro5.server.Daemon()                 # Start Pyro daemon
    uri = daemon.register(StringService)           # Register the class as a Pyro object
    print("Ready. Object URI =", uri)
    daemon.requestLoop()                           # Wait for calls

if __name__ == "__main__":
    main()
