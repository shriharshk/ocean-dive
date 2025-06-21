using UnityEngine;
using System.Collections.Generic;

public class GameManager : MonoBehaviour
{
    public GameObject obstaclePrefab;
    public float spawnInterval = 2f;
    public float obstacleSpeed = 5f;
    public int maxHealth = 3;

    private float timer = 0f;
    private int health;
    private readonly List<GameObject> obstacles = new();
    private AudioSource audioSource;

    void Start()
    {
        health = maxHealth;
        audioSource = GetComponent<AudioSource>();
        if (audioSource != null)
        {
            audioSource.loop = true;
            audioSource.Play();
        }
    }

    void Update()
    {
        timer += Time.deltaTime;
        if (timer >= spawnInterval)
        {
            SpawnObstacle();
            timer = 0f;
        }

        for (int i = obstacles.Count - 1; i >= 0; i--)
        {
            obstacles[i].transform.Translate(Vector3.left * obstacleSpeed * Time.deltaTime);
            if (obstacles[i].transform.position.x < -10f)
            {
                Destroy(obstacles[i]);
                obstacles.RemoveAt(i);
            }
        }
    }

    void SpawnObstacle()
    {
        Vector3 pos = new Vector3(10f, Random.Range(-3f, 3f), 0f);
        obstacles.Add(Instantiate(obstaclePrefab, pos, Quaternion.identity));
    }

    public void Hurt()
    {
        health -= 1;
        Debug.Log("Hurt! Health: " + health);
        if (health <= 0)
        {
            Debug.Log("Game Over!");
        }
    }
}
