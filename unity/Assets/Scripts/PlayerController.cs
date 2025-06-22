using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float forwardSpeed = 5f;
    public float verticalSpeed = 5f;
    private Rigidbody2D rb;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        float v = Input.GetAxisRaw("Vertical");
        Vector2 vel = rb.velocity;
        vel.x = forwardSpeed;
        vel.y = v * verticalSpeed;
        rb.velocity = vel;
    }
}
