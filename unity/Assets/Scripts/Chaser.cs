using UnityEngine;

public class Chaser : MonoBehaviour
{
    public Transform target;
    public float followSpeed = 4f;

    void Update()
    {
        if (target != null)
        {
            Vector3 pos = transform.position;
            pos = Vector3.Lerp(pos, target.position, followSpeed * Time.deltaTime);
            transform.position = pos;
        }
    }
}
