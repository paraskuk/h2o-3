package ai.h2o.webserver.iface;

public interface WebServer {

  void start(String ip, int port) throws Exception;

  void stop() throws Exception;

}
