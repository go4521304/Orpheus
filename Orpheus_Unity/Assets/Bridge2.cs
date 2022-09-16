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

    // 발판
    [SerializeField] List<GameObject> blocks;
    public List<GameObject[]> block = new List<GameObject[]>();
    float blockWidth = 1.5f;


    public List<GameObject> bridges = new List<GameObject>();

    float width = 36.754f;

    private KEY key = KEY.None;

    private bool isUpdate = false;

    private void Awake()
    {
        // 브릿지 생성 코드
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

        // 발판 생성 코드
        Vector3[] blockPos = new Vector3[3];
        blockPos[0] = new Vector3(-6.293f, 0.371f, 0);
        blockPos[1] = new Vector3(-7.023f, -0.092f, 0);
        blockPos[2] = new Vector3(-7.763f, -0.55f, 0);

        while (block.Count * blockWidth < length)
        {
            GameObject[] blockObj = new GameObject[3];

            for (int i = 0; i < 3; i++)
            {
                blockObj[i] = Instantiate(blocks[0]) as GameObject;
                blockObj[i].transform.parent = transform;
                blockObj[i].transform.position = blockPos[i];
                blockObj[i].GetComponent<SpriteRenderer>().sortingOrder = i + 1;

                blockPos[i].x += blockWidth;
            }

            block.Add(blockObj);
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        gameManager = GameManager.Instance;
        gameManager.tickEvent.AddListener(TickEvt);
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

    public Vector3 GetBlockPos(int i, int j)
    {
        return block[i][j].transform.position;
    }
}
