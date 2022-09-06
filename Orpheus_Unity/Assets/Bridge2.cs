using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bridge2 : MonoBehaviour
{
    [SerializeField] GameObject bridge;

    [SerializeField] float length;

    [SerializeField][Range(1f, 20f)] float speed;

    public List<GameObject> bridges = new List<GameObject>();

    float width = 36.754f;

    // Start is called before the first frame update
    void Start()
    {
        GameObject obj;
        Vector3 pos = new Vector3(10.146f, -2.25f, 0);

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
        transform.position = Vector2.left * Time.time * speed;
    }
}
