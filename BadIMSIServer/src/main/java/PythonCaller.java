import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;

/**
 * Python Caller, for
 */
public class PythonCaller {

    private String[] command;

    public PythonCaller(String scriptPath) {
        this.command = new String[4];
        this.command[0] = "python";
        this.command[1] = scriptPath;
        this.command[2] = "-i";
        this.command[3] = "smqueue.txt";
    }

    public void process() throws IOException {
        Runtime rt = Runtime.getRuntime();
        //Process pr = rt.exec(this.command);
        String cmd = this.command[0] + " " + this.command[1];
        Process pr = rt.exec(command);
        System.out.println(cmd);
        BufferedReader bfr = new BufferedReader(new InputStreamReader(pr.getInputStream()));
        String line;
        while ((line = bfr.readLine()) != null) {
            System.out.println(line);
        }
    }

    public static String getCleanPath() {
        URL location = PythonCaller.class.getProtectionDomain().getCodeSource()
                .getLocation();
        String path = location.getFile();

        return new File(path).getParent();
    }

    public static void main(String[] args) {
        System.out.println(getCleanPath());
        PythonCaller pc = new PythonCaller("badimsicore_sms_interceptor.py");
        try {
            pc.process();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
