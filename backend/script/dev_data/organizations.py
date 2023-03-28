"""Sample Organization models to use in the development environment.

These were intially designed to be used by the `script.reset_database` module."""

from ...models.organization import Organization

__authors__ = ["Kris Jordan, Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


org1 = Organization(id=1, 
                    name="ACM at Carolina", 
                    overview="ACM at Carolina is dedicated to helping encourage students find their passion in the computer science world and build a strong community of students, faculty, and professionals at Chapel Hill. Feel free to check out our page!", 
                    description="Mission Statement: ""We are a professional community of Tar Heels who study computing; we are dedicated to exploring our field, defining our interests, engaging with each other, discovering our strengths, and improving our skills."" If you are interested in joining, please visit this link: https://bit.ly/ACM-Sign-Up. Also, make sure to contact us with any questions!",
                    image="https://se-images.campuslabs.com/clink/images/b8ab1d8e-ee34-449f-ae5f-e843896455c704688f5b-d1b0-411e-9f69-14c063114d55.jpg?preset=med-sq")

org2 = Organization(id=2, 
                name="Ackland Art Museum", 
                overview="The Ackland Art Museum features a collection of over 19,000 artworks and rotating exhibitions throughout the year. Admission to the Museum is free for all. A vibrant schedule of events and opportunities for students to get involved are available.", 
                description="The Ackland Art Museum, located on S. Columbia Street near Franklin St., features a permanent collection of over 20,000 works of art. Rotating special exhibitions feature a wide range of art: from sound and video installations to early modern prints and photographs, from 19th-century French paintings to contemporary Japanese ceramics. Ackland Upstairs is the Museum’s second floor gallery where they display art selected by UNC-Chapel Hill faculty members to complement the courses they teach. It’s likely you will have a class at the Ackland during your time at Carolina! The Ackland also offers a vibrant year-round schedule of free and low-cost public programs featuring live music, ﬁlms, hands-on art making classes, gallery tours, and evening and weekend activities. Their ART& community space is food & beverage friendly and makes a great study spot. The Ackland offers a variety of opportunities for students to engage with the Museum, including the Ackland Student Guide program and internships. In addition, student memberships to the Museum are free for UNC undergraduate and graduate students and offer benefits including 10'%' off at the Museum Store. Sign up for FREE Ackland Student Membership. To stay connected, follow the Ackland on social media and sign up for our e-news! https://www.youtube.com/watch?v=0H1nKdxZp-E&t=2s",
               image="https://se-images.campuslabs.com/clink/images/ee0bc303-002e-4aca-aaba-81ad270d3901c0ac95ac-7e47-4ee6-95bf-c6f9598dd2fd.jpg?preset=med-sq")

org3 = Organization(id=3, 
                name="Active Minds at Carolina", 
                overview="Active Minds at Carolina seeks to foster a community of mindful and dedicated students who are committed to a world in which individuals can seek help for mental health issues without fear of stigma or lack of access.", 
                description="Active Minds at Carolina is the UNC-Chapel Hill chapter of Active Minds. Our projects increase students’ awareness of mental health conditions, provide information and resources regarding mental health and mental illness, encourage students to have conversations regarding their mental health, and serve as a liaison between students and the mental health community. Through campus-wide events, collaborations, and national programs, Active Minds at Carolina aims to fight against the stigma that surrounds mental health issues. We work to create a comfortable environment for open conversations on mental health to take place on the UNC-Chapel Hill campus. If you would like to get involved or have any questions regarding the club please contact one of our Co-Presidents. Please join our Slack if you are interested in being involved! This is our main platform of communication :)",
               image="https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq")


models = [
    org1,
    org2,
    org3
]
