[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronised between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronisation, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronisation
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
   - Similarly, detect changes in the database and update the Google Sheet.
  2.	CRUD Operations
   - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
   - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
- Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
- Provide options for conflict resolution (e.g., last write wins, user-defined rules).
    
2. Scalability: 	
- Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
- Optimize for scalability and efficiency.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)
- Use ChatGPT4o/o1/Github Co-pilot, anything that accelerates how you work 💪🏽. 

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [ ] My code's working just fine! 🥳
- [ ] I have recorded a video showing it working and embedded it in the README ▶️
- [ ] I have tested all the normal working cases 😎
- [ ] I have even solved some edge cases (brownie points) 💪
- [ ] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get some help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore? 😛

We're available at techhiring@superjoin.ai for all queries. 

All the best ✨.

## Developer's Section
*Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)*

### Approach to the Problem

To tackle the real-time synchronization challenge between Google Sheets and MySQL, I implemented a system that supports bidirectional synchronization, CRUD operations, and handles basic edge cases. Below is a summary of the approach and implementation:

1. **Setup and Configuration**
   - Enabled Google Sheets API and created a service account with the appropriate credentials.
   - Configured MySQL with a database (`superJoin`) and a table (`sync_table`) to store and manage data.

2. **Python Scripts**
   - **`sheets.py`**: 
     - Managed Google Sheets interactions using the `gspread` library.
     - Provided functions to read from and write to Google Sheets.
   - **`db.py`**:
     - Handled MySQL operations using `mysql-connector-python`.
     - Implemented functions to connect to the database, read data, and insert data.
   - **`sync.py`**:
     - Implemented the core synchronization logic.
     - Added functions to synchronize data from Google Sheets to MySQL and vice versa.
     - Ensured that CRUD operations are supported and that data consistency is maintained.

3. **Real-time Synchronization**
   - Implemented a simple mechanism to periodically synchronize data between Google Sheets and MySQL.
   - Used `sync_google_sheets_to_db` to pull updates from Google Sheets and `sync_db_to_google_sheets` to push updates from MySQL to Google Sheets.

4. **Testing and Verification**
   - Tested synchronization by updating both Google Sheets and MySQL and verifying that changes were accurately reflected on both sides.
   - Ensured that CRUD operations work as expected and that the system can handle various data scenarios.

5. **Challenges and Solutions**
   - **Challenge**: Ensuring data consistency during bidirectional sync.
     - **Solution**: Implemented basic data handling and update functions to ensure that data is consistently updated and that conflicts are handled by the latest update.
   - **Challenge**: Handling different data formats and ensuring compatibility.
     - **Solution**: Carefully managed data formatting during the read and write operations to ensure compatibility between Google Sheets and MySQL.

### Video Demonstration
[Embed your video showing the project working here]

### Final Notes
The system currently handles real-time synchronization effectively with basic conflict resolution. Future enhancements may include more robust conflict handling and optimization for larger datasets and higher update frequencies.

Feel free to review the implementation and provide feedback. Thank you for considering my submission!


