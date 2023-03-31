"""Sample Organization models to use in the development environment.

These were intially designed to be used by the `script.reset_database` module."""

from ...models.organization import Organization

__authors__ = ["Kris Jordan, Jackson Davis, Antonio Tudela"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


org1 = Organization(id=1, #CS
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
                    description="Active Minds at Carolina is the UNC-Chapel Hill chapter of Active Minds. Our projects increase student' awareness of mental health conditions, provide information and resources regarding mental health and mental illness, encourage students to have conversations regarding their mental health, and serve as a liaison between students and the mental health community. Through campus-wide events, collaborations, and national programs, Active Minds at Carolina aims to fight against the stigma that surrounds mental health issues. We work to create a comfortable environment for open conversations on mental health to take place on the UNC-Chapel Hill campus. If you would like to get involved or have any questions regarding the club please contact one of our Co-Presidents. Please join our Slack if you are interested in being involved! This is our main platform of communication :)",
                    image="https://se-images.campuslabs.com/clink/images/074a951c-704c-4b35-9e81-f16da39f9f3ed291f0dd-d7c7-47c5-9ba9-e014a2a1dc04.jpg?preset=med-sq")

org4 = Organization(id=4,
                    name="(aCc) - a Culture club",
                    overview="Share, respect, and support all cultural identities.",
                    description="Our Mission: Share, respect, and support all cultural identities. Share: We hold Culture Shop and Festival Assembly for our members to share their cultural identities and knowledge in culture. Culture Shop offers an online platform to showcase cultures with pictures or videos or other materials on our organization's website. Members who have a culture or multiple cultures listed online will have the chance to show their cultures at Festival Assembly, which is held once per year. We will invite all UNC students to come to our Festival Assembly. Respect: We hold workshops for lectures and discussions. We will invite professors, graduate students, researchers, and other scholars in academia to educate us about culture. We will also invite other cultural organizations to talk about connections or differences among cultures together. Respecting each other's cultural identities is our priority. Support: We hold Culture Support Community and Culture Support Service to support both international students and endangered cultures. We will have an online community chat group for students to connect, and we will hold regular meetings for students to share their stories and support each other. As for Culture Support Service, we will offer a channel to encourage people worldwide to look for and collect endangered cultures. We will work together to discover how to commit to preserving global cultural identities and bring endangered cultures back.",
                    image="https://se-images.campuslabs.com/clink/images/78a6be92-aa7f-46d3-b731-c3f92da37039571a72b6-5e51-48e9-b8a4-74ae42ac858d.JPG?preset=small-sq")

org5 = Organization(id=5,
                    name="0 Degrees at UNC-CH",
                    overview="Join us, a fun social group that hosts events and fosters a welcoming environment!",
                    description="We aim to bring people who would not otherwise interact together to create long-lasting friendships and broaden their social networks by hosting events and creating a welcoming environment for all students. Feel free to join our discord server, where a lot of the communication is done: https://discord.gg/JnmUhS8X59",
                    image="https://se-images.campuslabs.com/clink/images/5907e905-93ef-44a3-916e-93c8c181db34777b1588-678d-44fa-bc0e-8853f8a79ede.png?preset=med-sq")

org6 = Organization(id=6,
                    name="1789",
                    overview="1789, powered by Innovate Carolina,  is free a co-working space and venture lab designed for students to take their idea to the next level, meet other student entrepreneurs, connect to resources and grow a team. ",
                    description="1789, powered by Innovate Carolina, is the University's central hub where innovation and entrepreneurship happen for all UNC students with an idea. Any UNC student is welcome to join.  1789 is free a co-working space and venture lab designed for students to take their idea to the next level, meet other student entrepreneurs, connect to resources and grow a team. With an open, flexible workspace conveniently located at 173 E. Franklin Street in the heart of downtown Chapel Hill, members may use the space for individual brainstorming, small meetings or larger events.  Innovate Carolina works to connect and support all students and programs on campus interested in innovation or entrepreneurship.  1789 members are not only connected to the Innovate Carolina network, but are also provided individualized support in starting their own ventures with access to workshops, classes, office hours and events in partnership with groups like Launch Chapel Hill, the Campus Y, the UNC Minor in Entrepreneurship, the Carolina Challenge and a plethora of other student organizations. ",
                    image="https://se-images.campuslabs.com/clink/images/13f76c3b-9504-46be-9b9a-0362c5ffb8d7f82aa3e6-2be6-4000-85f1-227422f703bc.jpg?preset=med-sq")

org7 = Organization(id=7,
                    name="180 Degrees Consulting UNC-Chapel Hill",
                    overview="Operating in over 100 branches around the world, 180 DC provides consulting services for nonprofits, social enterprises, and socially minded companies in an entirely student-led manner.",
                    description="", # this is left empty on purpose as the club has no desc :(
                    image="https://se-images.campuslabs.com/clink/images/5c8242e0-b2fd-4e75-bc35-384976b0b86cc9a6e5cb-bb57-4aba-9d83-e40139997863.png?preset=small-sq")                  

org8 = Organization(id=8,
                    name="BeAM",
                    overview="BeAM@CAROLINA is a network of makerspaces where any UNC student, staff, or faculty member can join the UNC maker community in the design and making of physical objects for education, research, entrepreneurship, and recreation.",
                    description="BeAM@CAROLINA is a network of makerspaces where any UNC student, staff, or faculty member can join the UNC maker community in the design and making of physical objects for education, research, entrepreneurship, and recreation. You can participate in open studios, training sessions, workshops, hosted classes and group activities. Enjoy spaces equipped with emerging technologies like 3D printing and laser cutting, along with areas dedicated to sewing and woodworking.",
                    image="https://se-images.campuslabs.com/clink/images/f04982cd-f95e-4fbf-807b-54e54860b75648c5a2fd-675c-4caf-98f7-7f34349b9504.jpg?preset=med-sq")

org9 = Organization(id=9, #CS
                    name="Women in Computer Science",
                    overview="A social, professional, and academic organization to empower women in computer science.",
                    description="Women in Computer Science provides a community for women in the field of computer science and additional fields involving programming. WICS is primarily concerned with facilitating a fun, welcoming, and engaging environment for its club members. We also provided opportunities via networking with partnered organizations and companies. Women in Computer Science also aims to hold multiple workshops and seminars geared towards breaking into and navigating the tech world.",
                    image="https://se-images.campuslabs.com/clink/images/a0a4f53b-5f5f-41c5-9abb-f76c398a16994fcb0c01-02b0-4525-bfc8-3a5c44640175.PNG?preset=med-sq")

org10 = Organization(id=10, #CS
                    name="Pearl Hacks",
                    overview="Pearl Hacks is an annual women & non-binary hackathon that empowers participants to pursue their interests in technology. ",
                    description="Pearl Hacks strives to empower women and non-binary groups in the field of computer science. We encourage our participants to learn and innovate using their coding skills, and we welcome first-time hackers by creating a collaborative environment for them to learn new skills. Additionally, we welcome a diverse group of minorities and remind them that they are amazing and needed in a field stereotypically dominated by men.",
                    image="https://se-images.campuslabs.com/clink/images/4f1a4ee2-315a-4001-98b8-bdaba68215a5dbf8cb84-0c1c-4e90-be8b-5c0273a9cac0.png?preset=med-sq")                   

org11 = Organization(id=11, #CS
                    name="Department of Computer Science",
                    overview="The Department of Computer Science offers instruction and performs research in the essential areas of computer science. ",
                    description="The Department of Computer Science offers instruction and performs research in the essential areas of computer science. Majors receive rigorous training in the foundations of computer science and the relevant mathematics, then have ample opportunity to specialize in advanced courses.",
                    image="") # empty as no image present

org12 = Organization(id=12, #CS
                    name="Black in Technology",
                    overview="Black in Technology (BiT) is a student and technology-based organization, that dedicates itself to the development of intensive programs for increasing Black and other ethnic participation in the field of technology and Computer Science.",
                    description="Black in Technology (BiT) is a student and technology-based organization, that dedicates itself to the development of intensive programs for increasing Black and other ethnic participation in the field of technology and Computer Science. BiT aims to increase the representation of Black students pursuing degrees in technology at the University of North Carolina at Chapel Hill. The primary mission of BiT is to voice the concerns of members and work to create an inclusive ecosystem for Black technology majors to thrive within the University.",
                    image="https://se-images.campuslabs.com/clink/images/01330403-6ba0-4da0-b227-90c588fd50441286457e-8bd4-4521-a6aa-56f63b99965f.png?preset=med-sq")

org13 = Organization(id=13, #CS
                    name="UNC-CH Game Development Club",
                    overview="This organization serves as a place for students learn and hone their game development skills. The club aims to publish one video game per year, ideally one per semester.",
                    description="The mission of UNC-CH Game Development Club is to provide a space for anyone interested in learning how to develop video games, whether they have no experience in it whatsoever or are already seasoned game developers. The club is open to anyone that can contribute in the video game development process whether they are interested in programming, 3D modeling, character design, storyboarding, music, creative writing, or any other related creative processes. The club also seeks to encourage students not studying computer science to join because game development requires more than just programmers to create a game. Game development is most often associated with computer programming, but it actually requires a much more diverse group of individuals skilled in different creative disciplines. UNC-CH Game Development Club seeks to foster this type of environment and be open to anyone that wishes to learn about this collective creative process. Join our club Discord server here to stay up to date! https://discord.gg/bMHxVPk",
                    image="https://se-images.campuslabs.com/clink/images/2bde173d-c6d6-4a50-a2ba-11f89c7dd695eef4e7ba-3561-4f07-8724-9dc19d1595b2.png?preset=med-sq")

org14 = Organization(id=14, #CS
                    name="Cybersecurity CTF Club",
                    overview="UNC-CH's hands-on computer security club, developing practical technical abilities in students and members of the local enthusiast community through lecture, workshops, and participation in competition against teams of practitioners across the world.",
                    description="We primarily communicate through discord, invite link at https://discord.gg/GSdrVQ7. UNC-CH's hands-on computer security club, developing practical technical abilities in students and members of the local enthusiast community through lecture, workshops, and participation in competition against teams of practitioners across the world. CTF stands for Capture The Flag, a form of competitive computer security competition with a typical focus in offensive or defensive operations, or solving a wide array of challenges in a variety of categories. We regularly practice skills in reverse engineering, system exploitation, web app auditing, forensics, and cryptography. We meet on a weekly basis. Check website for updates. If you would like to join our club and come to meetings, please email ntropy.unc@gmail.com. Membership on heellife does not mean that you will get notifications or are automatically signed up to our list-serve.",
                    image="https://se-images.campuslabs.com/clink/images/b7015dec-588a-478f-9813-b0d6ef694eaa48fdeded-7fd8-4170-b5b6-aa17b0dd7fd2.png?preset=med-sq")

org15 = Organization(id=15, #CS
                    name="CS+Social Good at UNC-Chapel Hill",
                    overview="CS+Social Good aims to inspire action towards thoughtful uses of technology though discussions, projects, and more. We partner with local nonprofits and organizations to create tech solutions that elevate their impact.",
                    description="Through technology, we have the opportunity to be a part of the positive change and evolution of a growing world of possibility. We aim to give nonprofits and organizations for social good in the Chapel Hill area the tools to effectively complete their goals with the use of knowledge and programs. We partner with 2-3 organizations per semester and develop custom technology solutions for their needs. These groups include 501(c) organizations, student groups, and Ph.D. candidates.",
                    image="https://se-images.campuslabs.com/clink/images/9bb27e74-fd00-4c7a-92bf-feb32e1d0aebaad4b06d-ea9b-454b-aee3-de5943ae2613.png?preset=med-sq")



#This is pretty ugly, would be better to use a loop... but like laterrr
models = [
    org1,
    org2,
    org3,
    org4,
    org5,
    org6,
    org7,
    org8,
    org9,
    org10,
    org11,
    org12,
    org13,
    org14,
    org15
]
