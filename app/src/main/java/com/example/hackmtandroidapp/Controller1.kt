package com.example.hackmtandroidapp

import org.jetbrains.anko.doAsync
import java.io.IOException
import java.io.PrintWriter
import java.net.Socket
import com.example.hackmtandroidapp.Inputs.FORWARD
import com.example.hackmtandroidapp.Inputs.LEFT
import com.example.hackmtandroidapp.Inputs.RIGHT
import com.example.hackmtandroidapp.Inputs.REV

public class Controller1{
    fun control(angle: Int) = when (angle){
            in 45..135 -> socket(FORWARD.data)
            in 136..225 -> socket(LEFT.data)
            in 226..315 -> socket(REV.data)
            else -> socket(RIGHT.data)
        }

    companion object {
        const val IP = "10.82.35.212"
        const val PORT = 81
    }

    fun socket(data:String){
        doAsync {
            try{
                Socket(IP, PORT).also { socket ->
                    PrintWriter(socket.getOutputStream()).apply {
                        write(data)
                        flush()
                        close()
                    }
                    socket.close()
                }
            }catch(e: IOException){
                e.printStackTrace()
            }

        }
    }
}