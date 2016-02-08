import org.junit.Test;

import java.io.IOException;

import static org.junit.Assert.assertNotEquals;

/**
 * Created by johnny on 08/02/16.
 */
public class PythonCallerTest {

    @Test(expected = NullPointerException.class)
    public void testNoArgs() {
        PythonCaller pc = new PythonCaller(null);
    }

    @Test
    public void testSuccessArgs() {
        String[] args = new String[1];
        args[0] = "../../BadIMSICore/badimsicore_openbts_init.py";
        PythonCaller pc = new PythonCaller(args);
    }

    @Test
    public void testCommandFailed() throws IOException {
        String[] args = new String[1];
        args[0] = "../../BadIMSICore/badimsicore_openbts_init.py";
        PythonCaller pc = new PythonCaller(args);
        int exitValue = pc.process();
        assertNotEquals(exitValue, 0);
    }

}