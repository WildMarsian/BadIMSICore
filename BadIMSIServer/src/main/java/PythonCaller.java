import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.Objects;


/**
 * Python Caller is a class that calls python code and return the result in the stdout.
 */
public class PythonCaller {

    private String program = "python";
    private String[] scriptPath;

    public PythonCaller(String[] scriptPath) {
        this.scriptPath = Objects.requireNonNull(scriptPath);
    }

    public int process() throws IOException {
        Runtime rt = Runtime.getRuntime();

        StringBuilder sb = new StringBuilder();
        sb.append(program);
        sb.append(" ");
        for (int i = 0;i<scriptPath.length;i++) {
            sb.append(scriptPath[i]);
            sb.append(" ");
        }

        System.out.println(sb.toString());

        Process pr = rt.exec(sb.toString());
        BufferedReader bfr = new BufferedReader(new InputStreamReader(pr.getInputStream()));
        String line;
        while ((line = bfr.readLine()) != null) {
            System.out.println(line);
        }

        int val = 1;
        try {
            val = pr.waitFor();
            return val;
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
            return -1;
    }

    public static String getCleanPath() {
        URL location = PythonCaller.class.getProtectionDomain().getCodeSource()
                .getLocation();
        String path = location.getFile();
        return new File(path).getParent();
    }

    public static void main(String[] args) {
        if(args.length == 0) {
            noArgsError();
        }

        if(args.length > 0) {
            //System.out.println(getCleanPath());
            PythonCaller pc = new PythonCaller(args);
            try {
                int exitValue = pc.process();
                System.out.println("Exit value : "+exitValue);

            } catch (IOException e) {
                errorOnScript(args);
                e.printStackTrace();
            }
        }

    }

    private static void noArgsError() {
        System.out.println("No arguments were found");
    }

    private static void errorOnScript(String[] args) {
        StringBuilder sb = new StringBuilder();
        for (String arg : args) {
            sb.append(arg+" ");
        }
        System.out.println("Error on the script : no script found for "+sb.toString());
    }
}
