using System;
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.Device;
using UnityEngine.Events;
using UnityEngine.UIElements;
using Screen = UnityEngine.Device.Screen;

enum KEY { None, Up, Down, Left, Right, Limit };

[System.Serializable] public class TickEvent : UnityEvent<int> { }

public class GameManager : MonoBehaviour
{
    private static GameManager gameManager = null;

    public static GameManager Instance
    {
        get
        {
            if (gameManager != null)
                return gameManager;
            else
                return null;
        }
    }

    public TickEvent tickEvent;

    private KEY key = KEY.None;

    [SerializeField] private int Bpm = 60;
    [SerializeField] private double Tempo = 1;

    private double timeGap;

    private double time = 1;


    private void Awake()
    {
        Screen.SetResolution(1920, 1080, true);

        if (gameManager == null)
        {
            gameManager = this;

            DontDestroyOnLoad(this);
        }
        else
        {
            Destroy(this);
        }

        tickEvent = new TickEvent();

        timeGap = (Bpm / 60) * Tempo;
        time = timeGap;
    }

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (time < 0)
        {
            tickEvent.Invoke((int)key);

            // Processing
            if (key != KEY.None)
                Debug.Log(key);

            time = timeGap;
            key = KEY.None;
        }
        else
        {
            time -= Time.deltaTime;

            if (Input.GetKeyDown(KeyCode.UpArrow))
                key = KEY.Up;
            else if (Input.GetKeyDown(KeyCode.DownArrow))
                key = KEY.Down;
            else if (Input.GetKeyDown(KeyCode.LeftArrow))
                key = KEY.Left;
            else if (Input.GetKeyDown(KeyCode.RightArrow))
                key = KEY.Right;
        }
    }
}
