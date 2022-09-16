using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    GameManager gameManager;

    [SerializeField] GameObject bridgeObj;
    Bridge2 bridge;

    Vector3 hCorrection = new Vector3(0, 1.0f, 0);

    int[] curPos = new int[2] {0, 1};
    int blockLimit;
    KEY key;

    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameManager.Instance;
        gameManager.tickEvent.AddListener(TickEvt);

        bridge = bridgeObj.GetComponent<Bridge2>();
        this.transform.position = bridge.GetBlockPos(curPos[0], curPos[1]) + hCorrection;

        blockLimit = bridge.block.Count;
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
        this.transform.position = bridge.GetBlockPos(curPos[0], curPos[1]) + hCorrection;
    }
    
    void TickEvt(int mKey)
    {
        key = (KEY)mKey;
    }
}
