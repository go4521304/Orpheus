using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public int moveSpeed;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 movement = Vector3.zero;

        if (Input.GetKeyDown(KeyCode.LeftArrow)) 
        {
            movement.x -= moveSpeed * Time.deltaTime;
            movement.y -= (moveSpeed * 2) * Time.deltaTime;
        }

        if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            movement.x += moveSpeed * Time.deltaTime;
            movement.y += (moveSpeed * 2) * Time.deltaTime;
        }

        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            movement.y += moveSpeed * Time.deltaTime;
        }

        transform.position += movement;
    }
}
