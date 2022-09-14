using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class Bridge2 : MonoBehaviour
{
    GameManager gameManager;

    [SerializeField] GameObject bridge;
    [SerializeField] float length;
    [SerializeField][Range(1f, 20f)] float speed;

    public List<GameObject> bridges = new List<GameObject>();

    float width = 36.754f;

    private KEY key = KEY.None;

    private bool isUpdate = false;

    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameManager.Instance;
        gameManager.tickEvent.AddListener(TickEvt);

        GameObject obj;
        Vector3 pos = new Vector3(10.615f, -2.211f, 0);

        while (bridges.Count * width < length)
        {
            pos.x += width;
            obj = Instantiate(bridge) as GameObject;
            obj.transform.parent = transform;
            obj.transform.position = pos;

            bridges.Add(obj);
        }

    }

    // Update is called once per frame
    void Update()
    {
        if (key == KEY.Up)
        {

        }
        else if (key == KEY.Down)
        {

        }
        else if (key == KEY.Left)
        {

        }
        else if (key == KEY.Right)
        {

        }
        //transform.Translate(Vector2.right * Time.deltaTime * speed);
    }

    void TickEvt(int mKey)
    {
        key = (KEY)mKey;
    }
}
