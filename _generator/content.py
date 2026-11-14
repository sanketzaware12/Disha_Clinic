# -*- coding: utf-8 -*-
# ALL SITE DATA LIVES HERE. Edit values, then run:  python build.py
# [REPLACE] = temporary dummy content to be replaced with client content.

C = dict(
    name="DISHA Advanced Surgical & Laser Piles Clinic",            # [REPLACE] hospital name
    short="Disha",
    tagline="Compassionate Surgical Care, Start to Finish",  # [REPLACE]
    owner="Dr. Abhijeet Suresh Shinde",                  # [REPLACE]
    doctor="Dr. Abhijeet Suresh Shinde",
    quals="MBBS, MS (General Surgery), FMAS",
    est="2012",
    address="2nd Floor, Lotus Plaza, College Road, Pune, Maharashtra 422005",  # [REPLACE]
    city="Pune",
    areas="Pune, Sinnar, Igatpuri, Dindori, Malegaon",
    phone="+91 98765 43210", phone_tel="+919876543210",
    whatsapp="919876543210",
    appt="+91 98765 43210", appt_tel="+919876543210",
    emergency="+91 98765 43211", emergency_tel="+919876543211",
    email="info@dishaclinic.example",
    hours="Mon – Sat: 9:00 AM – 8:00 PM",
    hours2="Sunday: OPD closed · Emergency 24×7",
    base="https://www.dishaclinic.example",   # [REPLACE] live domain (used in sitemap/canonical)
    map_embed="https://www.google.com/maps?q=College+Road+Pune&output=embed",
    map_link="https://www.google.com/maps/search/?api=1&query=College+Road+Pune",
    social={"Instagram": "#", "Facebook": "#", "LinkedIn": "#", "YouTube": "#"},
    slots=["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM"],
    closed_days=[0],  # 0 = Sunday
    link_index=True,  # True: links end with index.html (works by double-click). False before live deploy (clean URLs).
    gsc="<!-- [REPLACE] Google Search Console verification: <meta name=\"google-site-verification\" content=\"XXXX\"> -->",
    ga="<!-- [REPLACE] Google Analytics / GTM snippet here -->",
)

# slug, name, icon, short(20-25w), intro, full(100-150w), features, faqs, keywords(primary, secondary...)
SERVICES = [
 ("laparoscopic-surgery", "Laparoscopic (Keyhole) Surgery", "pulse",
  "Minimally invasive keyhole procedures performed through tiny incisions, offering less pain, minimal scarring and a faster return to your normal routine.",
  "Laparoscopic surgery uses a small camera and fine instruments inserted through tiny cuts. It allows our surgeons to treat many abdominal conditions with greater precision and less trauma to the body.",
  "Laparoscopic surgery, also known as keyhole surgery, is performed through incisions of only a few millimetres. A high-definition camera projects a magnified view of the abdomen onto a monitor, helping the surgeon operate with exceptional precision. Compared with open surgery, patients usually experience less pain, a lower risk of wound infection, minimal scarring and a shorter hospital stay. At our clinic, laparoscopic techniques are used for gallbladder, hernia, appendix and selected bowel conditions. Every case is assessed individually, and your surgeon will explain clearly whether a keyhole approach is the safest option for you or whether open surgery is better suited. Our modern operation theatres and experienced team ensure your procedure is carried out to the highest standards of safety and hygiene.",
  ["Tiny incisions and minimal scarring", "Less post-operative pain", "Shorter hospital stay", "Faster return to work and routine", "Lower risk of wound infection"],
  [("Is laparoscopic surgery safe?", "Yes. When performed by an experienced surgeon in a well-equipped theatre, it is a well-established and safe approach. Your surgeon will explain the benefits and risks for your case."),
   ("How long will I stay in the hospital?", "Most keyhole procedures need a stay of one to two days, depending on the surgery and your general health."),
   ("Can every surgery be done by keyhole?", "No. Some situations, such as dense adhesions or certain emergencies, are safer with open surgery. Your surgeon recommends the approach that fits you best.")],
  ["laparoscopic surgeon in Pune", "keyhole surgery Pune", "laparoscopic surgery hospital", "minimally invasive surgery"]),
 ("gallbladder-stone-surgery", "Gallbladder Stone Surgery", "heart",
  "Safe laparoscopic gallbladder removal for painful gallstones, with a clear treatment plan, quick recovery and compassionate support throughout your care.",
  "Gallstones can cause repeated pain, nausea and serious complications if ignored. We offer keyhole gallbladder removal with careful assessment before and attentive follow-up after surgery.",
  "Gallstones are hardened deposits that form in the gallbladder and can cause sharp pain in the upper right abdomen, nausea and indigestion, especially after fatty meals. When symptoms keep returning or complications develop, removing the gallbladder is the most reliable solution. Our surgeons perform laparoscopic cholecystectomy through small incisions, allowing most patients to walk within hours and return home the next day. Before surgery, we review your ultrasound and blood reports, discuss anaesthesia and answer every question you have. After the operation, you receive simple diet and wound-care guidance along with scheduled follow-up visits. You can live a completely normal life without a gallbladder, and our team stays available to support your recovery at every step.",
  ["Keyhole gallbladder removal", "Walk within hours of surgery", "Usually one-night hospital stay", "Clear diet and recovery guidance", "Follow-up visits included in care plan"],
  [("Do all gallstones need surgery?", "Not always. Stones that cause no symptoms can often be observed. Surgery is advised when pain, infection or other complications occur."),
   ("Can I live normally without a gallbladder?", "Yes. The liver continues to produce bile, and most people eat a normal diet after a short adjustment period."),
   ("When can I return to work?", "Most patients resume light work within one week, depending on the type of job and recovery.")],
  ["gallbladder stone surgery in Pune", "gallstone removal", "laparoscopic cholecystectomy", "gallbladder pain treatment"]),
 ("hernia-repair-surgery", "Hernia Repair Surgery", "shield",
  "Mesh-based hernia repair using open or laparoscopic techniques, selected for your hernia type, age and lifestyle to reduce the chance of recurrence.",
  "A hernia will not heal on its own and can become dangerous if it gets trapped. Timely repair gives lasting relief and prevents emergencies.",
  "A hernia occurs when part of the intestine or tissue pushes through a weak spot in the abdominal wall, appearing as a bulge in the groin, navel or abdomen. It may cause discomfort when lifting, coughing or standing for long periods. Because hernias do not resolve without treatment, planned surgery is the safest option. We offer both laparoscopic and open mesh repair, chosen according to the hernia type, its size, your age and your daily activities. A strong mesh reinforces the weak area and lowers the chance of the hernia returning. Most patients go home within a day, and we provide clear advice on lifting, exercise and returning to work so that you recover safely and confidently.",
  ["Laparoscopic and open repair options", "Strong mesh reinforcement", "Day-care or one-night stay", "Low recurrence rates", "Guidance on safe return to activity"],
  [("Can a hernia heal without surgery?", "No. A hernia does not close by itself. Surgery is the only permanent treatment, and early repair is simpler and safer."),
   ("Is mesh repair safe?", "Modern surgical mesh is widely used and safe. It strengthens the repair and significantly reduces the risk of recurrence."),
   ("What happens if I delay surgery?", "The hernia may grow larger, become painful or get trapped, which can need emergency surgery.")],
  ["hernia surgeon in Pune", "hernia repair surgery", "laparoscopic hernia repair", "inguinal hernia treatment"]),
 ("piles-fissure-fistula-treatment", "Piles, Fissure & Fistula Treatment", "cross",
  "Discreet, modern treatment for piles, anal fissure and fistula, matched to the severity of your condition, from simple medical care to day-care procedures.",
  "Anorectal problems are common and treatable. We offer private consultation, accurate diagnosis and the least invasive option that works for you.",
  "Piles, fissures and fistulas cause pain, bleeding, itching or discharge, and many people delay care out of embarrassment. In our clinic, consultations are private, respectful and judgement-free. After a careful examination, we recommend the simplest effective treatment, ranging from dietary changes and medication to banding, laser or day-care surgery. Fistulas are assessed with imaging where needed so that the repair protects bowel control. Modern techniques mean less pain, quicker healing and a rapid return to daily life. Our team also guides you on diet, hydration and bowel habits to prevent recurrence, so you gain long-term relief and not just a temporary fix.",
  ["Private and respectful consultation", "Treatment matched to severity", "Day-care procedures available", "Imaging-guided fistula assessment", "Prevention and diet counselling"],
  [("Are piles always treated with surgery?", "No. Early piles often improve with diet, medication and lifestyle changes. Surgery is advised only for advanced or persistent cases."),
   ("Is the procedure painful?", "Modern anaesthesia and techniques keep discomfort low, and we provide pain relief and aftercare advice."),
   ("Can these conditions come back?", "Recurrence is possible, but good bowel habits and follow-up care greatly reduce the risk.")],
  ["piles treatment in Pune", "fissure treatment", "fistula surgery", "laser piles surgery"]),
 ("appendix-surgery", "Appendix Surgery", "clock",
  "Prompt laparoscopic appendectomy for appendicitis, with round-the-clock access to surgeons and a quick, comfortable recovery after the operation.",
  "Appendicitis needs fast attention. Our surgical team is available around the clock to diagnose and operate safely when required.",
  "Appendicitis usually begins with pain around the navel that shifts to the lower right abdomen, often with fever, nausea and loss of appetite. Without treatment, the appendix can burst and cause a serious infection, so early evaluation is essential. Our emergency surgical team is available 24×7 to examine you, arrange an ultrasound or CT scan and decide on treatment. Most cases are treated with laparoscopic appendectomy, which uses small incisions, causes less pain and allows an early return home. We explain each step to you and your family, keep you comfortable throughout and give clear instructions for wound care, diet and activity after discharge so that your recovery is smooth.",
  ["24×7 emergency surgical team", "Rapid diagnosis with imaging", "Laparoscopic appendectomy", "Short hospital stay", "Clear aftercare instructions"],
  [("What are the warning signs of appendicitis?", "Pain moving to the lower right abdomen, fever, vomiting and loss of appetite. Seek medical care promptly if these appear."),
   ("Can appendicitis be treated without surgery?", "Some mild cases may be managed with antibiotics, but surgery is the most reliable treatment. Your surgeon will advise."),
   ("How long is recovery?", "Most patients return to normal activity in one to two weeks after keyhole surgery.")],
  ["appendix surgery in Pune", "appendicitis treatment", "laparoscopic appendectomy", "emergency surgeon"]),
 ("kidney-stone-treatment", "Kidney Stone Treatment", "bed",
  "Advanced endoscopic removal of kidney and ureteric stones, planned around stone size, position and your risk of recurrence for lasting relief.",
  "Kidney stones cause severe pain and can damage the kidney if neglected. We use minimal-access techniques to clear stones safely.",
  "Kidney and ureteric stones often cause sudden, severe pain in the back or side, blood in the urine and nausea. Small stones may pass naturally with medication and fluids, but larger stones or those causing blockage need active treatment. After assessing your scans and kidney function, we choose the most suitable technique, such as ureteroscopy for stones in the ureter or percutaneous removal for larger kidney stones. These endoscopic methods avoid large incisions, reduce pain and speed up recovery. We also review the likely cause of your stones and advise on hydration, diet and follow-up tests, which helps reduce the chance of future stones and protects your kidney health in the long term.",
  ["Minimal-access endoscopic methods", "Treatment based on stone size and position", "Reduced pain and faster recovery", "Kidney function assessment", "Prevention and diet advice"],
  [("Can a kidney stone pass on its own?", "Small stones often do with plenty of fluids and medication. Larger or blocking stones need treatment."),
   ("Is stone surgery done without cuts?", "Many stones are removed endoscopically through natural passages or a very small keyhole."),
   ("How can I prevent new stones?", "Drink enough water, limit excess salt, follow dietary advice and attend recommended follow-up tests.")],
  ["kidney stone treatment in Pune", "kidney stone removal", "ureteric stone surgery", "endoscopic stone removal"]),
 ("lipoma-cyst-removal", "Lipoma & Cyst Removal", "user",
  "Safe day-care removal of lipomas, cysts and soft-tissue lumps after proper assessment, with neat stitching and minimal scarring for a natural result.",
  "Most skin and soft-tissue lumps are harmless, but they should be examined. We assess the lump first and remove it only when appropriate.",
  "A painless lump under the skin is often a lipoma, a cyst or a ganglion, and many are harmless. Even so, any new or growing lump deserves a proper examination, because some need further tests. During your consultation, the surgeon examines the swelling, may advise an ultrasound and explains whether observation or removal is best. Removal is usually a short day-care procedure under local anaesthesia, with neat stitching to keep the scar small. Tissue can be sent for laboratory testing when needed. You go home the same day with wound-care instructions, and follow-up ensures the area heals well. Early removal is simpler, particularly before a lump becomes large or infected.",
  ["Careful examination and diagnosis", "Day-care procedure", "Local anaesthesia in most cases", "Neat stitching, minimal scar", "Tissue testing when advised"],
  [("Do all lumps need to be removed?", "No. Harmless lumps can be monitored. Removal is advised if a lump grows, hurts or causes cosmetic concern."),
   ("Will the lump come back?", "If the lump is removed completely, recurrence is uncommon, although new ones can form elsewhere."),
   ("Is the procedure painful?", "The area is numbed with local anaesthesia, so you feel little discomfort during the procedure.")],
  ["lipoma removal in Pune", "cyst removal surgery", "ganglion treatment", "skin lump surgery"]),
 ("emergency-gi-surgery", "Emergency G.I. Surgery", "heart",
  "Round-the-clock emergency operating team for acute abdominal conditions such as obstruction, perforation and severe infection, with rapid decision-making.",
  "Sudden severe abdominal pain should never be ignored. Our 24×7 team is ready to assess and operate whenever there is an emergency.",
  "Acute abdominal emergencies, including intestinal obstruction, perforation, trapped hernia and abscess, need quick diagnosis and treatment. Our clinic maintains a 24×7 emergency operating team so that care never waits for morning. On arrival, patients are examined immediately, stabilised and investigated with blood tests and imaging. If surgery is needed, it is carried out in a fully equipped theatre with experienced anaesthesia support. We keep families informed at every stage and handle cashless mediclaim paperwork to reduce stress at a difficult time. If you have sudden severe pain, repeated vomiting or cannot pass gas or stool, please go to the nearest emergency facility first and call our emergency number.",
  ["24×7 emergency operating team", "Immediate assessment and imaging", "Fully equipped theatres", "Cashless mediclaim support", "Clear communication with family"],
  [("Is the emergency service open at night?", "Yes. Our emergency surgical team is available 24 hours a day, every day of the year."),
   ("Do you accept mediclaim?", "Yes. Cashless facility is available with many insurers. Our team helps with the paperwork."),
   ("What should I do in an abdominal emergency?", "Reach the nearest emergency facility without delay and call our emergency number so the team can prepare.")],
  ["emergency surgeon in Pune", "24 hour emergency surgery", "intestinal obstruction surgery", "emergency hospital Pune"]),
]

PRODUCTS = [
 ("post-surgery-recovery-kit", "Post-Surgery Recovery Kit", "Complete home-care kit with wound dressings, antiseptic, gauze, tape and a simple recovery guide prepared by our surgeons.",
  "Our Post-Surgery Recovery Kit gives you everything needed for safe wound care at home. It includes sterile dressings, antiseptic solution, gauze, medical tape, disposable gloves and an illustrated care booklet written by our surgical team. The kit is designed for day-care and short-stay patients who need clear, simple support after discharge. Each item is individually packed and clearly labelled for easy use."),
 ("abdominal-support-binder", "Abdominal Support Binder", "Breathable, adjustable binder that supports the abdomen after hernia and abdominal surgery, improving comfort during movement.",
  "The Abdominal Support Binder provides gentle compression and support after hernia repair and other abdominal operations. Made from breathable, skin-friendly fabric with an adjustable closure, it reduces discomfort when walking, coughing or changing position. Available in multiple sizes, and our team will advise you on the correct fit and how long to wear it."),
 ("compression-stockings", "Medical Compression Stockings", "Graduated compression stockings that help circulation and lower the risk of clots during recovery or long periods of rest.",
  "Medical Compression Stockings apply graduated pressure to the legs to improve blood circulation. They are commonly advised after surgery, during bed rest and for people with vein problems. The soft, durable fabric is comfortable for daily wear. Your surgeon will recommend the right compression level and size for your condition."),
 ("piles-comfort-cushion", "Piles Comfort Cushion", "Ergonomic donut-style cushion that reduces pressure while sitting, helping comfort during recovery from anorectal procedures.",
  "The Piles Comfort Cushion is an ergonomic seat cushion designed to relieve pressure on the sensitive area while sitting. It is useful during recovery from piles, fissure and fistula procedures and for people who sit for long hours. The firm, supportive foam keeps its shape, and the washable cover is easy to maintain."),
]

TESTIMONIALS = [  # [REPLACE] with real reviews
 ("Rahul Patil", "Gallbladder surgery patient", "The doctor explained everything patiently, and the keyhole surgery went smoothly. I was walking the same evening and home the next day. Truly caring staff."),
 ("Sunita Kulkarni", "Hernia repair patient", "I was nervous about surgery, but the team made me feel completely at ease. Clean rooms, honest advice and excellent follow-up care."),
 ("Amit Shinde", "Emergency appendix patient", "We arrived at midnight and the team acted immediately. The surgery was quick and my son recovered fast. We are grateful for the 24×7 care."),
]

WHY = [
 ("shield", "Experienced Surgeons", "Specialist general and laparoscopic surgeons with years of hands-on experience."),
 ("heart", "Patient-First Care", "Honest opinions, clear explanations and no pressure to operate."),
 ("pulse", "Advanced Technology", "Modern laparoscopic and endoscopic equipment in sterile operation theatres."),
 ("clock", "24×7 Emergency", "A dedicated emergency operating team available day and night."),
 ("cross", "Cashless Mediclaim", "Insurance and cashless support with help for all paperwork."),
 ("bed", "Comfortable Recovery", "Clean, private rooms designed for rest and a calmer recovery."),
]

FACILITIES = ["24-hour emergency operation", "Modern laparoscopic setup", "Comfortable private rooms", "Latest operation equipment", "Cashless mediclaim facility", "Ample parking facility"]

HOME_FAQ = [
 ("Do I really need surgery?", "Not always. During your consultation, the surgeon reviews your reports and will honestly tell you whether surgery is needed now, later or not at all."),
 ("Is keyhole surgery better than open surgery?", "For many procedures it means smaller cuts, less pain and quicker recovery, but the right approach depends on your condition. Your surgeon will explain why."),
 ("Is emergency care available at night?", "Yes. Our emergency operating team is available 24×7 for acute surgical problems."),
 ("Do you accept cashless mediclaim?", "Yes. We work with many insurance providers, and our team helps you with the process."),
]

TEAM = [("Dr. Abhijeet Suresh Shinde", "Founder & Senior Surgeon"), ("Dr. Neha Joshi", "Consultant Anaesthetist"), ("Dr. Sameer Kale", "Consultant Urologist")]  # [REPLACE]
AWARDS = ["Best Surgical Care Award", "NABH Entry Level Certificate", "Excellence in Patient Safety", "Laparoscopy Fellowship Certificate"]  # [REPLACE]

# Blogs. Body markup: "## " heading, "- " bullet, otherwise paragraph.
BLOGS = [
 dict(slug="gallbladder-stone-symptoms-and-treatment", title="Gallbladder Stone Symptoms and Treatment in Kharadi, Pune",
  sub="Learn the warning signs of gallstones, how they are diagnosed and when keyhole surgery is the right choice for you.",
  cat="Guides", date="2026-11-05", author="Dr. Abhijeet Suresh Shinde", glyph="heart", kw="gallbladder stone treatment in Pune",
  mt="Gallbladder Stone Symptoms and Treatment in Kharadi, Pune", 
  body="""Gallstones are one of the most common reasons people visit a surgeon for upper abdominal pain. Many stones stay silent for years, but once they start causing symptoms, they tend to return. Understanding the warning signs helps you seek care early and avoid complications. This guide explains what gallstones are, how they are treated and what recovery looks like.
## What are gallstones?
The gallbladder is a small pouch under the liver that stores bile, a fluid that helps digest fats. When substances in bile such as cholesterol or pigments harden, they form stones that can be as small as a grain of sand or as large as a golf ball. Stones may block the flow of bile, causing pain, inflammation or infection.
## Common symptoms
Symptoms often appear after a heavy or fatty meal. Typical signs include:
- Sharp pain in the upper right or middle abdomen that may spread to the back or right shoulder
- Nausea and vomiting
- Bloating, gas and indigestion
- Fever or chills if infection develops
- Yellowing of the skin or eyes if a stone blocks the bile duct
## Causes and risk factors
Gallstones are more common in women, people over 40, those with obesity or rapid weight loss, and those with a family history. Diets high in fat and low in fibre, diabetes and certain medications can also increase the risk. Pregnancy and long gaps between meals may contribute as well. While you cannot control every factor, a balanced diet and regular activity help lower your risk.
## How gallstones are diagnosed
Diagnosis usually begins with a clinical examination and an abdominal ultrasound, which clearly shows stones in the gallbladder. Blood tests check for infection and liver involvement. In some cases, additional imaging such as an MRI scan is advised to look at the bile ducts. A correct diagnosis allows your surgeon to plan the safest treatment for you.
## Treatment options
Stones that cause no symptoms are often only observed. However, when you have repeated pain, inflammation or complications, the standard treatment is removal of the gallbladder, called cholecystectomy. Medicines to dissolve stones are slow, unreliable and stones commonly return, so surgery is the lasting solution.
Most gallbladders today are removed by laparoscopic surgery. The surgeon makes a few tiny incisions, inserts a camera and fine instruments, and removes the gallbladder safely. Compared with open surgery, keyhole surgery means less pain, smaller scars and a faster return to routine.
## Is surgery safe?
Laparoscopic gallbladder removal is among the most commonly performed operations worldwide and has an excellent safety record when done by an experienced team. Before surgery, your surgeon reviews your health, explains the risks and benefits, and answers your questions. In a small number of cases, a conversion to open surgery may be needed for safety, and you will be told about this in advance.
## Recovery after surgery
Most patients walk within hours and go home the next day. You can usually return to light work within a week. Early meals should be light, and you can gradually return to your normal diet. Keep the wounds clean and dry, avoid heavy lifting for the period your surgeon advises, and attend your follow-up visit. Life without a gallbladder is completely normal for the majority of people.
## When to seek urgent help
Please seek immediate medical care if you have severe continuous abdominal pain, high fever, repeated vomiting or yellow discoloration of the eyes. These can be signs of a serious complication that needs prompt treatment.
## Conclusion
Gallstones are common and very treatable. If you have recurring upper abdominal pain, do not wait for a complication. A simple consultation and ultrasound can give you clear answers. To discuss your symptoms with our surgeon, contact us or message us on WhatsApp today."""),
 dict(slug="piles-vs-fissure-symptoms-causes-when-to-see-doctor", title="Piles vs Fissure: Symptoms, Causes and When to See a Doctor",
  sub="Not sure whether your anal pain or bleeding is piles or a fissure? Here is a simple guide to tell them apart.",
  cat="Tips", date="2026-10-28", author="Dr. Abhijeet Suresh Shinde", glyph="cross", kw="piles treatment in Pune",
  mt="Piles vs Fissure: Symptoms, Causes and When to See a Doctor",
  body="""Bleeding or pain around the anus is worrying, and many people feel too embarrassed to talk about it. The truth is that piles and fissures are very common and highly treatable. Because their symptoms overlap, it helps to understand the differences so you know when to seek help. This article explains both conditions in simple language.
## What are piles?
Piles, also called haemorrhoids, are swollen blood vessels inside or around the anus. Internal piles develop inside the rectum and often cause painless bleeding, while external piles form under the skin around the anus and can cause itching, swelling and discomfort. Piles may sometimes protrude outside during a bowel movement and then return on their own or need to be pushed back.
## What is an anal fissure?
An anal fissure is a small tear in the lining of the anal canal. It usually results from passing a hard or large stool. The hallmark of a fissure is sharp, cutting pain during and after a bowel movement, which may last for hours, often with a small amount of bright red blood on the tissue paper.
## Key differences at a glance
- Piles often cause painless bleeding, a lump or swelling, and itching
- Fissures typically cause severe pain during and after passing stool
- Piles bleeding may drip or coat the stool, while fissure bleeding is usually streaks on paper
- Fissures can cause tightness of the anal muscle, while piles can cause a feeling of incomplete emptying
## Common causes
Both conditions are linked to constipation and straining. Other contributors include a low-fibre diet, too little water, sitting for long hours, pregnancy, chronic diarrhoea and heavy lifting. Spending a long time on the toilet or using a mobile phone there also increases pressure on the area. Correcting these habits is an important part of treatment and prevention.
## Home care that helps
Many early cases improve with simple measures:
- Eat more fibre from fruits, vegetables, whole grains and pulses
- Drink plenty of water throughout the day
- Do not strain or sit on the toilet for long
- Take warm sitz baths for ten to fifteen minutes
- Stay active and avoid prolonged sitting
Medicines prescribed by your doctor, such as stool softeners and soothing ointments, can also give relief.
## When medical treatment is needed
If symptoms last more than a couple of weeks, keep returning or become severe, you should see a surgeon. Persistent bleeding needs proper examination, because other conditions can look similar and should not be ignored. Never assume that all rectal bleeding is piles.
For advanced piles, treatment options include rubber band ligation, laser or other day-care procedures and, in selected cases, surgery. Chronic fissures that do not heal may need a short procedure to relax the muscle and allow healing. Your surgeon will recommend the least invasive option that works for your condition.
## Is treatment painful?
Modern techniques and anaesthesia keep discomfort low, and most procedures are done as day care. Patients typically go home the same day and return to routine activity within a short time. Clear aftercare advice helps healing and lowers the chance of recurrence.
## Preventing a repeat problem
After treatment, continue a high-fibre diet, adequate hydration and regular exercise. Respond to the urge to pass stool without delay, and avoid straining. These small habits make the biggest difference to long-term relief.
## Conclusion
Piles and fissures are common, treatable and nothing to be embarrassed about. The earlier you seek advice, the simpler the treatment usually is. If you are dealing with pain or bleeding, book a private consultation with our surgeon by contacting us or messaging us on WhatsApp."""),
 dict(slug="laparoscopic-surgery-recovery-what-to-expect", title="Laparoscopic Surgery Recovery: What to Expect After",
  sub="A practical day-by-day guide to recovery after keyhole surgery, including diet, activity, wound care and warning signs.",
  cat="News", date="2026-10-20", author="Dr. Abhijeet Suresh Shinde", glyph="pulse", kw="laparoscopic surgery recovery",
  mt="Laparoscopic Surgery Recovery: What to Expect After Surgery",
  body="""Laparoscopic, or keyhole, surgery is popular because it allows most people to recover faster than after open surgery. Even so, knowing what to expect helps you plan your time off, manage discomfort and spot problems early. This guide walks you through the typical recovery after common laparoscopic procedures such as gallbladder, hernia and appendix surgery.
## The first day in hospital
After the operation, you are monitored in a recovery area until the anaesthesia wears off. Mild pain around the incisions is normal and is controlled with medicines. Some people feel shoulder-tip pain for a day or two, caused by the gas used to inflate the abdomen during surgery, which settles quickly. Most patients sit up and walk with assistance within hours.
## Eating and drinking
You usually begin with sips of water, followed by light food such as soup, khichdi or toast once you feel comfortable. Over the next few days, you can return to a normal diet unless your surgeon advises otherwise. Eat smaller, more frequent meals at first and avoid very oily or spicy food while your digestion settles.
## Pain and medicines
Pain after keyhole surgery is generally mild to moderate. Take medicines exactly as prescribed, and do not wait for pain to become severe. Walking regularly also reduces discomfort and gas. If your pain is increasing instead of improving, let your surgeon know.
## Caring for your wounds
The small incisions are covered with waterproof dressings or skin glue. Keep them clean and dry, and follow instructions about when you can shower. Avoid applying creams or home remedies unless advised. Mild bruising and slight redness at the edges are normal.
## Activity and getting back to work
Walking is encouraged from day one because it improves circulation and reduces the risk of blood clots. Light daily activity can resume quickly. As a general guide:
- Office or desk work: often within one week
- Driving: when you can turn and brake comfortably without pain
- Heavy lifting and strenuous exercise: usually after two to four weeks, depending on the surgery
- Hernia repair patients should follow lifting restrictions carefully to protect the repair
Always follow the specific advice given by your surgeon, as recovery varies from person to person.
## Warning signs you should not ignore
Contact your surgeon or visit the emergency department if you notice:
- Fever above 38°C or chills
- Increasing pain, swelling or redness near the wounds
- Pus or foul-smelling discharge
- Persistent vomiting or inability to eat or drink
- Severe abdominal swelling or no passage of gas or stool
- Yellowing of the skin or eyes
Early attention to these signs allows quick and simple treatment.
## Tips for a smoother recovery
Rest when you are tired, but do not stay in bed all day. Drink enough water, include fibre in your meals to avoid constipation and sleep well. Avoid smoking, which delays healing. Attend all follow-up visits, since they let your surgeon check your wounds and answer your questions.
## Emotional wellbeing
It is normal to feel tired or a little low for a few days after any operation. Gentle activity, good food, sunlight and support from family usually help. If your mood does not improve, speak to your doctor.
## Conclusion
Most people recover well and return to their normal routine within days to a few weeks after laparoscopic surgery. With clear guidance and good follow-up, recovery can be comfortable and uneventful. If you have questions about an upcoming procedure or your recovery, contact our team or message us on WhatsApp."""),
]

PRIVACY = [
 ("Information We Collect", "We collect information you provide when you book an appointment, fill an enquiry form, call or message us. This may include your name, phone number, email address, age, gender, preferred service and any health-related details you choose to share. We also collect limited technical data such as browser type, device and pages visited through cookies and analytics."),
 ("How We Use Your Information", "We use your information to schedule and confirm appointments, respond to enquiries, provide patient care, send important service messages, improve our website and meet legal obligations. We do not sell your personal information."),
 ("Cookies and Analytics", "Our website uses cookies and similar technologies to remember preferences and understand how visitors use the site. You can disable cookies in your browser settings, although some features may not work as expected."),
 ("Sharing of Information", "We share information only with doctors and staff involved in your care, with service providers who help operate our systems under confidentiality obligations, with insurers where you request cashless services, and with authorities where required by law."),
 ("Data Security", "We use reasonable administrative, technical and physical safeguards to protect your information against unauthorised access, loss or misuse. No method of transmission over the internet is completely secure, so we cannot guarantee absolute security."),
 ("Patient Rights", "You may request access to the personal information we hold about you, ask us to correct inaccurate information, and withdraw your consent for non-essential communication at any time by contacting us using the details below."),
 ("Data Retention", "We keep personal information only as long as necessary for the purposes described here, for medical record requirements and to comply with applicable laws."),
 ("Third-Party Links", "Our website may contain links to third-party sites such as Google Maps and social media. We are not responsible for the privacy practices of those websites."),
 ("Policy Updates", "We may update this Privacy Policy from time to time. The latest version will always be available on this page with the revised date."),
 ("Contact for Privacy Concerns", "For any privacy-related question or request, please contact us using the email address and phone number shown below."),
]
TERMS = [
 ("Use of the Website", "By accessing this website, you agree to these Terms and Conditions. You agree to use the site only for lawful purposes and not to misuse, copy or disrupt any part of it."),
 ("Medical Information Disclaimer", "The information on this website, including blogs and service pages, is for general awareness only. It is not a substitute for professional medical advice, diagnosis or treatment. Always consult a qualified doctor about your health."),
 ("Appointments and Cancellations", "Appointment requests made online are subject to confirmation by our team. We may contact you to confirm, reschedule or decline a request. Please inform us in advance if you need to cancel or change your appointment."),
 ("Emergency Disclaimer", "This website is not for emergencies. If you are experiencing a medical emergency, go to the nearest emergency facility immediately and call our emergency number."),
 ("Products", "Product information is provided for general reference. Availability, pricing and suitability should be confirmed with our team, and use should follow your doctor's advice."),
 ("Intellectual Property", "All text, graphics, logos and other content on this website belong to the hospital or its licensors and may not be copied or reused without written permission."),
 ("Limitation of Liability", "While we work to keep the website accurate and available, we do not guarantee that it is free from errors or interruptions. To the extent permitted by law, we are not liable for any loss arising from your use of this website."),
 ("Governing Law and Jurisdiction", "These Terms are governed by the laws of India. Any dispute is subject to the exclusive jurisdiction of the courts in " + C["city"] + ", Maharashtra."),
 ("Changes to These Terms", "We may revise these Terms at any time. Continued use of the website after changes means you accept the updated Terms."),
 ("Contact", "For questions about these Terms, please contact us using the details below."),
]

# Extra sections inserted before the conclusion of each blog (keeps articles within 800-1200 words)
EXTRA = {
 "gallbladder-stone-symptoms-and-treatment": """## Diet tips to ease gallstone symptoms
Food does not dissolve gallstones, but sensible eating can reduce painful attacks while you wait for treatment. Choose smaller, regular meals instead of long gaps followed by heavy ones. Limit fried food, full-fat dairy, bakery items and processed snacks, which make the gallbladder contract strongly. Include vegetables, fruits, whole grains, pulses and lean protein, and drink enough water through the day.
Avoid crash diets and very rapid weight loss, as these can actually encourage new stones to form. If you need to lose weight, aim for a gradual and steady plan.
## Questions patients commonly ask
Many people ask whether gallstones can be flushed out with home remedies or herbal drinks. There is no reliable evidence that such methods remove stones, and they can delay proper treatment or cause dangerous blockages. Others worry that surgery is risky or that digestion will suffer. In reality, the operation is routine, and most people eat normally afterwards, although some notice softer stools for a few weeks. Another common question is whether stones found by chance must be removed. If you have no symptoms, your surgeon may simply advise regular review, but diabetes, large stones or a history of pancreatitis can change that advice, so a personal assessment is important.""",
 "piles-vs-fissure-symptoms-causes-when-to-see-doctor": """## Myths about piles and fissures
Several myths stop people from getting timely care. One is that piles always need surgery, when in fact most early cases settle with simple measures. Another is that spicy food alone causes piles; while it may irritate, the real drivers are constipation, straining and low fibre. Many also believe that bleeding always means piles, yet other bowel and rectal conditions can look similar, which is why examination matters. Finally, some think these problems affect only the elderly, but they are common in young adults, office workers and new mothers.
Women may notice flare-ups during pregnancy or after delivery because of hormonal changes and pressure, and these usually respond well to gentle treatment and dietary care.
## What to expect at your consultation
At your visit, the surgeon will ask about your bowel habits, diet, pain and bleeding, and will perform a gentle, private examination. Sometimes a short scope test is advised to look inside the rectum and rule out other conditions. You will leave with a clear diagnosis, a treatment plan and practical advice. There is no need to feel embarrassed, as our team handles these concerns every day with sensitivity and respect. Most patients say they wish they had come sooner.""",
 "laparoscopic-surgery-recovery-what-to-expect": """## Recovery after specific procedures
Recovery varies by operation. After gallbladder removal, most people go home the next day and eat a light diet within hours. After laparoscopic appendectomy, you can usually walk the same day and resume desk work within one to two weeks. Hernia repair patients also walk early, but must be careful with heavy lifting for several weeks so that the repair can strengthen. Procedures on the bowel take longer, with a slower return to diet and activity, and your surgeon will give individual guidance.
## Sleep, diet and hydration
Good rest speeds healing, so sleep on your back or a comfortable side, with a pillow to support the abdomen when you cough or move. Eat protein-rich foods such as eggs, dal, curd and lean meat, together with fruit and vegetables, to support tissue repair. Fibre and fluids prevent constipation, which can strain your wounds, especially after hernia surgery. Limit tea, coffee and fizzy drinks in the first days if they upset your stomach.
## Follow-up visits
Your first follow-up is usually within one to two weeks. The surgeon checks your wounds, reviews any test reports and answers questions about returning to work, exercise and travel. Bring a list of questions and any medicines you are taking. Do not skip this visit even if you feel completely well, since it is the best opportunity to confirm that healing is on track.""",
}
for _b in BLOGS:
    _b["body"] = _b["body"].replace("## Conclusion", EXTRA[_b["slug"]] + "\n## Conclusion")

# ======================= DISHA CLINIC OVERRIDES =======================
C.update(
    name="DISHA Advanced Surgical & Laser Piles Clinic", short="Disha",
    tagline="Journey towards better life",
    owner="Dr. Abhijeet Suresh Shinde", doctor="Dr. Abhijeet Suresh Shinde",
    quals="MS (General Surgery) | DEMS | DIHM",
    role="General & Laparoscopic Surgeon | Consultant Proctologist",
    exp_years="10+", patients="3,500+",
    est="2026", founded="20 October 2026", founded_iso="2026-10-20",
    address="1st Floor, OPD No. 2, Survey No. 22/2, Ganga Altus, F Building, Cherry Life, Near Manipal Hospital, Thite Nagar, Kharadi, Pune, Maharashtra 411014",
    street="1st Floor, OPD No. 2, Survey No. 22/2, Ganga Altus, F Building, Cherry Life, Near Manipal Hospital, Thite Nagar, Kharadi",
    locality="Kharadi, Pune", postal="411014",
    city="Pune", areas="Kharadi, Pune",
    about_clinic="Disha Advanced Surgical and Laser Piles Clinic in Kharadi, Pune, specializes in advanced laser and laparoscopic care for piles, fissures, fistulas, hernias, gallstones and varicose veins, alongside comprehensive GI diagnostics and oncology surgery.",
    phone="+91 97668 15782", phone_tel="+919766815782", whatsapp="919766815782",
    appt="+91 97668 15782", appt_tel="+919766815782", emergency="+91 97668 15782", emergency_tel="+919766815782",
    email="info@dishaclinic.example", hours="Daily: 10:00 AM – 9:00 PM", hours2="Call ahead for appointments",
    base="https://www.dishaclinic.example",
    map_embed="https://www.google.com/maps?q=Ganga+Altus+Cherry+Life+Thite+Nagar+Kharadi+Pune+411014&output=embed",
    map_link="https://maps.app.goo.gl/dh9mbhsyUwVJ43zh7",
    slots=["10:00 AM","11:00 AM","12:00 PM","01:00 PM","02:00 PM","03:00 PM","04:00 PM","05:00 PM","06:00 PM","07:00 PM","08:00 PM"],
    closed_days=[],
)
# Credentials supplied by the client (Requirement Document, Section 1)
CREDENTIALS = [
    ("Postgraduate", "MS (General Surgery)", "Master of Surgery in General Surgery", "award"),
    ("Emergency Care", "DEMS", "Diploma in Emergency Medical Services, Ruby Hall Clinic, Pune", "clock"),
    ("Industrial Health", "DIHM", "Diploma in Industrial Health Management, Ruby Hall Clinic, Pune", "shield"),
    ("Laser Proctology", "Diploma in Laser Proctology", "Advanced laser techniques for piles, fissure and fistula", "pulse"),
    ("Proctology Training", "Healing Hands Clinic, Pune", "Specialised proctology training", "user"),
]
_old = {s[0]: s for s in SERVICES}
def _kw(n): l = n.lower(); return [f"{l} in Pune", f"best {l} doctor in Kharadi", f"{l} treatment cost Pune", f"{l} specialist Kharadi Pune"]
_gen = [("Is the consultation private?", "Yes. Every consultation and examination is private, respectful and judgement-free."),
        ("How do I book an appointment?", "Call or WhatsApp +91 97668 15782, or use the online booking form. The clinic is open daily from 10 AM to 9 PM.")]
def S(slug, name, icon, short, intro, full, feats, faqs, kw=None):
    return (slug, name, icon, short, intro, full, feats, list(faqs) + _gen, kw or _kw(name))
def _o(slug, name=None, icon=None):
    s = _old[slug]; return (s[0], name or s[1], icon or s[2], s[3], s[4], s[5], s[6], list(s[7]) + _gen[:1], s[8])
_c = lambda n: n.replace("Pune", "Pune")

SERVICES = [
 S("laser-piles-treatment", "Laser Piles Treatment", "pulse",
   "Advanced laser treatment for piles (haemorrhoids) that shrinks the swelling with minimal cuts, less pain and a quick return to routine.",
   "Laser piles surgery is a modern, minimally invasive way to treat piles with very little bleeding and a faster recovery.",
   "In laser treatment, a fine laser fibre delivers focused energy to the piles mass, shrinking it and sealing the blood supply without large wounds. Compared with conventional surgery, patients usually report less pain, minimal bleeding, a short procedure time and an early return to work. It is suited to many grade 2, 3 and some grade 4 piles. Dr. Shinde examines you first and recommends laser only when it is the right option for you.",
   ["Minimal cutting and bleeding","Short day-care procedure","Less post-operative pain","Quick return to daily routine","Suitable for many grades of piles"],
   [("Is laser piles surgery painful?","Discomfort is much lower than with conventional surgery. Pain relief and aftercare advice are provided."),("Can piles return after laser treatment?","Recurrence is possible if constipation and straining continue, so diet and bowel-habit guidance is part of the plan.")],
   ["laser piles treatment in Pune","laser surgery for piles","painless piles treatment","best piles doctor in Pune"]),
 S("piles-haemorrhoid-surgery", "Piles (Haemorrhoid) Treatment", "cross",
   "Treatment for piles matched to the grade, from diet and medicines to rubber-band ligation, stapler and surgical removal.",
   "Piles are common and treatable. We choose the simplest option that works for your grade and lifestyle.",
   "Piles cause bleeding, pain, itching or a lump around the anus. Early piles often settle with diet, fibre, fluids and medicines. Advanced piles may need a day-care procedure such as banding, laser, stapler haemorrhoidopexy or conventional haemorrhoidectomy. After a private examination, Dr. Shinde explains every option and its trade-offs so that you decide with full information.",
   ["Private, gentle examination","Treatment matched to piles grade","Laser, stapler and open options","Diet and bowel-habit counselling","Clear recovery plan"],
   [("Do all piles need surgery?","No. Early piles often improve with diet, medication and lifestyle changes. Surgery is advised only for advanced or persistent piles."),("Is bleeding during stools always piles?","Not always. Bleeding should be examined to rule out other conditions, so please do not self-treat for long.")],
   ["piles treatment in Pune","haemorrhoid surgery","piles doctor Pune","piles specialist"]),
 S("fissure-treatment", "Anal Fissure Treatment", "shield",
   "Relief for the sharp, tearing pain of an anal fissure with ointments, Botox or a short procedure such as lateral sphincterotomy.",
   "A fissure is a small tear that causes severe pain and bleeding during or after passing stools.",
   "Most acute fissures heal with stool softeners, topical ointments and warm sitz baths. Chronic fissures that keep coming back may need Botox injection or a short procedure called lateral internal sphincterotomy, which relaxes the muscle and allows healing. Dr. Shinde examines gently and selects the treatment that gives lasting relief with minimum risk.",
   ["Ointment and medical management","Botox and procedure options","Short day-care surgery if needed","High success in relieving pain","Prevention guidance"],
   [("Why does a fissure hurt so much?","The tear exposes sensitive tissue and the muscle goes into spasm, which delays healing."),("Will I need surgery?","Many heal with medicines. Surgery is reserved for chronic fissures that do not respond.")]),
 S("fistula-treatment", "Anal Fistula Treatment", "pulse",
   "Assessment of anal fistula, with MRI where needed, and repair chosen to cure the tract while protecting bowel control.",
   "A fistula is an abnormal tunnel near the anus that causes recurring discharge, pain and abscesses.",
   "Fistulas rarely heal on their own and often follow an abscess. Treatment depends on how the tract runs in relation to the sphincter muscles. Options include fistulotomy, seton placement, LIFT, laser closure and flap procedures. MRI is advised for complex or recurrent cases so that the tract is mapped accurately and the repair protects continence.",
   ["Accurate mapping of the tract","Sphincter-saving techniques","Laser and conventional options","Care for recurrent fistula","Follow-up until healed"],
   [("Can a fistula heal with medicines?","Antibiotics may settle infection but the tunnel usually needs a procedure to heal."),("Will surgery affect bowel control?","Techniques are chosen to protect the muscle, and the risk is explained before surgery.")]),
 S("pilonidal-sinus-surgery", "Pilonidal Sinus Treatment", "shield",
   "Treatment of painful, discharging sinuses at the top of the buttock cleft, from minimal procedures to flap repair.",
   "A pilonidal sinus is a hair-related infection near the tailbone that tends to recur without correct treatment.",
   "Pilonidal disease causes pain, swelling and discharge above the natural cleft. Treatment ranges from abscess drainage to sinus excision, minimally invasive pit-picking and flap procedures that lower recurrence. Wound care and hair-removal advice after surgery are an important part of cure.",
   ["Drainage of acute abscess","Minimally invasive options","Flap procedures for recurrence","Wound-care guidance"],
   [("Why does it keep coming back?","Hair keeps entering the sinus; correct surgery and hair control reduce recurrence.")]),
 S("perianal-abscess-drainage", "Perianal Abscess Treatment", "clock",
   "Prompt drainage of painful perianal abscesses, with a plan to prevent a fistula from forming.",
   "A perianal abscess causes throbbing pain and swelling near the anus and needs timely drainage.",
   "An abscess is a collection of pus that does not respond to antibiotics alone. Drainage under anaesthesia gives quick relief. Because many abscesses lead to a fistula, Dr. Shinde examines for an underlying tract and plans the next step if needed.",
   ["Quick relief by drainage","Day-care procedure","Check for hidden fistula","Clear aftercare"],
   [("Can an abscess be treated with tablets?","Tablets alone rarely cure it. Drainage is the definitive treatment.")]),
 _o("laparoscopic-surgery"), _o("gallbladder-stone-surgery"), _o("hernia-repair-surgery"), _o("appendix-surgery"),
 S("diagnostic-laparoscopy", "Diagnostic Laparoscopy", "eye",
   "A keyhole look inside the abdomen to find the cause of unexplained pain or problems scans cannot clarify.",
   "When tests are inconclusive, a small camera can show the cause and often treat it in the same sitting.",
   "Diagnostic laparoscopy uses a tiny camera through a small cut to inspect the abdominal organs. It helps in chronic abdominal pain, suspected adhesions, infection and some undiagnosed lumps, and allows biopsy or treatment during the same procedure.",
   ["Small incisions","Direct view of organs","Biopsy possible","Quick recovery"],
   [("Is it done under anaesthesia?","Yes, under general anaesthesia, and most patients go home within a day or two.")]),
 S("hydrocele-surgery", "Hydrocele Surgery", "shield",
   "Safe surgical correction of hydrocele, the painless fluid swelling around the testis, as a short procedure.",
   "Hydrocele surgery removes the fluid sac and prevents it from refilling.",
   "A hydrocele is a collection of fluid around the testicle that can grow large and uncomfortable. It does not disappear with medicines. A short operation removes or folds the sac, and most patients return home the same day or the next day.",
   ["Short procedure","Day-care or one-night stay","Low recurrence","Clear recovery advice"],
   [("Does a hydrocele need surgery?","If it is large, uncomfortable or growing, surgery is the lasting solution.")]),
 S("bowel-surgery", "Small & Large Bowel Surgery", "pulse",
   "Open and laparoscopic surgery for bowel obstruction, perforation, tumours and other intestinal disease.",
   "Careful bowel surgery restores function and removes disease with the safest possible technique.",
   "Bowel surgery may be needed for blockage, perforation, diverticular disease, strictures or growths. Where suitable, keyhole techniques are used for smaller wounds and faster recovery. Planning includes tests, nutrition and clear counselling for the patient and family.",
   ["Laparoscopic where suitable","Detailed pre-operative planning","Nutrition and recovery support","Family counselling"],
   [("Is keyhole possible for bowel surgery?","In many planned cases yes, while emergencies may need open surgery.")]),
 _o("kidney-stone-treatment"),
 S("ureteric-stone-removal", "Ureteric Stone Removal (URS)", "pulse",
   "Telescopic removal of stones stuck in the ureter without any cut, usually as a day-care or short-stay procedure.",
   "URS treats ureteric stones through the natural passage with no incision.",
   "Ureteric stones cause severe colicky pain, vomiting and blood in urine. In ureteroscopy, a thin scope reaches the stone, which is broken and removed. A temporary stent may be placed. Most patients go home within a day.",
   ["No external cut","Short hospital stay","Quick pain relief","Stone-prevention advice"],
   [("Will a stent be needed?","Sometimes a thin stent is placed for a short time and removed later.")]),
 S("prostate-surgery", "Prostate Surgery (TURP)", "shield",
   "Telescopic prostate surgery for urinary blockage caused by an enlarged prostate.",
   "TURP relieves urine flow problems from prostate enlargement without an external cut.",
   "An enlarged prostate can cause weak stream, frequent urination and retention. When medicines fail, TURP removes the obstructing tissue through the urethra. Patients are counselled about recovery, catheter care and follow-up.",
   ["No external incision","Improved urine flow","Clear catheter guidance","Follow-up care"],
   [("When is surgery advised?","When medicines no longer help or complications like retention or stones occur.")]),
 S("stricture-urethra", "Stricture Urethra Treatment", "pulse",
   "Treatment for narrowing of the urinary passage causing weak stream and repeated infections.",
   "Urethral stricture treatment restores a comfortable flow of urine.",
   "A stricture is scarring that narrows the urethra. Options include dilatation, internal urethrotomy and reconstruction for selected cases. Treatment is chosen by length and site of the narrowing.",
   ["Accurate assessment","Endoscopic options","Reconstruction when needed","Follow-up to avoid recurrence"],
   [("Can a stricture return?","Recurrence is possible, so follow-up and sometimes self-dilatation are explained.")]),
 _o("lipoma-cyst-removal", "Lipoma, Cyst & Swelling Removal"),
 S("breast-lump-removal", "Breast Lump Removal", "heart",
   "Careful assessment and removal of breast lumps, with sensitive counselling and biopsy where required.",
   "Any new breast lump deserves proper assessment, and many are harmless.",
   "Breast lumps may be fibroadenomas, cysts or, rarely, something more serious. After examination and imaging, a biopsy may be advised. Removal is planned with cosmetic care and the tissue is sent for confirmation.",
   ["Examination and imaging","Biopsy where needed","Cosmetic incision","Private consultation"],
   [("Are all lumps cancer?","No, most are benign, but every lump should be examined.")]),
 S("thyroid-surgery", "Thyroid Surgery", "shield",
   "Surgery for thyroid nodules, goitre and selected thyroid conditions, with attention to voice and calcium safety.",
   "Thyroid surgery is planned carefully after scans, blood tests and clear counselling.",
   "A thyroid operation may be advised for large goitre, suspicious nodules or overactivity not controlled by medicine. Half or full removal is chosen by diagnosis. Dr. Shinde explains the effect on voice, calcium and the need for tablets after surgery.",
   ["Thorough pre-operative work-up","Voice-nerve protection","Clear counselling on tablets","Follow-up blood tests"],
   [("Will I need tablets afterwards?","After full removal yes, and sometimes after half removal. This is explained beforehand.")]),
 S("circumcision-surgery", "Circumcision (Adult & Child)", "check",
   "Safe, hygienic circumcision for medical reasons using modern techniques, with private and comfortable care.",
   "Circumcision is performed with strict hygiene, local or regional anaesthesia and clear aftercare.",
   "Circumcision may be advised for phimosis, recurrent infection or personal preference. Modern techniques, including stapler and conventional methods, are chosen to suit age and condition. The procedure is short and done in a private, comfortable setting.",
   ["Short day-care procedure","Private and comfortable","Modern techniques","Clear wound care"],
   [("How long is recovery?","Most people return to routine in a few days, with follow-up as advised.")]),
 S("corn-surgery", "Foot Corn Treatment", "check",
   "Treatment for painful or recurring corns and calluses with extra care for patients with diabetes.",
   "A corn is thickened skin from pressure and can be removed with a short procedure.",
   "Corns can make walking painful and may become infected, especially in diabetes. Treatment removes the corn and corrects the pressure cause with footwear advice so that it does not return.",
   ["Short day-care procedure","Footwear advice","Diabetic foot care","Low recurrence"],
   [("Can corns come back?","They can if pressure continues, so footwear guidance matters.")]),
 S("ingrown-toenail-surgery", "Ingrown Toenail Surgery", "check",
   "A short nail procedure for a toenail that keeps digging in, with care advice to stop it returning.",
   "Ingrown toenail surgery gives lasting relief from pain and repeated infection.",
   "When the nail edge digs into the skin it causes pain and infection. Under local anaesthesia the offending portion is removed and the nail bed treated so that it does not regrow into the skin. Most people walk out the same day.",
   ["Local anaesthesia","Day-care procedure","Low recurrence","Simple aftercare"],
   [("Is it painful?","The area is numbed, and aftercare pain is usually mild.")]),
 S("abscess-surgery", "Abscess Surgery", "clock",
   "Timely incision and drainage of abscesses anywhere on the body, with wound care until healed.",
   "An abscess needs drainage, not just antibiotics, for quick relief and healing.",
   "Abscesses are painful collections of pus that need prompt drainage under anaesthesia, followed by dressings and follow-up. Early treatment prevents spread of infection.",
   ["Prompt drainage","Day-care in many cases","Dressing guidance","Follow-up until healed"],
   [("Can antibiotics alone cure it?","Usually not. Drainage is the key treatment.")]),
 S("diabetic-foot-surgery", "Diabetic Foot Care & Surgery", "heart",
   "Early assessment and surgical care for diabetic foot ulcers and infections to protect the limb.",
   "Diabetic foot problems can worsen quickly. Early surgical care saves limbs.",
   "Diabetic ulcers and infections need debridement, drainage and careful sugar control. Early treatment prevents spreading infection and lowers the risk of amputation. Foot-care education is part of treatment.",
   ["Wound debridement","Infection control","Foot-care education","Follow-up dressings"],
   [("When should I see a surgeon?","At the first non-healing wound, redness, swelling or blackened skin.")]),
 S("upper-gi-endoscopy", "Upper GI Endoscopy", "eye",
   "A short telescopic examination of the food pipe, stomach and duodenum to find the cause of acidity, pain or bleeding.",
   "Upper GI endoscopy gives a direct look at the upper digestive tract.",
   "Endoscopy helps in persistent acidity, difficulty swallowing, upper abdominal pain and bleeding. A thin flexible scope is passed after throat numbing or light sedation. Biopsies can be taken during the same procedure.",
   ["Short procedure","Biopsy possible","Same-day discharge","Clear report"],
   [("Is it painful?","It is usually well tolerated with throat spray or light sedation.")]),
 S("lower-gi-endoscopy", "Lower GI Endoscopy (Colonoscopy)", "eye",
   "Examination of the rectum and colon to evaluate bleeding, change in bowel habit and polyps.",
   "Colonoscopy finds the cause of rectal bleeding and detects problems early.",
   "A flexible scope examines the large bowel for piles, polyps, colitis or growths. Biopsies or polyp removal can be done in the same sitting. Bowel preparation instructions are given beforehand.",
   ["Detects polyps and growths","Biopsy possible","Bowel-prep guidance","Day-care procedure"],
   [("Who needs a colonoscopy?","People with rectal bleeding, change in bowel habit or advised screening.")]),
 _o("emergency-gi-surgery"),
]
GROUPS = [
 ("Anorectal Surgeries", "cross", "Piles, fissure, fistula and more with laser and modern techniques", ["laser-piles-treatment","piles-haemorrhoid-surgery","fissure-treatment","fistula-treatment","pilonidal-sinus-surgery","perianal-abscess-drainage"]),
 ("Laparoscopic & Abdominal Surgeries", "pulse", "Keyhole surgery and abdominal care for faster recovery", ["laparoscopic-surgery","gallbladder-stone-surgery","hernia-repair-surgery","appendix-surgery","diagnostic-laparoscopy","bowel-surgery"]),
 ("Urological Surgeries", "heart", "Stones, prostate, urethra, hydrocele and circumcision care", ["kidney-stone-treatment","ureteric-stone-removal","prostate-surgery","stricture-urethra","hydrocele-surgery","circumcision-surgery"]),
 ("General & Day-care Surgeries", "check", "Lumps, thyroid, abscess, corn and toenail surgery", ["lipoma-cyst-removal","breast-lump-removal","thyroid-surgery","abscess-surgery","corn-surgery","ingrown-toenail-surgery"]),
 ("Endoscopy, Emergency & Foot Care", "eye", "Scopes, urgent GI surgical care and diabetic foot surgery", ["upper-gi-endoscopy","lower-gi-endoscopy","emergency-gi-surgery","diabetic-foot-surgery"]),
]
CORE = ["laser-piles-treatment","piles-haemorrhoid-surgery","fissure-treatment","fistula-treatment","gallbladder-stone-surgery","hernia-repair-surgery","appendix-surgery","kidney-stone-treatment","lipoma-cyst-removal","circumcision-surgery","laparoscopic-surgery","pilonidal-sinus-surgery"]

_oldp = {p[0]: p for p in PRODUCTS}
PRODUCTS = [
 ("sitz-bath-tub", "Sitz Bath Tub", "Comfortable over-the-toilet sitz bath tub for soothing warm-water soaks after piles, fissure or fistula treatment.",
  "The Sitz Bath Tub fits over a standard toilet seat and lets you soak the anal area in warm water, which relaxes the muscle, eases pain and keeps the area clean. It is recommended by our surgeons after piles, fissure and fistula procedures and for everyday relief. Easy to clean and suitable for adults."),
 _oldp["piles-comfort-cushion"], _oldp["post-surgery-recovery-kit"], _oldp["abdominal-support-binder"], _oldp["compression-stockings"],
 ("gentle-anal-care-wipes", "Gentle Anal Care Wipes", "Soft, alcohol-free, fragrance-free wipes for gentle cleaning of the sensitive area during piles and fissure recovery.",
  "Gentle Anal Care Wipes are designed for comfortable hygiene when plain toilet paper is too harsh. They are alcohol-free and fragrance-free, which helps avoid irritation of sensitive or healing skin. Useful after bowel movements and during recovery from piles, fissure and fistula procedures. Ask our team if they suit your condition."),
 ("dietary-fibre-supplement", "Dietary Fibre Supplement", "Psyllium-based fibre supplement that helps keep stools soft and regular, reducing straining in piles and fissure.",
  "A good fibre intake is a cornerstone of piles and fissure care. This psyllium-based dietary fibre supplement is mixed with water and taken as advised to keep stools soft and regular, so there is less straining. It supports, but does not replace, a healthy high-fibre diet and plenty of fluids. Please follow Dr. Shinde's advice on dosing."),
 ("hot-cold-gel-pack", "Hot & Cold Gel Pack", "Reusable gel pack for soothing swelling and discomfort, used hot or cold as advised by your surgeon.",
  "The Hot & Cold Gel Pack can be chilled to reduce swelling or warmed to relax muscles, as advised after a procedure. The soft, flexible pad moulds to the body and is reusable. Always wrap it in a thin cloth and follow your surgeon's instructions for how long and how often to use it."),
]
WHY = [
 ("shield", "Specialist Surgeon", "Dr. Shinde is a general & laparoscopic surgeon and consultant proctologist."),
 ("pulse", "Laser & Modern Techniques", "Advanced laser, stapler and keyhole options chosen to suit you."),
 ("heart", "Honest Advice", "A clear opinion on whether you need surgery, with no pressure."),
 ("users", "Private & Respectful", "Discreet consultations in a comfortable, judgement-free setting."),
 ("clock", "Convenient Timing", "Open daily from 10 AM to 9 PM for easy appointments."),
 ("check", "Same Surgeon, Start to Finish", "The surgeon who examines you operates and follows up your recovery."),
]
FACILITIES = ["Advanced laser surgery setup", "Modern laparoscopic equipment", "Private consultation room", "Sterile operation theatre", "Comfortable recovery area", "Open daily 10 AM – 9 PM"]
HOME_FAQ = [
 ("Is laser treatment better than conventional piles surgery?", "Laser usually means less pain, minimal bleeding and quicker recovery, but the best choice depends on your grade and anatomy. Dr. Shinde will explain this after examination."),
 ("Do I really need surgery for piles?", "Not always. Early piles often improve with diet, fluids and medicines. Surgery is advised only when needed."),
 ("Is my consultation private?", "Yes. Examinations are private, gentle and respectful."),
 ("What are your clinic timings?", "We are open daily from 10:00 AM to 9:00 PM. Call +91 97668 15782 to book."),
]
TESTIMONIALS = []   # add real patient reviews here (with consent). Section hides itself when empty.
TEAM = [("Dr. Abhijeet Suresh Shinde", "General & Laparoscopic Surgeon | Consultant Proctologist")]
AWARDS = []
