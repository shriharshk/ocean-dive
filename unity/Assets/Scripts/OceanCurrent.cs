using UnityEngine;

public class OceanCurrent : MonoBehaviour
{
    void OnTriggerExit2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            GameManager gm = FindObjectOfType<GameManager>();
            if (gm != null)
            {
                gm.Hurt();
            }

            // Keep the player inside the current bounds
            var bounds = GetComponent<Collider2D>().bounds;
            Vector3 pos = other.transform.position;
            pos.y = Mathf.Clamp(pos.y, bounds.min.y, bounds.max.y);
            other.transform.position = pos;
        }
    }
}
