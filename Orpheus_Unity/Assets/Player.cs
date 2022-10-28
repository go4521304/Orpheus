using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class Player : MonoBehaviour
{
    GameManager gameManager;

    [SerializeField] GameObject bridgeObj;
    Bridge2 bridge;

    Vector3 hCorrection = new Vector3(0, 1.0f, 0);
    Vector3 targetPosition = new Vector3(0, 1.0f, 0);

    int[] curPos = new int[2] {0, 1};
    int blockLimit;
    float moveSpeed;
    KEY key;

    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameManager.Instance;
        gameManager.tickEvent.AddListener(TickEvt);

        bridge = bridgeObj.GetComponent<Bridge2>();
        this.transform.position = bridge.GetBlockPos(curPos[0], curPos[1]) + hCorrection;
        targetPosition = this.transform.position;

        blockLimit = bridge.block.Count;

        moveSpeed = (float)(gameManager.getBpm() / 60) * 7.5f; 
    }

    // Update is called once per frame
    void Update()
    {
        if (key == KEY.Up && curPos[1] > 0)
        {
            curPos[1] -= 1;
            key = KEY.None;
        }
        else if (key == KEY.Down && curPos[1] < 2)
        {
            curPos[1] += 1;
            key = KEY.None;
        }
        else if (key == KEY.Left && curPos[0] > 0)
        {
            curPos[0] -= 1;
            key = KEY.None;
        }
        else if (key == KEY.Right && curPos[0] < blockLimit)
        {
            curPos[0] += 1;
            key = KEY.None;
        }
        targetPosition= bridge.GetBlockPos(curPos[0], curPos[1]) + hCorrection;

        transform.position = Vector3.MoveTowards(gameObject.transform.position, targetPosition, moveSpeed * Time.deltaTime);
    }
    
    void TickEvt(int mKey)
    {
        key = (KEY)mKey;
    }
}
