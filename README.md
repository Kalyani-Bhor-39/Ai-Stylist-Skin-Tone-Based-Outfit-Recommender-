# 👗 AI Stylist: Skin-Tone Based Outfit Recommender

## 📌 Project Overview
Choosing the right outfit for your *skin tone* and *occasion* is often confusing. Many people struggle with:
- Lack of awareness about *color harmony* → leads to low confidence.  
- Shopping platforms providing *generic recommendations*, not personalized advice.  
- Inability to *visualize outfits before purchase*, causing high return rates.  

Our solution: *AI Stylist*, a personal fashion assistant that **analyzes your skin tone** and provides **personalized outfit recommendations**, chatbot guidance for styling, and a *virtual try-on experience*. The system ensures that **every suggestion complements your natural complexion**, making fashion choices confident and tailored.

---

## 🚀 Features
1. **Skin Tone Detection**  
   - AI analyzes user photos or live webcam feed.  
   - Classifies skin tone into categories: Fair, Medium, Dark, and custom shades.  
   - Skin tone detection is the **foundation** for personalized outfit recommendations.

2. **Outfit Recommendation**  
   - Suggests outfits that **match the user’s skin tone and chosen season**.  
   - Categories: Business, Formal, Kurti, Wedding, Casual, etc.  
   - Uses a **color–outfit matching database**, optimized per skin tone.

3. **Chatbot Stylist**  
   - AI-powered stylist chatbot provides **contextual styling advice**.  
   - Example: “What should I wear for an interview?” → Suggests outfits compatible with your **skin tone**.

4. **Virtual Try-On (AR)**  
   - Upload a photo or use webcam.  
   - AI detects **face and body landmarks**, adjusts outfits in real time.  
   - Helps users **visualize how skin-tone-matched outfits look on them** before purchasing.

---

## 🛠 Technology Stack
- **AI / ML**: Python (TensorFlow, OpenCV) → skin tone detection, image preprocessing, landmark detection.  
- **Chatbot (LLM / APIs)**: AI stylist provides **personalized advice based on skin tone**.  
- **Virtual Try-On (AR)**: Mediapipe, TensorFlow.js, WebAR SDK.  
- **Frontend**: HTML, CSS, JavaScript (responsive UI).  
- **Backend**: Flask (Python) → connects AI, chatbot, and AR modules.  
- **Database**: MySQL → stores user preferences and skin-tone-based outfit data.

---

## 📊 Process Flow
1. **Skin tone analysis** (CV + preprocessing) → determines your skin tone category.  
2. Outfit recommendation based on **detected skin tone** + database → generates personalized suggestions.  
3. Chatbot provides **styling advice tailored to skin tone and occasion**.  
4. Virtual try-on overlays outfits on the user’s photo/webcam → **see the impact of skin-tone matched clothes in real time**.

---

## 💡 Use Cases
- **E-commerce Integration**: Personalized skin-tone-based outfit suggestions → increases retailer conversion rates.  
- **Personal Styling Assistant**: Daily wear, parties, weddings, interviews with outfits tailored to your **complexion**.  
- **Virtual Try-On in Fashion Apps**: Visualize outfits that match your skin tone → reduces online shopping returns.

---

## ⚡ Constraints
- **Privacy & Security**: Handling user photos safely.  
- **Cost & Resources**: AI + AR require significant compute power.  
- **Scalability**: Support multiple users with low latency.  
- **Accuracy**: Must detect skin tones accurately across diverse users, lighting, and camera conditions.

---

## ✅ Conclusion
*AI Stylist* puts **skin tone detection at the core** of fashion personalization. By analyzing a user’s skin tone first, the system ensures **every recommendation, from outfit selection to virtual try-on, complements the user’s natural complexion**. Combined with chatbot styling guidance and AR-based try-on, it helps users make **confident, informed, and personalized fashion choices** like never before.

