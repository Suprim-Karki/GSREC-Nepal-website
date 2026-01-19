from django.core.management.base import BaseCommand
from core.models import HeroSection, Country, Service, TestPrep, Testimonial, Partner, Feature, Stat, Milestone

class Command(BaseCommand):
    help = 'Load initial data from React app constants'

    def handle(self, *args, **kwargs):
        self.stdout.write("Loading initial data...")

        # Hero
        if not HeroSection.objects.exists():
            HeroSection.objects.create(
                title_part1="Dream Big.",
                title_part2="Study Global.",
                subtitle="Your bridge to the world's best universities. We provide end-to-end guidance for students aspiring to study abroad in UK, USA, Australia, Canada, and beyond.",
                is_active=True
            )
            self.stdout.write("Created Hero Section")

        # Features (Why Choose Us)
        features_data = [
            {"title": "High Visa Success", "text": "Our dedicated visa team meticulously reviews your documents.", "icon_class": "fa-file-circle-check", "order": 1},
            {"title": "Scholarship Support", "text": "We have helped students secure over $5 Million in scholarships.", "icon_class": "fa-hand-holding-dollar", "order": 2},
            {"title": "Post-Landing Support", "text": "From accommodation to airport pickups, we are with you.", "icon_class": "fa-house-chimney", "order": 3}
        ]
        for f_data in features_data:
            Feature.objects.get_or_create(title=f_data['title'], defaults=f_data)
        self.stdout.write(f"Loaded {len(features_data)} features")

        # Stats
        stats_data = [
             {"num": "12+", "label": "Years Experience", "order": 1},
             {"num": "5k+", "label": "Students Placed", "order": 2},
             {"num": "98%", "label": "Visa Success", "order": 3},
             {"num": "50+", "label": "University Partners", "order": 4}
        ]
        for s_data in stats_data:
            Stat.objects.get_or_create(label=s_data['label'], defaults={'number': s_data['num'], 'order': s_data['order']})
        self.stdout.write(f"Loaded {len(stats_data)} stats")

        # Countries
        countries_data = [
            {
                "name": "Europe",
                "intro": "Europe offers a unique blend of history, culture, and innovation. With a single Schengen visa, students can explore 27+ countries while receiving world-class education.",
                "facts": ["Schengen Visa Travel", "Low/No Tuition in many regions", "Diverse Cultural Exposure", "Erasmus+ Exchange Opportunities"],
                "universities": ["ETH Zurich", "TU Munich", "Sorbonne University", "University of Amsterdam"],
                "flag_emoji": "🇪🇺",
                "order": 1
            },
            {
                "name": "United Kingdom",
                "intro": "The United Kingdom stands as a beacon of academic excellence, home to some of the world's oldest and most prestigious universities. Shorter masters programs allow faster workforce entry.",
                "facts": ["2-Year Post Study Work Visa", "1-Year Masters Programs", "World-class Research Facilities", "Home to 4 of Top 10 World Universities"],
                "universities": ["University of Oxford", "Imperial College London", "University of Edinburgh", "Manchester University"],
                "flag_emoji": "🇬🇧",
                "order": 2
            },
            {
                "name": "United States",
                "intro": "The USA hosts the highest number of international students worldwide, offering unmatched flexibility in course choices, vast research funds, and cutting-edge technology.",
                "facts": ["STEM OPT up to 3 Years", "Merit-based Scholarships", "Flexible Curriculum (Major/Minor)", "Global Career & Networking"],
                "universities": ["MIT", "Stanford University", "Harvard University", "UCLA"],
                "flag_emoji": "🇺🇸",
                "order": 3
            },
            {
                "name": "Australia",
                "intro": "Known for its high quality of life and globally recognized qualifications. The Group of Eight (Go8) universities consistently rank among the world's best.",
                "facts": ["Post-Study Work Rights up to 4-6 Years", "High Minimum Wage", "Multicultural Society", "Excellent Student Support Services"],
                "universities": ["University of Melbourne", "University of Sydney", "ANU", "UNSW"],
                "flag_emoji": "🇦🇺",
                "order": 4
            },
             {
                "name": "Canada",
                "intro": "Canada is renowned for its welcoming attitude towards immigrants and high academic standards. It offers clear pathways to permanent residency.",
                "facts": ["Clear PR Pathways", "Co-op & Internship Programs", "Affordable Tuition & Living", "Safe, Inclusive Environment"],
                "universities": ["University of Toronto", "McGill University", "UBC", "University of Alberta"],
                "flag_emoji": "🇨🇦",
                "order": 5
            },
             {
                "name": "New Zealand",
                "intro": "Experience world-class education in one of the most scenic and peaceful countries on earth. New Zealand's education system focuses on practical, hands-on learning.",
                "facts": ["3-Year Post Study Work Visa", "Safe & Peaceful Environment", "Innovative Teaching Methods", "Research & PhD Opportunities"],
                "universities": ["University of Auckland", "University of Otago", "Victoria University", "Massey University"],
                "flag_emoji": "🇳🇿",
                "order": 6
            }
        ]

        for c_data in countries_data:
            Country.objects.get_or_create(name=c_data['name'], defaults=c_data)
        self.stdout.write(f"Loaded {len(countries_data)} countries")

        # Services
        services_data = [
            {
                "title": "Career Counseling",
                "icon_class": "fa-compass",
                "intro": "Confused about which course or country to choose? Our certified counselors provide in-depth career counseling to help you make informed decisions based on your academic profile, financial background, and long-term career goals.",
                "features": ["In-depth Profile Evaluation", "Course & University Selection", "Country Comparison & Analysis", "Long-term Career Roadmap"],
                "process": "We start with a detailed profile assessment, followed by 1-on-1 sessions to understand your aspirations.",
                "order": 1
            },
            {
                "title": "University Admissions",
                "icon_class": "fa-university",
                "intro": "We streamline the complex application process, ensuring your application stands out. From crafting compelling SOPs to managing timelines, our team handles the heavy lifting.",
                "features": ["SOP/LOR Editing & Refinement", "Application Strategy & Timeline", "Interview Preparation", "Offer Letter & Acceptance Management"],
                "process": "Our team reviews every document, ensures error-free application forms, and communicates with universities on your behalf.",
                "order": 2
            },
             {
                "title": "Visa Assistance",
                "icon_class": "fa-passport",
                "intro": "Our experts guide you through the entire documentation and financial requirements to maximize your success rate. We stay updated with the latest immigration policies.",
                "features": ["Comprehensive Document Checklist", "Financial Proof Guidance", "Mock Visa Interviews", "Form Filing & Slot Booking"],
                "process": "We conduct rigorous mock interviews to boost your confidence and meticulously verify every financial document.",
                "order": 3
            },
             {
                "title": "Scholarship Guidance",
                "icon_class": "fa-certificate",
                "intro": "We help meritorious students secure scholarships ranging from partial funding to 100% tuition waivers. Our team tracks deadlines for thousands of scholarship programs globally.",
                "features": ["Merit-based Assessment", "Essay Writing Support", "University Specific Grants", "Government Aid Applications"],
                "process": "We analyze your academic achievements and assist in crafting compelling scholarship essays.",
                "order": 4
            },
            {
                "title": "Forex & Accommodation",
                "icon_class": "fa-money-bill-transfer",
                "intro": "We assist with currency exchange at competitive rates, education loan assistance, and finding secure accommodation near your university.",
                "features": ["Best Exchange Rates", "Education Loan Support", "On/Off-campus Housing", "Travel Insurance"],
                "process": "We connect you with trusted forex partners and housing providers, ensuring your transition is smooth and safe.",
                "order": 5
            },
            {
                "title": "Pre-departure Support",
                "icon_class": "fa-plane-departure",
                "intro": "Our pre-departure briefings cover everything from packing lists and airport immigration to culture shock and networking tips.",
                "features": ["Packing Checklist", "Immigration Procedures", "Alumni Networking", "Cultural Etiquette"],
                "process": "Attend our detailed briefing sessions where we connect you with students already studying at your destination.",
                "order": 6
            }
        ]

        for s_data in services_data:
            Service.objects.get_or_create(title=s_data['title'], defaults=s_data)
        self.stdout.write(f"Loaded {len(services_data)} services")

        # Test Prep
        test_data = [
            {
                "name": "IELTS",
                "full_name": "International English Language Testing System",
                "icon_class": "fa-comments",
                "intro": "The IELTS is the world's most popular English language proficiency test. It uses a 9-band scale to clearly identify levels of proficiency. We offer comprehensive training for both Academic and General Training modules.",
                "format_data": [
                    {"section": "Listening", "duration": "30 mins", "description": "Four recordings of native English speakers."},
                    {"section": "Reading", "duration": "60 mins", "description": "40 questions testing reading skills."},
                    {"section": "Writing", "duration": "60 mins", "description": "Task 1 (Graph/Letter) and Task 2 (Essay)."},
                    {"section": "Speaking", "duration": "11-14 mins", "description": "Face-to-face interview with an examiner."}
                ],
                "score_scale": "Scale of 1-9 (Bands)",
                "validity": "2 Years",
                "order": 1
            },
             {
                "name": "PTE",
                "full_name": "Pearson Test of English",
                "icon_class": "fa-headset",
                "intro": "PTE Academic is a fully computer-based academic English language test. One of its key advantages is the speed of results, often available within 48 hours.",
                "format_data": [
                    {"section": "Speaking & Writing", "duration": "54-67 mins", "description": "Personal introduction, read aloud, repeat sentence, essay."},
                    {"section": "Reading", "duration": "29-30 mins", "description": "Fill-in-the-blanks, multiple choice, re-order paragraphs."},
                    {"section": "Listening", "duration": "30-43 mins", "description": "Summarize spoken text, dictation, multiple choice."}
                ],
                "score_scale": "Scale of 10-90",
                "validity": "2 Years",
                "order": 2
            },
             {
                "name": "TOEFL",
                "full_name": "Test of English as a Foreign Language",
                "icon_class": "fa-book-open",
                "intro": "TOEFL iBT measures the English language ability of non-native speakers wishing to enroll in English-speaking universities.",
                "format_data": [
                    {"section": "Reading", "duration": "54-72 mins", "description": "3-4 passages from academic texts."},
                    {"section": "Listening", "duration": "41-57 mins", "description": "Listening to lectures and conversations."},
                    {"section": "Speaking", "duration": "17 mins", "description": "Express an opinion on a familiar topic."},
                    {"section": "Writing", "duration": "50 mins", "description": "Write essay responses based on reading/listening."}
                ],
                "score_scale": "Scale of 0-120",
                "validity": "2 Years",
                "order": 3
            },
             {
                "name": "SAT",
                "full_name": "Scholastic Assessment Test",
                "icon_class": "fa-pen-nib",
                "intro": "The SAT is an entrance exam used by most US colleges. The new Digital SAT is shorter and adaptive.",
                "format_data": [
                    {"section": "Reading & Writing", "duration": "64 mins", "description": "Two modules. Covers craft, structure, and ideas."},
                    {"section": "Math", "duration": "70 mins", "description": "Two modules. Covers algebra, advanced math, geometry."}
                ],
                "score_scale": "Scale of 400-1600",
                "validity": "5 Years",
                "order": 4
            },
        ]
        
        for t_data in test_data:
            TestPrep.objects.get_or_create(name=t_data['name'], defaults=t_data)
        self.stdout.write(f"Loaded {len(test_data)} test preps")

        # Testimonials
        testimonials_data = [
          { "name": "Sarah Jenkins", "university": "University of Oxford", "quote": "GSREC made my dream of studying at Oxford a reality. Their SOP editing was a game-changer." },
          { "name": "Michael Chen", "university": "University of Toronto", "quote": "I was worried about my visa, but the team guided me through every document. Got my approval in 2 weeks!" },
          { "name": "Priya Patel", "university": "University of Melbourne", "quote": "The career counseling session gave me clarity on which course to pick. Best decision ever." },
          { "name": "David Kim", "university": "Stanford University", "quote": "From SAT prep to final admission, GSREC was with me at every step. Highly recommended!" },
          { "name": "Emma Wilson", "university": "ETH Zurich", "quote": "Applying to Europe can be tricky, but their destination experts made it seamless." },
          { "name": "Rajesh Kumar", "university": "TU Munich", "quote": "Secured a full scholarship thanks to their guidance on profile building. Forever grateful." }
        ]
        
        for test in testimonials_data:
             Testimonial.objects.get_or_create(name=test['name'], defaults=test)
        self.stdout.write(f"Loaded {len(testimonials_data)} testimonials")

        # Partners
        partners_data = [
            {"name": "University of Oxford", "website": "https://www.ox.ac.uk"},
            {"name": "Stanford University", "website": "https://www.stanford.edu"},
            {"name": "Harvard University", "website": "https://www.harvard.edu"},
            {"name": "University of Toronto", "website": "https://www.utoronto.ca"},
            {"name": "University of Melbourne", "website": "https://www.unimelb.edu.au"},
        ]
        for p_data in partners_data:
            Partner.objects.get_or_create(name=p_data['name'], defaults=p_data)
        self.stdout.write(f"Loaded {len(partners_data)} partners")
        
        # Milestones
        milestones_data = [
            {"year": "2010", "title": "Inception", "description": "Founded with a vision to streamline study abroad processing."},
            {"year": "2015", "title": "Expansion", "description": "Opened 3 new branches across Nepal and partnered with 50+ universities."},
            {"year": "2018", "title": "Award Winning", "description": "Recognized as 'Best Education Consultancy' by National Education Board."},
            {"year": "2023", "title": "Global Reach", "description": "Successfully placed over 5000 students in top global universities."},
        ]
        for m_data in milestones_data:
            Milestone.objects.get_or_create(year=m_data['year'], defaults=m_data)
        self.stdout.write(f"Loaded {len(milestones_data)} milestones")

        self.stdout.write(self.style.SUCCESS('Successfully loaded all initial data'))
