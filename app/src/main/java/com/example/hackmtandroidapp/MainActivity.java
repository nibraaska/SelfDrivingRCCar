package com.example.hackmtandroidapp;

import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.os.Message;


import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {

    public static Handler handler;
    public static int CONNECTION_ERROR;
    public static int CONNECTION_LOST;
    public SocketClientThread socketClient;
    public String host = "10.82.35.212";
    public int port = 80;
    public int test = 10;

    //10.82.35.212;5000
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //
        final Controller1 controller = new Controller1();
        //
        socketClient = new SocketClientThread(host, port);

        final TextView TVangle = (TextView) findViewById(R.id.angleVal);
        final TextView TVstrength = (TextView) findViewById(R.id.strengthVal);

        final JoystickView joystick = (JoystickView) findViewById(R.id.joystickView_left);

        socketClient.sendCommand(test);

        joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {
                TVangle.setText("ANGLE:" + String.valueOf(angle));
                TVstrength.setText("STRENGTH:" + String.valueOf(strength));

                controller.control(angle);


            }
        });
    }
}
