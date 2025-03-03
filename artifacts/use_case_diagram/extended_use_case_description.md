## **Use Case Description: AI Chatbot Assistance**

### **Use Case Name:**  
AI Chatbot Assistance  

### **Actors:**  
- **Visitor** (Primary)  
- **Registered User** (Primary)  
- **AI Chatbot** (System)  

### **Description:**  
This use case allows visitors and registered users to interact with the **AI Chatbot** for FAQs, event recommendations, and general assistance. The chatbot retrieves relevant information and provides appropriate responses.  

### **Preconditions:**  
- The user must be on the Canti Classics website.  
- The AI chatbot must be **active and accessible**.  

### **Trigger:**  
- The user clicks on the **Chatbot Icon** in the bottom-right corner.  

### **Normal Flow (Basic Path):**  
1. The user clicks on the **Chatbot Icon**, and the chat window opens.  
2. The chatbot greets the user and presents options (e.g., FAQs, Event Info, Search).  
3. The user types a question or selects a predefined option.  
4. The chatbot processes the input and retrieves relevant information.  
5. The chatbot displays a **response** based on the query.  
6. If the user needs further assistance, the chatbot suggests related questions or actions.  
7. If applicable, the chatbot provides **links to events, artists, or recordings**.  
8. The user can continue the conversation or close the chat window.  

### **Alternative Flow (Exceptions):**  
- **Chatbot Does Not Understand the Question:**  
  1. The chatbot requests the user to **rephrase the question**.  
  2. If the question remains unclear, the chatbot offers **support contact details**.  

- **User Asks About Booking an Event:**  
  1. The chatbot retrieves upcoming event details.  
  2. The chatbot provides a **direct booking link** if applicable.  

- **User Searches for an Artist or Recording:**  
  1. The chatbot accesses the **search system** and fetches results.  
  2. The chatbot presents the most relevant options with links.  

### **Postconditions:**  
- The user successfully receives **relevant responses** or is guided to additional support.  
- If applicable, the user is redirected to an event booking or artist page.  

### **Requirement References:**  
- **FR1:** The chatbot must provide predefined FAQ responses based on user queries.
- **FR2:** The chatbot must include smooth animations for opening and closing.
- **FR3:** The chatbot must display a typing indicator when processing responses.
