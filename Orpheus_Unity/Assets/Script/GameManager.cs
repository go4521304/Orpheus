using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    private enum KEY {None, Up, Down, Left, Right};
    private KEY key = KEY.None;
    private double time = 1;


    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (time < 0)
        {
            // Processing
            Debug.Log("Test");

            time = 1;
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
