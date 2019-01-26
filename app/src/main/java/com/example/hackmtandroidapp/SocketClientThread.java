package com.example.hackmtandroidapp;

import android.os.Message;
import android.util.Log;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

//10.82.35.212;5000
public class SocketClientThread extends Thread {
    private String host;
    private int port;

    private final Object lock = new Object();
    private boolean running = true;

    private int value = 0;

    private Socket socket = null;

    public SocketClientThread(String host, int port)
    {
        this.host = host;
        this.port = port;
    }

    private void openSocket() throws IOException
    {
        try
        {
            InetSocketAddress address = new InetSocketAddress(host, port);
            InetAddress servAddress = InetAddress.getByName(host);
            //String address =  host+":"+port;
            socket = new Socket(servAddress,port);
            if(address != null) {
                socket.connect(address, 1000);
                Log.i("Car", "Connected to " + host + " port " + port);
            }else{
                Log.i("Tag", "This shouldn't happen");
            }
        }
        catch (IOException e)
        {
            Log.e("Car","Socket open failed" + e.getMessage());
            Message msg = MainActivity.handler.obtainMessage(MainActivity.CONNECTION_ERROR, e.getMessage());
            MainActivity.handler.sendMessage(msg);
            throw e;
        }
    }

    @Override
    public void run()
    {
        try
        {
            openSocket();
        }catch (IOException e)
        {
            return;
        }

        try
        {
            while(running)
            {
                synchronized (lock)
                {
                    lock.wait();

                    carCommand(); //Define


                }
            }
        }
        catch (InterruptedException e)
        {
            running = false;
        }
    }

    private void carCommand()
    {
        if(!running)
            return;

        if(socket == null || !socket.isConnected())
        {
            Log.i("CarCommand", "Retrying COnnection");
            try
            {
                openSocket();
            }
            catch(IOException e)
            {
                running = false;
                return;
            }
        }

        try
        {
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            writer.println(value);
            writer.flush();
        }
        catch (IOException e)
        {
            Log.e("CarCommand", "Socket write failed" + e.getMessage());
            Message msg = MainActivity.handler.obtainMessage(MainActivity.CONNECTION_LOST, e.getMessage());
            MainActivity.handler.sendMessage(msg);
            socket = null;
        }

        //value = 0;
    }

    public synchronized void sendCommand(int sendValue)
    {
        synchronized (lock)
        {
            this.value = sendValue;
            lock.notify();
        }
    }

    public void stopRunning()
    {
        synchronized (lock)
        {
            running = false;
            if (socket!=null)
            {
                try
                {
                    socket.close();
                }catch (IOException e)
                {
                    //Ignore
                }
            }
            lock.notify();
        }
    }
}
