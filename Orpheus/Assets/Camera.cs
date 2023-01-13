using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera : MonoBehaviour
{
    public GameObject Target;

    private Vector3 posOffset;

    // Start is called before the first frame update
    void Start()
    {
        posOffset = transform.position - Target.transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        transform.position = Target.transform.position + posOffset;

        //transform.LookAt(Target.transform.position);
    }
}
