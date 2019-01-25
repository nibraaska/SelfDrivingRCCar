package com.example.hackmtandroidapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        final TextView TVangle = (TextView) findViewById(R.id.angleVal);
        final TextView TVstrength = (TextView) findViewById(R.id.strengthVal);

        final JoystickView joystick = (JoystickView) findViewById(R.id.joystickView_left);

        joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {
                TVangle.setText("ANGLE:" + String.valueOf(angle));
                TVstrength.setText("STRENGTH:" + String.valueOf(strength));

                if((angle > 250) && (angle < 290)){
                    TVangle.setText(-1 + "");
                    TVangle.setTextSize(20);
                }

                if((angle > 75) && (angle < 110)){
                    TVangle.setText(1 + "");
                    TVangle.setTextSize(20);
                }

                if((angle > 165) && (angle < 205)){
                    TVangle.setText(-1 + "");
                    TVangle.setTextSize(20);
                }

                if((angle > 345) || (angle < 15)){
                    TVangle.setText(1 + "");
                    TVangle.setTextSize(20);
                }

            }
        });
    }
}
