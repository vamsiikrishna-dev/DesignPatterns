from Facadee import Linkedin
from Models import User, Profile, Education, Experience, Skill, JobPosting, JobState
from NotificationService import NotificationType


def main():
    # =============================================
    # Initialize LinkedIn Platform
    # =============================================
    linkedin = Linkedin()
    print("=" * 60)
    print("LinkedIn Low-Level Design - Demo")
    print("=" * 60)

    # =============================================
    # 1. Register Users
    # =============================================
    print("\n--- 1. Registering Users ---")
    alice = User("alice_dev", "password123")
    bob = User("bob_engineer", "securepass")
    charlie = User("charlie_pm", "mypass456")

    linkedin.register_user(alice)
    linkedin.register_user(bob)
    linkedin.register_user(charlie)
    print(f"Registered: {alice}")
    print(f"Registered: {bob}")
    print(f"Registered: {charlie}")

    # =============================================
    # 2. Login
    # =============================================
    print("\n--- 2. Login ---")
    try:
        logged_in_user = linkedin.login("alice_dev", "password123")
        print(f"Logged in as: {logged_in_user}")
    except Exception as e:
        print(f"Login failed: {e}")

    try:
        linkedin.login("alice_dev", "wrongpassword")
    except Exception as e:
        print(f"Expected failure: {e}")

    # =============================================
    # 3. Create Profiles
    # =============================================
    print("\n--- 3. Creating Profiles ---")
    alice_profile = Profile(
        heading="Senior Software Engineer",
        summary="Passionate about building scalable systems",
        experience=[
            Experience("Amazon", "SDE II", "2021-01-01", "2024-01-01"),
            Experience("Google", "SDE I", "2019-06-01", "2020-12-31"),
        ],
        education=[
            Education("MIT", "B.S. Computer Science", "2015-09-01", "2019-05-01"),
        ],
        skills=[
            Skill("Python"),
            Skill("System Design"),
            Skill("AWS"),
        ]
    )
    linkedin.create_profile(alice, alice_profile)
    print(alice.get_profile())

    bob_profile = Profile(
        heading="Backend Engineer",
        summary="Java and distributed systems enthusiast",
        experience=[
            Experience("Microsoft", "Software Engineer", "2020-03-01"),
        ],
        education=[
            Education("Stanford", "M.S. Computer Science", "2018-09-01", "2020-03-01"),
        ],
        skills=[
            Skill("Java"),
            Skill("Kafka"),
            Skill("Microservices"),
        ]
    )
    linkedin.create_profile(bob, bob_profile)
    print(bob.get_profile())

    # =============================================
    # 4. Connection Requests
    # =============================================
    print("\n--- 4. Connection Requests ---")

    # Alice sends connection request to Bob
    linkedin.send_connection_request(alice, bob)
    print(f"{alice.get_username()} sent connection request to {bob.get_username()}")
    print(f"{bob.get_username()}'s pending requests: {bob.get_connection_requests()}")

    # Bob accepts Alice's request
    linkedin.accept_connection(bob, alice)
    print(f"{bob.get_username()} accepted {alice.get_username()}'s request")
    print(f"Bob: {bob}")
    print(f"Alice: {alice}")

    # Charlie sends request to Alice
    linkedin.send_connection_request(charlie, alice)
    linkedin.accept_connection(alice, charlie)
    print(f"Alice after accepting Charlie: {alice}")

    # =============================================
    # 5. Post Jobs
    # =============================================
    print("\n--- 5. Posting Jobs ---")
    job1 = JobPosting(
        position="Senior Python Developer",
        experience="5+ years",
        location="Seattle, WA",
        description="Build scalable backend services using Python and AWS",
        skills=["Python", "AWS", "Microservices"],
        state=JobState.OPEN
    )
    job2 = JobPosting(
        position="Product Manager",
        experience="3+ years",
        location="San Francisco, CA",
        description="Lead product strategy for enterprise SaaS platform",
        skills=["Product Strategy", "Agile", "Data Analysis"],
        state=JobState.OPEN
    )
    linkedin.post_job(job1)
    linkedin.post_job(job2)
    print(job1)
    print(job2)

    # Close a job
    job2.set_state(JobState.CLOSED)
    print(f"After closing: {job2}")

    # =============================================
    # 6. Notifications
    # =============================================
    print("\n--- 6. Sending Notifications ---")
    linkedin.send_notification(
        sender=alice,
        receiver=bob,
        content="Alice viewed your profile",
        notification_type=NotificationType.MESSAGE
    )
    linkedin.send_notification(
        sender=charlie,
        receiver=alice,
        content="New job matching your skills: Senior Python Developer",
        notification_type=NotificationType.JOB_ALERT
    )

    print(f"\n{bob.get_username()}'s inbox ({len(bob.get_inbox())} notifications):")
    for n in bob.get_inbox():
        print(f"  {n}")

    print(f"\n{alice.get_username()}'s inbox ({len(alice.get_inbox())} notifications):")
    for n in alice.get_inbox():
        print(f"  {n}")

    # =============================================
    # 7. Search Users
    # =============================================
    print("\n--- 7. Search Users ---")
    results = linkedin.search("alice")
    print(f"Search 'alice': {results}")

    results = linkedin.search("engineer")
    print(f"Search 'engineer': {results}")

    results = linkedin.search("charlie")
    print(f"Search 'charlie': {results}")

    results = linkedin.search("unknown")
    print(f"Search 'unknown': {results}")

    # =============================================
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()