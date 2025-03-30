import openai
import os
import asyncio
from agents import Agent, Runner, WebSearchTool, trace


async def web_search(job_title, employer):
    query = f"latest news about {job_title} at {employer}"
    agent = Agent(
        name="Web Searcher",
        instructions="You are a helpful agent.",
        model="gpt-4o-mini",
        tools=[WebSearchTool(user_location={"type": "approximate", "city": "Norfolk Virginia"})],
    )
    with trace("Web search example"):
        result = await Runner.run(
            agent, query
        )
    return result.final_output


async def generate_interview_question(job_title, employer):
    # Create an interview question based on the job title and employer.
    context = f"Generate a concise interview question for a {job_title} position at {employer}. Customize it based on {resume}"
    agent = Agent(
        name="Interview Question Generator",
        instructions="You are a helpful assistant generating one concise interview question.",
        model="gpt-4o-mini",
        tools=[],
    )
    with trace("Interview question generation"):
        result = await Runner.run(
            agent, context
        )
    return result.final_output


async def evaluate_answer(answer, job_title, employer):
    # Evaluate the user's answer and provide feedback.
    context = f"Provide feedback on the following answer for a {job_title} position at {employer}, considering {resume}: {answer}"
    agent = Agent(
        name="Answer Evaluator",
        instructions="You are an evaluator providing one sentence of positive feedback and one sentence of constructive feedback to each interview answer. Do not provide resume feedback. Keep it concise.",
        model="gpt-4o-mini",
        tools=[],
    )
    with trace("Answer evaluation"):
        result = await Runner.run(
            agent, context
        )
    return result.final_output


async def interview_session(job_title, employer):
    while True:
        question = await generate_interview_question(job_title, employer)
        print(f"Interview Question: {question}")

        user_answer = input("Your Answer: ")
        if user_answer.lower() == 'exit':
            break

        feedback = await evaluate_answer(user_answer, job_title, employer)
        print(f"Feedback: {feedback}")


if __name__ == "__main__":
    print("Hello Catherine! Welcome to your custom Interview Coach!")
    #job_title = input("Enter the job title you're preparing for: ")
    #employer = input("Enter the employer's name: ")
    job_title = "Vice president of operations"
    employer = "First Health, Moore Hospital, Pinehurst North Carolina"
    resume = '''Catherine Hughes
SUMMARY
Passionate and engaged leader with a focus on relationships, collaboration and consensus building, with a commitment to excellence; seasoned, creative, and outcome driven operational leader with proven track record leading successful teams, developing and implementing strategic plans for organizational quality improvement, service line growth, employee engagement and morale; experience in physician and service contract negotiations, reduction of financial costs, and complex technology implementations; active community business leader.
"
PROFESSIONAL EXPERIENCE AND CAREER HISTORY

March 2022-Present 
Vice President of Hospital Operations, Sentara RMH
Reporting to the President of Sentara RMH with responsibility for leading the day-to-day operations of a 238 licensed bed, Magnet designated, Top 100 ranked (2021), complex care medical center serving a seven-county region with over 200,000 residents and annual net revenues of $570 million; an affiliate of Sentara Health, an integrated, 12-hospital system with facilities located in Virginia and North Carolina with over 35,000 employees and 2,000 providers that is currently ranked as one of the nation’s Top 15 health systems. Sentara Health Plans serves over 1 million members in Virginia and Florida.

Clinical Services: Surgical Services, Oncology, Orthopedic, Heart and Vascular (including Cardiothoracic Surgery), Hospitalist, OB Hospitalist, Neonatology, Sleep Lab, Rehabilitation, Wound Care, and Imaging.

Operational Services: Facilities, Emergency Preparedness, Biomed, Construction, Security, Nutritional Services, Environmental Services, Guest Services, and RMH Wellness Center. 

Division liaison for Pharmacy, Lab, Supply Chain with local operational oversight.  

Initiated staff led committees to craft and execute improvement plans for Employee and Patient Satisfaction resulting in a three-year trend of improvement (Emp Satisfaction rose from 23rd%ile to 67th, HCAHPS rate hospital increased 8.15% points to 73.1%- 56th%ile).
Formulated a multipronged recruitment strategy with CNO and Foundation, including partnerships with local nursing schools to reduce vacancy rates and eliminate 7M in travel staff. All jobs turnover decreased to 14.2% (national average 17.2%) and RN turnover has led the Sentara system for three years at 7.5% (national average 15%).
Weekly collaboration with Ambulatory, Medical Group, and Health Plan scheduling and authorization leaders to increase market share, grow procedural volumes, and improve documentation which drove an 8.6% increase in annual gross patient service to 1.5B in 2024.
Partnered with pharmacy to implement 340B at SRMH which led to 9.2M in savings in 2024.  Plans to expand the program within our region for additional savings.
Executive Sponsor of system-wide high performance teams- Emergency Medicine, Sepsis Mortality, Surgical Services, Patient Satisfaction, Workplace Violence, and Sustainability.  
Trusted partner of the CNO and CMO; member of Quality Management System Committee overseeing division Clinical Performance Index which has seen a three-year improvement trend on metrics including LOS (4.03/0.81 ratio), HAI’s (8 total in 2024), Emergency Dept Treatment Time (186 minutes), Mortality ratios (0.87) and Readmission rates (12.3%).
Member of the Perioperative Executive Committee which has improved OR efficiency metrics including First Case on Time Starts (80%), Room Turnover (26 min), and reduction of same day cancellations through a PASS Clinic (3.5%). 
Lead successful contract negotiations- to include the expansion of an independent radiation oncology provider group to cover both SRMH and SMJH hospital divisions, reduced Healogics Wound Care contract fees by 10%, created recruitment assistance and stipend package for independent urology practice, and led RFP process for Morrison Foodservice contract cost reduction.
Oversee space planning, construction, and division real estate portfolio in order to maximize revenue generating space, operational efficiencies, and maintain regulatory requirements.

September 2013-March 2022               
Executive Director/Director of Patient Care Services, Sentara Martha Jefferson Hospital
Reported to the Chief Operating Officer/Interim President with responsibility for oversight of daily operations of a 176 licensed bed community hospital serving 8 counties with 10,000 annual admissions, annual revenues in excess of $350M and 1,200 team members:

Clinical Services: Outpatient Surgical Services, Interim Inpatient Surgical Services, Advanced Gastroenterology/Digestive Health, Rehabilitation, Imaging, Wound Care, Senior Services.

Operational Services: Customer Satisfaction, Grievance and Patient Advocacy, Facilities, Construction, Nutritional Services, Environmental Services, Security, Guest Services, and Administrative liaison for Supply Chain and Biomed.  

Demonstrated year over year service line growth since 2016 in Advanced Gastroenterology, resulting in regional capture of patients and successful recruitment of a second provider.
Effectively implemented a financial improvement plan at the Outpatient Surgery Center to reverse profit loss to profit gain, coordinated efforts with Main OR to increase ASC OR utilization to over 90%, fostered improvement in physician relationships and recruited surgeons from a competing surgery center. Participated in anesthesia contract transition and expansion plan. 
Strategic oversight of Medical Imaging service line with over 100,000 annual exams in a very competitive market. Participated in Ivy Venture consultation to increase market share and net revenue.  Partnered with radiologists and team for a PACS upgrade, serving as the internal beta site to work through implementation challenges. 
Following the acquisition close, facilitated the transition of staff and services of our Outpatient Rehab department to our joint venture company Physical Therapy at ACAC (PT@ACAC).
Partnered with the Director of Finance in creation of department budgets, capital planning and prioritization, cost reduction action plans. Productivity YTD 105% through targeted action planning with underperforming departments. 
Key leader for local recruitment, retention, employee engagement and succession plan efforts. Lead the Employee Recognition Team planning staff engagement events.  Charter member of the Diversity and Inclusion Team. Coordinator for Annual Leadership Educational Retreats.  Serve as the facilitator for Director Quarterly Meeting and Manager/Team Coordinator Lunch and Learn series.  
Collaborated with Nursing Leaders for data driven action planning for our Customer Experience programs and four consecutive Magnet designations.  Led the system in Inpatient HCAHPS Scores.
Chaired the division Grievance Committee.  Launched the Patient Family Advisory Council in 2012, and developed an annual grant program in 2016 for staff to request Foundation funds for programs or resources aimed to improve employee and patient satisfaction.
Partnered with the Foundation to conceive and implement a Family Caregiver Program (a Sentara first), Senior RN Navigator, and Clinical Career Pathways scholarships. 
Administrative leader with oversight for Facilities Master Plan, lease management, and construction projects including COPN approval.
System responsibilities included: Operational lead for Morrison’s contract, system review of Wound Care contract and dashboard development, member of Behavioral Health HPT, Clinical Engineering Workgroup, Workplace Violence Prevention, Patient Experience Workgroup, and Workday Test User Group.  
Ensured compliance with regulatory requirements for various local, state and federal accreditations.

September 2010-August 2013         
Director Food Service, Retail and Patient Transport, Sentara Martha Jefferson Hospital
Oversight of 3 departments, 6 locations, 75 employees, 30 volunteers and a $3 million budget.
Implemented a centralized Patient Transportation department incorporating TeleTracker software.
Chaired and participated on multiple transition teams for the Replacement Hospital project.
Oriented and trained over 100 employees and volunteers to new facility layout and processes.
Led a task force related to enhancing and improving the organizations Patient Experience, Value Based Purchasing and HCAHPS scores. 
"
"
July 2005-August 2010       
Manager, Food and Nutrition Services and Retail Services, Martha Jefferson Hospital
Managed labor and supply budget over $2 million with 48 employees.
Provided Clinical Nutrition Support to Inpatients and serve on Nutrition Support Committee.
Implemented new technology applications- Computrition, Point of Sale, Payroll Deduction.
Redeployed hospital Gift Shop to incorporate Outpatient Healthcare Retail.
Acquired and incorporated both a Cancer Care and Lactation business into main Gift Shop.


March 2004- June 2005
Supervisor, Food and Nutrition Services Department, Martha Jefferson Hospital      

AWARDS AND RECOGNITION
Sentara CEO Award for Patient Satisfaction in 2012
Sentara Martha Jefferson President’s Award in 2013
Sentara Top Hat Award for Transformational Work in 2023"
 
EDUCATION
"Advisory Board Executive Leadership Fellowship
Walden University- Master of Business Administration- Strategic Planning and Marketing 
University of Delaware, Newark, DE- Dietetic Internship 
Johnson & Wales University, Providence, RI- Bachelor of Science in Culinary Nutrition Arts 
"
"
PROFESSIONAL AFFILIATIONS AND COMMUNITY INVOLVEMENT 

Current 

Fellow of the American College of Healthcare Executives (FACHE)
Blue Ridge Community College Educational Foundation Board 
United Way of Harrisonburg, Board Member and Governance Committee
Sentara United Way Campaign Chair 
Past 
Virginia Hospital & Healthcare Association Patient Satisfaction Advisory Committee
Executive Committee, United Way Charlottesville
Chair of Financial Stability and Community Health Committees, United Way Charlottesville
Executive Committee and Secretary, Albemarle County Police Foundation Board
President Blue Ridge Dietetic Association 

References Available Upon Request '''

    asyncio.run(interview_session(job_title, employer))
